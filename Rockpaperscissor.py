import random
paper = '''                                                          
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88     '''

scissor = '''                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                              
                                            '''
rock = '''                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
                                '''

items = [rock,paper,scissor]
game_choice = random.choice(items)

choose = int(input(f"please choose the 1 as rock 2 as paper and 3 as scissors"))
if choose == 1 :
    print(f"you have chosen \n {rock}")
    choose = rock
    print(f"computer has chosen\n{game_choice}")
    if choose == game_choice : 
        print("you win")
    else :
        print("you lose")

elif choose == 2:
    print(f"you have chosen \n {paper}")
    choose = paper
    print(f"computer has chosen\n{game_choice}")
    if choose == game_choice : 
        print("you win")
    else :
        print("you lose")
elif choose == 3:
    print(f"you have chosen \n {scissor}")
    choose = scissor
    print(f"computer has chosen\n{game_choice}")
    if choose == game_choice : 
        print("you win")
    else :
        print("you lose")
else :
    print("wrong choice")