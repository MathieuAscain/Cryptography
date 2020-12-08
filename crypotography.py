
# Program : Encryption of a message
# goal    : Encryption - pratical work 1 - algorithm 
# date    : 21/08/2020
# autor   : Mathieu Seligmann
# issue   : 0.0

word = input("Enter a sentence to encrypt ")
myKey = input("Enter a key as encryption   ")


reverseWord = word[len(word)//2:] + word[:len(word)//2]
#print(reverseWord)

"""
    creation of a key with the same quantity 
    of bits than the reversed sentence

"""

myKey = (len(reverseWord)//len(myKey))*myKey + myKey[0:len(reverseWord)%len(myKey)]
print(myKey)

userString = ''

"""
    creation of a binary user string adding the bits of "-" in between each 'octet'
    add '0101101' only between the first and the last character"
    "-" is directly substituted to its corresponding binary digits

"""
for i in range(len(reverseWord)):
    octetString = ''
    dividend = ord(reverseWord[i])
    while dividend != 0:
        octetString = str(dividend % 2) + octetString
        dividend = dividend // 2
    if (len(octetString)) != 7:
        octetString = (7 - len(octetString))*'0' + octetString
    if i == 0:
        userString = userString + octetString
    elif i == (len(reverseWord)):
        userString = userString + octetString
    else:
        userString = userString + '0101101' + octetString

userKey = ''

"""
    creation of the final binary key adding the bits of "-" in between each 'octet'
    add '0101101' only between the first and the last character"
    "-" is directly substituted to its corresponding binary digits

"""

for i in range(len(reverseWord)):
    octetKey = ''
    dividend = ord(myKey[i])
    while dividend != 0:
        octetKey = str(dividend % 2) + octetKey
        dividend = dividend // 2
    if (len(octetKey) != 7):
        octetKey = (7 - len(octetKey))*'0' + octetKey
    if i == 0:
        userKey = userKey + octetKey
    elif (i == (len(reverseWord))):
        userKey = userKey + octetKey      
    else:
        userKey = userKey + '0101101' + octetKey
    #print("Final key ", userKey)


"""
    XOR bit to bit in between the final user string and the final key string
    in order to get an encrypted string
    0^0 = 0, 0^1=1, 1^0=1, 1^1=0

"""

wordEncrypted = ''

for i in range(len(userKey)):
    crypting = int(userString[i])^int(userKey[i])
    wordEncrypted += str(crypting)
print("Crypted message :   ", wordEncrypted)


"""
    XOR bit to bit in between the encrypted string and the final key string
    in order to get a decrypted string
    0^0 = 0, 0^1=1, 1^0=1, 1^1=0

"""

wordDecrypted = ''

for i in range(len(wordEncrypted)):
    decrypting = int(wordEncrypted[i])^int(userKey[i])
    wordDecrypted += str(decrypting)
#print("Decrypted message : ", wordDecrypted)
#print("Original message :  ", userString)

i = 0
message = ''

"""
    first:  conversion from binary to ASCII number and,
    second: conversion from ASCII number to character
    initial sentence stored in message

"""

while i <= (len(wordEncrypted)-1):
    code = 0
    for k in range(6,-1,-1):
        code += int(wordDecrypted[i])*(2**k)
        i += 1
    message += chr(code)
    i += 7
    #print(message)


"""
    check if message length is even or odd
    to adapt the final message shown in the console

"""

if len(message) % 2 == 0:
    message = message[(len(message)//2):] + message[:((len(message)//2))]
else:
    message = message[(len(message)//2)+1:] + message[:((len(message)//2)+1)]
print(message)