
#wewillgetthe factorial
fact = int(input("enetr the number you want to get the factorial\n"))
num = fact
while fact >= 1 :
    fact = fact-1
    num = num * (fact)
    if fact == 1 :
        break
    print(num)
print(num)
