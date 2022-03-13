from hashlib import sha256

#GENERATE MERKLE: creates a merkle
def gen_merkle(transactions):
    #if no transactions
    if len(transactions) == 0:
        return ""

    #base case when there is only 1 transaction
    if len(transactions) == 1:
        return transactions[0].hash.hex() #<-- we want it to be hexadecimal

    #find the merkle of left and right side and hash them
    midpoint = int(len(transactions)/2)
    left = gen_merkle( transactions[0:midpoint] )
    right = gen_merkle( transactions[midpoint::] )

    return sha256( (left+right).encode() ).hexdigest()


#HASH KEY: hashes a public key
def hash_key(key):
    digits = key["n"]
    return sha256( str(digits).encode() ).hexdigest()
