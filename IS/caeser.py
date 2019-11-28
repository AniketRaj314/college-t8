key = input("enter your key ")					 #taking input as key
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  #initial array
arr = list()
msg_len = raw_input("enter length of msg to be encrypted ")
r = a[::-1]          							 #reversing the list for deryption

def decrption(b,r):                               #decrpytion function
	c=[]
	for w in range(int(msg_len)):
		for q in range(26):
			if b[w] == r[q]:
				pos = q
				new_pos = (pos + (key+1)) % 26                                                                       
				c.append(r[new_pos])
	decipher = listToString(c) 
	print "decryption: ",decipher

def encryption():                              	  #encryption function
	arr = raw_input("enter input msg ")       	  #input msg array		
	b=[]
	for k in range(int(msg_len)):                 
		for j in range(26):
			if arr[k] == a[j]:
				pos = j
				new_pos = (pos + (key+1)) % 26 
				b.append(a[new_pos])
	cipher = listToString(b) 
	print "encryption: ",cipher
	decrption(b,r)                                  #calling decyption function

def listToString(c):  								#converting to string
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in c:  
        str1 += ele   
    # return string   
    return str1  

encryption()										#calling encryption function

