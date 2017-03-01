Generalization of Caesar Cipher

**Shift** each letter in the message `k` letters in the alphabet

Example with `k=11`

```
meet me after the toga party
XPPE XP LQEPC ESP EZRL ALCEJ
```

## Cryptanalysis of Shift Cipher
What would it take to break the shift cipher? That is, if you know that a ciphertext is obtained using a shift cipher, how would you get the original plaintext?

- **Brute Force Approach** : Try out all possible keys
- **What is the key space? How many keys are there?** " For an English alphabet 26. (Why?)
- Note that we assume here that the cryptanalyst knows the language that the original plaintext is in
