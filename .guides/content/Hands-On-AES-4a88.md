You can now try out some encryption yourself. This time you are going to open up a Linux terminal window and run the command yourself.

On the left hand side is a terminal window. We have written a program in the Python language to handle this. 

Press the button below to clean up the folder with the various files. You can press this button each time you want to experiment again.

{Clean Up}(rm aes/deciphered.txt aes/cipher.txt)

## Edit your plain text
The first thing to do is to type some plain text into a file. Click on `plaintext.txt` in the file tree to open it up.

## Encrypt
In the terminal window, type in the following command 

```
python aes.py encrypt plaintext.txt cipher.txt 
```

This runs the Python script `aes.py` and tells it to encrypt the file called `plaintext.txt` and write the output to `cipher.txt`.

You will be prompted to enter a password. Enter something short and simple.

## Open the cipher text
Once you have run the program, you will be able to see this file in the file tree. Open it and take a look.

This would be the file that you would send to someone.

## Decrypt the cipher text
The encrypted `cipher.txt` is now deciphered by someone using the same password. 

We will do this in the same place using the following command.

```
python aes.py decrypt cipher.txt deciphered.txt 
```

## Get the password wrong
Try the decryption step again but use the wrong password. If you then try to open the file, you will probably get an error saying `can't open binary file`. This is because the decryption step mangled things and it cannot be shown as text.

Feel free to press the button at the top of the page and start again.



