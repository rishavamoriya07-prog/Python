# #we will generate a code for factorial with for loop
# fact = int(input("please enter the number you want to get the factorial"))
# num = fact
# for x in reversed(range(1,fact)) :
    
#     num = num*x
    
#     print(num)
# print(num)
    
def fact(n):
    if(n<0):
        return 0
    if(n<2):
        return n
    return n*fact(n-1)

print(fact(1))
    