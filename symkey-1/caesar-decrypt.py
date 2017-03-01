# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
ciphertext = ""

# read file
file = open("ciphertext.txt", "r") 
for line in file: 
    ciphertext = ciphertext + line 

# decipher
plaintext = ""
for c in ciphertext.upper():
    if c.isalpha(): 
      plaintext += I2L[ (L2I[c] - key)%26 ]
    else: 
      plaintext += c

# write out the file
deciphertext_file = open("decipheredtext.txt","w") 
deciphertext_file.writelines(plaintext) 
deciphertext_file.close()       
      
print plaintext
