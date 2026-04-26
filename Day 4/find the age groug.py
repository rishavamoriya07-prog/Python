#we will generate the code for getting age group
age = int(input("please enter the age "))
if age <= 15 :
    print("enetr age is of kid")
elif age >=15 and age <= 28 :
    print("entered age is of teen")
elif age >= 28 and age <=40 :
    print("entered age is of adult")
else :
    print("entered age is of old member")