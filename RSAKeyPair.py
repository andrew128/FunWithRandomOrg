'''
Create RSA Key Pair based on Random.org data

Private key will be in "./privateKey.pem"
Public key will be in "./publicKey.pem"
'''
# ----------------------------------------
from urllib.request import *
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

numBits = 1024
typeOfByte = "h"
byteURL = "https://www.random.org/cgi-bin/randbyte?nbytes=+"+str(numBits)+"&format="+typeOfByte

# output should be random byte string
def getRandomBytes(self):
    URLRequest = Request(byteURL.format(numBits))
    URLRequest.add_header("User-Agent", "andrew_wei1@brown.edu")
    data =  urlopen(URLRequest).read()
    decoded = ""
    for datum in data.splitlines():
        decoded+=str(datum.decode("utf-8"))
    return decoded.encode()

# use RSA.generate function to create keys
# key = RSA.generate(numBits, get_random_bytes)
key = RSA.generate(numBits, getRandomBytes)
privateKey = key.exportKey('PEM')
publicKey = key.publickey().exportKey('PEM')

# write keys to files
privateKeyFile = open("privateKey.pem", "w")
privateKeyFile.write(privateKey.decode("utf-8") )
privateKeyFile.close()

publicFile = open("publicKey.pem", "w")
publicFile.write(publicKey.decode("utf-8") )
publicFile.close()
