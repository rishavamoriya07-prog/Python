#we will try to generate a code to run a fibonacci sereis
a = 0
b = 1
num = int(input("how many digit you want fibonacci sereis"))
print(a)
print(b)
for i in range(1,num-1) :
    c = a+b
    a = b
    b = c
    print(c)
