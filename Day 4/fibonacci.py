n = int(input("Enter how many Fibonacci numbers you want: "))

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
