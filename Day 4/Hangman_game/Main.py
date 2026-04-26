import random 
import list
import art
          
random_word = random.choice(list.words)  
print(random_word)  
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
    if guessedword in final_letter :
        print("you have already entered this letter choose again")
    if guessedword not in random_word:
        lives -= 1
        print(f"you guessed {guessedword}  try again")
        if lives == 0:
            print("********************you lose game over***********************")
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
    print(art.stages[lives])
    if "_" not in display:
        gameover = True
        print("########################you win########################")
            




    
    

