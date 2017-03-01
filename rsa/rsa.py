import base64
import sys
import ast

from Crypto import Random
from Crypto.PublicKey import RSA

CRYPT_BLOCK_SIZE = 128

def usage():
  print """Usage:
     rsa.py keys <private.key> <public.key>
     rsa.py encrypt public.pem inputFile <outputFile>
     rsa.py decrypt private.pem inputFile <outputFile>
     """
  exit(1)

def keys(filenames):
  private_key_filename = 'private.key'
  public_key_filename = 'public.key'
  if len(filenames) > 1:
    private_key_filename = filenames[0]
    public_key_filename = filenames[1]

  generator = Random.new().read
  key = RSA.generate(1024, generator)
  publickey = key.publickey()

  write_file(public_key_filename, publickey.exportKey())
  write_file(private_key_filename, key.exportKey())

def encrypt(args):
  if len(args) < 2:
    usage()

  public_key_file = args[0]
  source_file = args[1]

  public_key = read_file(public_key_file)
  key = RSA.importKey(public_key)
  text_to_encrypt = read_file(source_file)
  encrypted_text = ''
  while True:
    chunk = text_to_encrypt[:CRYPT_BLOCK_SIZE]
    text_to_encrypt = text_to_encrypt[CRYPT_BLOCK_SIZE:]
    encrypted_text += key.encrypt(chunk, 32)[0]
    if len(text_to_encrypt) == 0:
      break
  encoded_text = _encode(encrypted_text)
  if len(args) == 3:
    write_file(args[2], encoded_text)
  else:
    sys.stdout.write(encoded_text)

def decrypt(args):
  if len(args) < 2:
    usage()

  private_key_file = args[0]
  source_file = args[1]

  private_key = read_file(private_key_file)
  key = RSA.importKey(private_key)
  encrypted_text = _decode(read_file(source_file))
  decrypted_text = ''
  while True:
    chunk = encrypted_text[:CRYPT_BLOCK_SIZE]
    encrypted_text = encrypted_text[CRYPT_BLOCK_SIZE:]
    decrypted_text += key.decrypt(chunk)
    if len(encrypted_text) == 0:
      break

  if len(args) == 3:
    write_file(args[2], decrypted_text)
  else:
    sys.stdout.write(decrypted_text)

def read_file(filename):
  handler = open(filename, "r")
  content = handler.read()
  handler.close()
  return content

def write_file(filename, text):
  handler = open(filename, "w")
  handler.write(text)
  handler.close()

def _encode(string):
  return base64.b64encode(string)

def _decode(string):
  return base64.b64decode(string)

def main():
  arguments = sys.argv
  if len(arguments) < 2:
    usage()

  action = arguments[1]
  arguments = arguments[2:]
  if action == 'keys':
    keys(arguments)
  elif action == 'encrypt':
    encrypt(arguments)
  elif action == 'decrypt':
    decrypt(arguments)
  else:
    usage()

main()
