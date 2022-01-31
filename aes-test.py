import aes

message = "Hello there"
cipherKey = 'as78ax56xty98hfe'
cipherMessage = aes.encrypt(message, cipherKey)
print('Cipher Text: ' + cipherMessage)

plainMessage = aes.decrypt(cipherMessage, cipherKey)
print('Plain Text: ' + plainMessage)