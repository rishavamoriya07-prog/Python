#Today we will be building the tip calculator
# Welcome to the tip calculator
# What was the total bill
# How much tip would you like to give
# How many people to split the bill
# Each person should pauy

print("welcom to the tip calculator\n")
bill = float(input("What is the to total bill ?\n"))
tip = float(input("How much percent  tip you want to give? \n"))
people = float(input("How many people are splitting the bill?\n"))
tip_in_number = round(bill*(tip/100),2)
total_bill = round(bill + tip_in_number,2)
payable = round(total_bill/people, 2)
print(f"total bill is {total_bill}")
print(f"each person has to pay {payable}")


