import socket

client = socket.socket()
client.connect( ("18.117.217.121", 7000) )

client.close()

exit()

from chain.block import Block
from chain.blockchain import Blockchain
from chain.transaction import Transaction
import rsa


#CODE TO GENERATRE TO/FROM FILE
#from os.path import exists
#IF ONE KEY DOES NOT EXIST, THEN REGENERATE
#if not exists("public.pem") or not exists("private.pem"):
#    (pubkey, privkey) = rsa.newkeys(600)
#    open("public.pem", "w").write( pubkey._save_pkcs1_pem().decode() )
#    open("private.pem", "w").write( privkey._save_pkcs1_pem().decode() )
#IF THEY DO EXIST, THEN LOAD
#else:
#    pubkey = rsa.PublicKey._load_pkcs1_pem( open("public.pem").read() )
#    privkey = rsa.PrivateKey._load_pkcs1_pem( open("private.pem").read() )

#LOAD MINTING KEYS
mintpub = rsa.PublicKey._load_pkcs1_pem( open("public.pem").read() )
mintpriv = rsa.PrivateKey._load_pkcs1_pem( open("private.pem").read() )

#GENERATE KEYPAIR
(pub, priv) = rsa.newkeys(600)


#CONNECT TO THE SERVER

#USER will be sha246( publickkey[n] )