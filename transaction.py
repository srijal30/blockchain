from helpers import gen_merkle, hash_key
from hashlib import sha256
import rsa

#class transaction
class Transaction():
    #INSTANCE
    #not implemented

    #CONSTRUCTORS
    def __init__(self, amount: int, sender: rsa.PublicKey, receiver: rsa.PublicKey, signature: bytes):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
        #generate the hash
        self.hash = self.gen_hash() #hash will be in bytess
    
    #METHODS
    #GENERATE HASH: generate hash with given info    
    def gen_hash(self):
        h = sha256()
        h.update( str(self.amount).encode() ) #string representation of amount
        h.update( hash_key(self.sender).encode() ) #hash of public key of sender
        h.update( hash_key(self.receiver).encode() ) #hash of public key of receiver
        return h.digest()
    
    #IS VALID: checks if transaction is valid
    def is_valid(self):
        #first check if signature is valid
        try: 
            rsa.verify( self.gen_hash(), self.signature, self.sender )
        except:
            return False #if error occurs, then return false
        #check if the amount is valid
        
        #add code to check if it is mint key, then it doesnt matter
        
        #return true at the end
        return True
        
    #TO STRING: prints out transaction in this format "amount:from:sender-to-receiver"
    def __str__(self):
        result = ""
        result += "\tFROM: "  + hash_key(self.sender) + "\n"
        result += "\tTO: " + hash_key(self.receiver) + "\n"
        result += "\tAMOUNT: " + str(self.amount) + "\n"
        result += "\tSIGNATURE: " + self.signature.hex() + "\n"
        result += "\tHASH: " + self.hash.hex() + "\n"
        return result

#TESTING
if __name__ == "__main__":
    #sender keygen
    (spub, spriv) = rsa.newkeys(600)
    #receiver keygen
    (rpub, rpriv) = rsa.newkeys(600)

    from blockchain import Blockchain
    chain = Blockchain()
    
    #create 10 blocks
    for i in range(10):
        #create 10 transactions
        trans = []
        for amt in range(0, 1000, 100):
            message =  str(amt+i) + hash_key(spub) + hash_key(rpub)
            #append the data
            message = sha256( message.encode() ).digest() #<--- we need it to be in bytes format
            #sign the data
            signature = rsa.sign( message, spriv, 'SHA-256')
            #create transaction
            trans.append( Transaction( amt+i, spub, rpub, signature ) )
        #generate the merkle
        merkle = gen_merkle(trans)
        #find the nonce
        nonce = 0
        while sha256( (chain.blocks[-1].hash+merkle+hash_key(rpub)+str(nonce)).encode() ).hexdigest()[:3] != "0"*3:
            nonce+=1
        #add the block
        chain.add_block( trans , hash_key(rpub) ,nonce)
    #check if chain is valid
    print( chain.is_valid() )
    #alter chain
    chain.blocks[2].transactions[3].receiver = spub
    #check if valid
    print( chain.is_valid() )
