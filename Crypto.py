# Transposition Cipher

# encryption function
def scrable2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = evenChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:] # half way to the end
    oddChars = cipherText[:halfLength]  # start to half way
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

        if len(oddChars) < len(evenChars):
            plainText = plainText + evenChars[-1]
    return plainText

# CaeserEncrypt(plainText, shift)
# CaeserDecrypt(cipherText, shift)

