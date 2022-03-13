from hashlib import sha256
import rsa
from chain.helpers import gen_merkle, hash_key

#NOTE THE HASHES HERE WILL BE IN BYTES DUE TO RSA MODULE REQUIRING SO

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
