#we will generate a code to print table of n

n = int(input("please neter the number you want to get multiplication\n"))
times = int(input("how many times you want the multiplication\n"))
i = 1
for mul in range(i,times+1):
    table = n *i
    print(table)
    i=i+1
    