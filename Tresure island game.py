#we will 

print(''' a pirate's treasure map
    ___
    ).x)
   (:_(
  
  Finrod




                                                                      



         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /''')

print("welcome to the treasure island please choose the options wisely")

print("""you are going in a straight path now two turns came what you want to choose "Left" or "right" """ )
direction = input().lower()
if(direction == "left") :
    print("Congratulation you have cleared first stage\n")
    decision = input("""now you are standing in fron of a lake what you want to choose "Swim" or "Wait" """).lower()
    if(decision == "wait") :
        print("Congratulation you have cleared second level now you are in front of three gates\n")
        color = input("""please choose one of the color among "red" "blue" "Green" \n""").lower()
        if (color == "red"):
            print("congratulation you have won the game ")
        else :
            print("Game over")

    else:
        print("game over")
else :
    print(direction)
    print("Game Over")