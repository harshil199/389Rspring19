import hashlib
import string

def crack():

    # Open and read hashes.txt
    with open("hashes.txt", "r") as h:
        hashes = h.read().splitlines()

    # Open and read passwords.txt
    with open("passwords.txt", "r") as p:
        passwords = p.read().splitlines()

    # ASCII Lowercase letters
    characters = string.ascii_lowercase

    # Prepend lowercase letter to a word in passwords
    for c in characters:
        for p in passwords:
            
            # crack hashes
            val = c + p
            hashkey = hashlib.sha256(val).hexdigest()

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52
            if hashkey in hashes:
                print val,":",hashkey

if __name__ == "__main__":
    crack()