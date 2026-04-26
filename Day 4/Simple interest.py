#today we will create the program to gennerate SI
p = float(input("please enter the principal amount\n"))
r = float(input("please entere rate of interest % \n"))
t = float(input("please enter the time in months\n"))
print("please be patience we are calculating simple interest")
SI = (p*r*t)/(100*12)
print(f"your simple interest is {SI}")