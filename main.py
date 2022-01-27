import random, string 

password_length = int(input("How long do you want your password to be? "))
password = ""

for position in range(password_length): 
  password += random.choice(string.ascii_letters)
  
print(password)

if password_length >= int(10):
 print(len(password))
else:
  print("We recommend to to use more characters")