
# random for generate ransom keys
from random import randint

import os

password = input("send your password: ")

# for random keys . we make a list of keys

key = ["1" , " 2", "3" ,"4", "5 ","6 ","7 ","8 ","9 ","0 ","a","b","c",
       "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
       "t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# empty password
pwd = ""
n = int(input("how many keys you want to generate: "))

for i in range(len(password)):
    guessPass = key[randint(0, n )]
    pwd = str(guessPass) + str(pwd)

print("your password is: ", pwd)
os.system("pause")

print("your password is: ", pwd)

