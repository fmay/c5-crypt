You are now going to get your hands dirty and do everything from the Linux command line again.

Here is a button to clean everything up in your folder.

{Clean Up}(rm rsa/encrypted.txt rsa/private.key rsa/public.key rsa/unencrypted.txt)

## Generate some keys
The first thing we need to do is to generate a **key pair** that consists of a private key and a public key.

From the command line on the left, enter `python rsa.py keys`.

If you look in the file tree, you will now find the 2 key files generated. Feel free to open these up to see what they look like.

## Encrypt your file
You are now ready to encrypt your file. We have prepared `plaintext.txt`. Enter some text in there.

Remember that in practice, you will have received someone else's public key so that you are able to unencrypt data that they send you. Similarly, if you want to send someone else data, you would send them your public key beforehand.

So, let's encrypt the file to send to Bob using Bob's public key. Now run the command `python rsa.py encrypt public.key plaintext.txt encrypted.txt`

## Unencrypt a file
Now let's imaging that Bob had sent you an encrypted file. You would have sent Bob your public key beforehand and he would have encrypted his file using your public key. 

Now that you have received it (this is `unencrypted.txt`) you decrypt it using your private key with `python rsa.py decrypt private.key encrypted.txt unencrypted.txt`

## The code
If you really want to see what the Python code looks like that handles all this, feel free to open up `rsa.py`.