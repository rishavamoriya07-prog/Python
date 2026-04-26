def calculate_love_score(name1,name2):
    total_name = name1+name2
    first = "true"
    second = "love"
    counter1 = 0
    counter2 = 0
    for i in  first :
        for j in total_name:
            if i == j:
                counter1 += 1 
    for i in second:
        for j in total_name :
            if i == j :
                counter2 += 1 
    print(int(str(counter1)+str(counter2)))


calculate_love_score(name1 ="Angela Yu",name2="Jack Bauer")
                
    
        