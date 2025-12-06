# 32 bit hexa te convert hoi jai Md5
# The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities
# Bit Size : 32


import hashlib
 

 
hash_value = input("md5 hash: ")
 
wordlist = input("File name: ")
try:
    pass_file = open(wordlist,"r")
except:
    print("No file found :(")
    quit()
 
for word in pass_file:
 
    enc_wrd =word.encode('utf-8')
    digest =hashlib.md5(enc_wrd.strip()).hexdigest()
   # print(word)
   #  print(digest)
   #  print(pass_hash)
    if digest.strip() == hash_value.strip():
        print("password found")
        print("Password is " + word)
        
        break
 
else:
    print("password not in list")  
