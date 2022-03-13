import chain.block as block
import chain.blockchain as blockchain
import chain.transaction as transaction
from chain.helpers import gen_merkle
from chain.helpers import hash_key
import rsa
from hashlib import sha224, sha256

#Test for Transaction

#minter key loading
mintpub = rsa.PublicKey._load_pkcs1_pem( open("chain/minting_pub.pem").read() )
mintpriv = rsa.PrivateKey._load_pkcs1_pem( open("chain/minting_priv.pem").read() )

#sender keygen
(spub, spriv) = rsa.newkeys(600)

#receiver keygen
(rpub, rpriv) = rsa.newkeys(600)

#create the chain
chain = blockchain.Blockchain()

#create 10 blocks
for i in range(10):
    #create 10 transactions
    trans = []

    message = "10000"+hash_key(mintpub)+hash_key(spub)
    message = sha256( message.encode() ).digest()
    signature = rsa.sign( message, mintpriv , 'SHA-256' )
    trans.append( transaction.Transaction(10000, mintpub, spub, signature) )

    for amt in range(0, 1000, 100 ):
        message =  str(amt+i) + hash_key(spub) + hash_key(rpub)
        #append the data
        message = sha256( message.encode() ).digest() #<--- we need it to be in bytes format
        #sign the data
        signature = rsa.sign( message, spriv, 'SHA-256')
        #create transaction.Transaction
        trans.append( transaction.Transaction( amt+i, spub, rpub, signature ) )

    #find the block data
    merkle = gen_merkle(trans)
    nonce = 0
    while sha256( (chain.blocks[-1].hash+merkle+hash_key(rpub)+str(nonce)).encode() ).hexdigest()[:3] != "0"*3:
        nonce+=1

    #add the block to the chain
    chain.add_block( trans , hash_key(rpub) ,nonce)

#Check if chain is valid
#print( chain )
print( chain.is_valid() )
print( chain.get_balance( hash_key(spub) ) )
print( chain.get_balance( hash_key(rpub) ) )

#Altering Chain and Checkign
chain.blocks[2].transactions[3].receiver = spub
print( chain.is_valid() )
print( chain.get_balance( hash_key(spub) ) )
print( chain.get_balance( hash_key(rpub) ) )
