import hashlib
from block import Block
from helpers import gen_merkle

#FOR THE FUTURE:
# add change difficulty
# add json dump

#class blockchain
class Blockchain():
    #INSTANCE
    blocks = []
    difficulty = 3

    #CONSTRUCTOR
    def __init__(self):
        #add genesis block
        self.blocks.append( Block("0"*64, [], "Salaj Rijal", 0) )

    #METHODS
    #ADD BLOCK
    def add_block(self, transactions, creator, nonce):
        #generate the hash
        hash = hashlib.sha256( self.blocks[-1].hash.encode() )
        hash.update( gen_merkle(transactions).encode() )        
        hash.update( creator.encode() )        
        hash.update( str(nonce).encode() )
        hash = hash.hexdigest()  
        #check if hash is signed
        if hash[:self.difficulty] == "0"*self.difficulty:
            self.blocks.append( Block(self.blocks[-1].hash, transactions, creator, nonce) )
            return True
        return False
        
    #IS VALID: checks if the blockchain is valid
    #-all hashes will be generated again and checked
    #-check if all the previous hashes are linked
    #-checks if all transactions are valid
    def is_valid(self):
        for index in range( 1, len(self.blocks) ):
            #check if hash matches generated hash
            if self.blocks[index].hash != self.blocks[index].gen_hash():
                return False
            #check if previous hash matches
            if self.blocks[index].p_hash != self.blocks[index-1].hash:
                return False
            #check if block has valid transactions
            if not self.blocks[index].valid_transactions():
                return False
        return True

    #LENGTH: return the amount of blocks <-- ? is this necasarry?
    def length(self):
        return len( self.blocks )

    #TO STRING
    def __str__(self):
        result = ""
        result += "DIFFICULTY: " + str(self.difficulty) + "\n\n"
        for block in self.blocks:
            result += str(block) + "\n\n"
        return result


#TESTS
if __name__ == "__main__":
    chain = Blockchain()
    print( chain.is_valid() )
    print( chain )
