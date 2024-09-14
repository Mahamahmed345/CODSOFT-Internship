import random
import string
def pas(length):
    password=''
    chr=string.ascii_letters+string.digits
    
    for i in range(length):
      password+=str(random.choice(chr))
    return password
    
      
print("PASSWORD GENERATOR\nEnter length more than or equal to 7")
            
while True:
      length=int(input("Enter password length:"))

      if length>=7:
            print('YOUR PASSWORD IS:',pas(length))
            break;
      else:
            print("Enter valid length")
