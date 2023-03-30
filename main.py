#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all=[letters,numbers,symbols]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
len_letters=len(letters)
len_number=len(numbers)
len_symbols=len(symbols)
password=""
total=nr_letters+nr_numbers+nr_symbols
while(1):
  r=random.randint(0,2)
  if(r==0 and nr_letters!=0):
    password=password+all[0][random.randint(0,len_letters-1)]
    nr_letters-=1   
  elif(r==1 and nr_numbers!=0):
    password=password+all[1][random.randint(0,len_symbols-1)]
    nr_numbers-=1
  elif(r==2 and nr_symbols!=0):
    password=password+all[2][random.randint(0,len_symbols-1)]
    nr_symbols-=1
  elif(nr_letters==0 and nr_numbers==0 and nr_symbols==0):
    break
       
print(password)  
#githubDirectCommit
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P