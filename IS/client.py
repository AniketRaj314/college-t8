import socket
import random             
s = socket.socket()          
dictionary = {}
nums = []

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

port = 3141              
s.connect(('127.0.0.1', port)) 
print(s.recv(1024).decode()) 
inp = input("Enter the text:")
key = int(input("Enter the key value:"))
create_dictionary(key)
encrypted_text = ""
for c in inp:
   encrypted_text += dictionary[c]
for _ in range(1024 - len(encrypted_text)):
   encrypted_text += " "
s.send(encrypted_text.encode())
s.send(str(key).encode())
s.close() 
