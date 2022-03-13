import hashlib
from chain.helpers import gen_merkle

#FOR THE FUTURE:
# add json dump
# make data into dictonary
# maybe validate merkle?
 
#class block
class Block():
    #CONSTRUCTOR               
    def __init__(self, p_hash: str, transactions: list, creator: str, nonce: int):
        #same for everyone
        self.p_hash = p_hash
        self.transactions = transactions 
        #dependent on user
        self.creator = creator
        self.nonce = nonce
        #generate the merkle root
        self.merkle = gen_merkle(transactions)
        #generate the hash
        self.hash = self.gen_hash()

    #METHODS
    #GENERATE HASH: generates a hash
    def gen_hash(self):
        #p_hash + merkle + creator + nonce
        param = ( self.p_hash+self.merkle+self.creator+str(self.nonce) ).encode()
        return hashlib.sha256(param).hexdigest()

    #IS VALID: checks if data matches hash and if transactions are valid
    #VALID TRANSACTIONS: returns true only if all the transactions are valid   
    def valid_transactions(self):
        #checks the merkle root
        if gen_merkle(self.transactions) != self.merkle:
            return False
        #check transactions individually
        for transaction in self.transactions:
            if not transaction.is_valid():
                return False
        #return true at the end
        return True

    #TO STRING: prints the block in a readable format with all important info
    def __str__(self):
        result = ""
        result += "HASH: " + self.hash + "\n"
        result += "PHASH: " + self.p_hash + "\n"
        result += "MERKLE: " + self.merkle + "\n"
        result += "TRANSACTIONS:\n"
        for transaction in self.transactions:
            result += str(transaction) + "\n"
        result += "CREATOR: " + self.creator + "\n"
        result += "NONCE: " + str(self.nonce) + "\n"
        return result

