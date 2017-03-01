You are now going to get your hands dirty and do everything from the Linux command line again.

## Generate some keys
The first thing we need to do is to generate a **key pair** that consists of a private key and a public key.

From the command line on the left, enter `python rsa.py keys`.

If you look in the file tree, you will now find the 2 key files generated. Feel free to open these up to see what they look like.

## Encrypt your file
You are now ready to encrypt your file. We have prepared `plaintext.txt`. Enter some text in there.

Now run the command `python rsa.py encrypt plaintext.txt encrypted.txt`