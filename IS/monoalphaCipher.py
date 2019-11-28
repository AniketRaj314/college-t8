import random
import string

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  #initial array

b = list(string.ascii_lowercase)                       #randomly generated list of characters
random.shuffle(b)
print ''.join(b[:94])

c = []
d = []

def listToString(c):                                    #function for converting to string
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in c:  
        str1 += ele   
    # return string   
    return str1  

print "randomly generated string is ",b
msg_len = raw_input("enter msg length ")                #taking message_length as input from user
msg = raw_input("enter your message ")                  #taking message as input from user

def encryption():                                       #encryption function
    for i in range(int(msg_len)):
        for j in range(26):
            if msg[i] == a[j]:
                pos = j
                c.append(b[pos])
    return c
            
def decryption():                                       #decryption function
    for k in range(int(msg_len)):
        for h in range(26):
            if c[k] == b[h]:
                pos1 = h
                d.append(a[pos1])
    return d

encrypted_text = encryption()                           #calling encryption funtion
cipher = listToString(encrypted_text)                   #converting to string
print "encrypted message is ", cipher                   #printing the encrypted message


decrypted_text = decryption()                           #calling decryption function
decipher = listToString(decrypted_text)                 #converting to string
print "decrypted msg is ",decipher                      #printing the decrypted message