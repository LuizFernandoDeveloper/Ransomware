from fileinput import close
import os 
import pyaes

# Open the file encrypted

fileName = "test.txt.learningRansomware"
file = open(fileName, "rb")
fileData = file.read()
file.close()

# kay to decrypt the encrypted file 

key = b"learningRansomwa" # Key of 16 bits
aes = pyaes.AESModeOfOperationCTR(key)

# decrypt the file 

decryptData = aes.decrypt(fileData)

# Remove  the file encrypted

os.remove(fileName)
newFile = "test.txt"
newFile = open(f'{newFile}', "wb")
newFile.write(decryptData)
newFile.close

# Finish 