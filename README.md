# AES encryption

This is an implementation of the AES encryption algorithm in Python, using 128 bits for both block and key size.

## Usage

```
import aes

message = "Hello there"
cipherKey = 'as78ax56xty98hfe'
cipherMessage = aes.encrypt(message, cipherKey)
print('Cipher Text: ' + cipherMessage)

plainMessage = aes.decrypt(cipherMessage, cipherKey)
print('Plain Text: ' + plainMessage)
```