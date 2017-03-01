import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import sys
import hashlib

def _encode(string):
  return base64.b64encode(string)

def _decode(string):
  return base64.b64decode(string)

def getAESObject(password, iv):
  return AES.new(password, AES.MODE_CFB, iv)

def encrypt(string, password):
  iv = Random.new().read(16) # initial vector
  encryptedString = getAESObject(password, iv).encrypt(string)
  return _encode(iv + encryptedString)

def decrypt(string, password):
  encryptedString = _decode(string)
  iv = encryptedString[:16]
  return getAESObject(password, iv).decrypt(encryptedString[16:])

def readFile(filename):
  f  = open(filename, "r")
  content = f.read()
  f.close()
  return content

def writeFile(filename, text):
  f  = open(filename, "w")
  f.write(text)
  f.close()

def hash(string, size):
  hashObject = MD5.new(string)
  hashObject.digest_size = size
  return hashObject.hexdigest()

def usage():
  print('Usage: aes.py encrypt|decrypt inputFile <outputFile>')
  exit(1)

def main():
  arguments = sys.argv
  if (len(arguments) <  3):
    usage()

  action = sys.argv[1]
  inputFile = sys.argv[2]
  password = raw_input('Enter Password: ')
  # fo AES256 we need 32 bit key, lets create it from password
  passwordHash = hash(password, 32)
  text = readFile(inputFile)

  if (action == 'encrypt'): # encription
    encryptedText = encrypt(text, passwordHash)
    if (len(sys.argv) == 4):
      writeFile(sys.argv[3], encryptedText)
    else:
      print(encryptedText)

  elif(action == 'decrypt'): # decryption
    decryptedText = decrypt(text, passwordHash)
    if (len(sys.argv) == 4):
      writeFile(sys.argv[3], decryptedText)
    else:
      print(decryptedText)
  else:
    usage()

main()