# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
plaintext = ""

# read file
plaintext_file = open("plaintext.txt", "r") 
for line in plaintext_file: 
    plaintext = plaintext + line 
    
# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha():
      ciphertext = ciphertext + I2L[ (L2I[c] + key)%26 ]
    else: 
      ciphertext += c
         
# write file
ciphertext_file = open("ciphertext.txt","w") 
ciphertext_file.writelines(ciphertext) 
ciphertext_file.close() 

print "Encyption complete!"

