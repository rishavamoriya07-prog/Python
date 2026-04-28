#today we will generate a rock paper scissor
import random
rock = 1
paper = 2
scissor = 3
key = [rock, paper, scissor]
computer_decision = random.choice(key)



print("welcome to rock paper scissor game ")
choice =int(input("please choose 1 as rock 2 as paper and 3 as scissor ")
)
print(f"you choose{choice}")
print(f"computer choice {computer_decision}")
if choice >3 or choice<0:
    print("wrong choice")
elif choice == computer_decision:
    print("draw")
elif (choice == 3 and computer_decision == 1) :
    print("you lose ")
elif choice ==1  and computer_decision == 3:
    print("you win")
elif choice > computer_decision :
    print("you win")
else :
    print("you lose")
print("you lose")



