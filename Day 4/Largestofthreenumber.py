#we will write the program to find the largest of the number
a = int(input("please enter the first number\n"))
b = int(input("please enter the second number\n"))
c = int(input("please enter the third number\n"))
print(f"your first number is{a}")
print(f"your first number is{b}")
print(f"your first number is{c}")
if a >b :
    if  c > a :
        print(f"gratest number is {c}")
    else : 
        print(f"greatest number is {a}")
elif b > c :
    print(f"greatest number is {b}")
else :
    print(f"greates number is {c}")
    

