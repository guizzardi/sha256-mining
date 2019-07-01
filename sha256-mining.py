import hashlib
import random
import time 


hash_string = 'informazione'
n = 10
start = time.time()

def encrypt_string():
    nonce = ''.join(["%s" % random.randint(0, 9) for num in range(0, n)])
    sha_signature = \
        hashlib.sha256(hash_string.encode() + nonce.encode()).hexdigest()
    return sha_signature, nonce


while 1:
    sha_signature, nonce = encrypt_string()
    print(sha_signature + ' N:' + nonce)
    if '0000' in sha_signature[:6]:
        print ('TROVATO IN %.3f SECONDI' % (time.time() - start))
        break

