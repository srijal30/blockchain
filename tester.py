import chain.block as block
import chain.blockchain as blockchain
import chain.transaction as transaction
from chain.helpers import gen_merkle
from chain.helpers import hash_key
import rsa
from hashlib import sha256




#Test for Transaction

#sender keygen
(spub, spriv) = rsa.newkeys(600)

#receiver keygen
(rpub, rpriv) = rsa.newkeys(600)

#create the chain
chain = blockchain.Blockchain()

#create 10 blocks
for i in range(10):
    #create 10 transaction.Transactions
    trans = []
    for amt in range(0, 1000, 100):
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
print( chain.is_valid() )

#Altering Chain and Checkign
chain.blocks[2].transactions[3].receiver = spub
print( chain.is_valid() )
