# #we will generate ac doe 
# #todoRandomly choose a word from the lisy
# #tpdp as the user to gues a letter and assign their  and check if the user guessed correct or not
# import random
# word_list = ['rishabh', 'aman', 'neeraj', 'manoj','rajat']
# choose_word = random.choice(word_list)
# placeholder = ""
# for y in choose_word :
#     placeholder = placeholder + "-"
# print(placeholder)



# game_over = False
# guess_letter = ""
# final_word = list(placeholder)
# i = 0
# while not game_over :
#     guess = input("input the guess number").lower()
#     guess_letter = ""
#     for x in choose_word :
#         if x == guess:
#             guess_letter += x
#         else :
#             guess_letter += "-"
        
    
#         for z in guess_letter :
                
#             if z == "-" :
#                 continue
                
#             else :
#                 final_word[i] = z
#             i = i+1
        
# print(str(final_word))
# if "-" not in "".join(final_word) :
#     game_over = True
#     print("you win")            
import random 
stages = [
    '''  --------
  |      |
  |      O
  |     /|\\
  |     / \\
  |
-+---+''',
    '''  --------
  |      |
  |      O
  |     /|\\
  |     / 
  |
-+---+''',
    '''  --------
  |      |
  |      O
  |     /|\\
  |     
  |
-+---+''',
    '''  --------
  |      |
  |      O
  |      |
  |     
  |
-+---+''',
    '''  --------
  |      |
  |      O
  |      
  |     
  |
-+---+''',
    '''  --------
  |      |
  |      
  |      
  |     
  |
-+---+''',
    '''  --------
  |      
  |      
  |      
  |     
  |
-+---+'''
]          
words =  [
    "python", "variable", "function", "loop", "string",
    "integer", "boolean", "dictionary", "tuple", "list",
    "class", "object", "inheritance", "module", "package",
    "debugging", "exception", "syntax", "compiler", "interpreter"
]
        
random_word = random.choice(words)  
 
placeholder = ""  
for i in range(0,len(random_word)) :
    placeholder += "_"
print(placeholder)
  
final_letter = []
gameover = False
lives = 6

while not gameover :
    display = ""
    guessedword = input("please input the letter \n").lower() 
    if guessedword not in random_word:
        lives -= 1
        print("wrong guess")
        if lives == 0:
            print("you lose game over")
            gameover = True
         
    for i in random_word:
        if i == guessedword :
            display+= i
            final_letter.append(guessedword)
        elif i in final_letter :
            display += i
            
        else :
            display+= "_"
    
    print(display)
    print(stages[lives])
    if "_" not in display:
        gameover = True
        print("you win")
            




    
    

