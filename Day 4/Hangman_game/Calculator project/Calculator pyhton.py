#Today we will create a code to make a calculator
first_number = int(input())
operand = input("please enter what operation you want to perforn +,-,/,* \n")
second_number = int(input())
a = True
def addition(first_number,second_number) :
        third_number =  first_number + second_number
        
        return third_number


def subtraction(first_number,second_number):
    third_number = first_number - second_number
    return third_number
    
def multiplication(first_number,second_number):
    third_number = first_number*second_number
    return third_number
    
def divide(first_number,second_number):
    third_number = first_number/second_number
    return third_number

result = None  
while a:       

    
    if operand == "+" :
        result = addition(first_number,second_number)
        print(result)
    elif operand == "-":
        result = subtraction(first_number,second_number)
        print(result)
    elif operand == "*":
        result= multiplication(first_number,second_number)
        print(result)
    elif operand == "/":
        result = divide(first_number,second_number)
        print(result)
    else :
        print("Wrong input")
    first_number = result 
    operand = input("please enter what operation you want to perforn +,-,/,* and press q to exit \n")
    if operand == "q":
        break
    second_number = int(input())

       

