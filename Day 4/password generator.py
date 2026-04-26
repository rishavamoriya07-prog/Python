#today we will generate a code to password genearatr
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l = int(input("how many alphabets you want in your password\n"))
n = int(input("how many numbers you want in your password\n"))
s = int(input("how many symmbold you want in your password\n"))

random_letter = random.sample(letters,l)
random_number = random.sample(numbers,n)
random_symbols = random.sample(symbols,s)

password = ""

for letter in range(1, l+1) :
    password = password + random.choice(letters)
for number in range(1, n+1):
    password = password + random.choice(numbers)
for symbol in range(1,s+1) :
    password = password + random.choice(symbols)
print(password)

List_pass = list(password)
random.shuffle(List_pass)
password = "".join(List_pass)
print(password)

    
