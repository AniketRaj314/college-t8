import socket   
import random
dictionary = {}
nums = []             
s = socket.socket()          
print("Socket successfully created")

port = 3141             
s.bind(('', port))         
print(f"socket binded to {s}") 

s.listen(5)      
print("socket is listening")  

def create_dictionary(x):
   ctr = 97
   print(f"The key is {x}")
   for _ in range(26):
      random.seed(x)
      while True:
         num = random.randrange(97, 123)
         if num not in nums:
               nums.append(num)
               dictionary[chr(ctr)] = chr(num)
               ctr += 1
               break
   print(dictionary)

   
 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print(f'Got connection from {addr}') 
  
   # send a thank you message to the client.  
   c.send(b'Thank you for connecting') 
   enc = c.recv(1024).decode().strip()
   key = int(c.recv(1024).decode())
   print(key+1)
   create_dictionary(key)
   op = ""
   for char in enc:
        for key, val in dictionary.items():
            if char == val:
               op += key


   print(op)
   
   c.close() 
