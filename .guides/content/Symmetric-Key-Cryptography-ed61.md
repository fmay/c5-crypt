![](.guides/img/acpptcryptokey.png) 

The distinction of symmetric key cryptography is the use of the same key for encryption and decryption. 

Alice is the sender who wants to send an encrypted message to Bob.

1. Alice has a file called `plaintext`.
1. She encrypts it using a *shared secret*. You can think of this as a password for now.
1. A file called `ciphertext` is created, which she can now send to Bob.
1. Bob now needs to decrypt `ciphertext` before he can read it using the *shared secret*.
1. Once, decrypted, Bob can read the original `plaintext` file sent by Alice.
