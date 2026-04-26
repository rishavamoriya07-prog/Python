#we witll write a code to find the largest of the number
numbers = [1,2,3,4,5,6,18,2,3,15,20,5,3,1,1,1,2,3,5,]

max_num = 0
for number in numbers :
    if number > max_num :
        max_num = number
print(max_num)
