import random
#rules of the game
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
#user inputs his choice
while True:
    print("1) Rock \n2) Paper\n3) Scissors")
    choice = int(input("enter your choice: "))
#if user didn't input one of the correct choices
    while choice > 3 or choice < 1:
       choice = int(input("please choose one of the given numbers "))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    print("user choice is",choice_name)
    print("now it's the computers turn . . . .")
#computers turn to choose
    comp_choice = random.randint(1 , 3)

    while comp_choice == choice:
        comp_choice = random.randint(1 , 3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"
#both user and computer input their choices
    print("computer choice is",comp_choice_name)
    print(choice_name,"vs",comp_choice_name)
#what each choice from both parties lead to
    if choice == comp_choice:
        print("it's a draw!\n",end="")
        result = "Draw"
    elif (choice == 1 and comp_choice == 2):
        print("Computer wins!\n",end="")
        result = "Paper"
    elif (choice == 1 and comp_choice == 3):
        print("You win!\n",end="")
        results = "Rock"
    elif (choice == 2 and comp_choice == 1):
        print("You win!\n",end="")
        result = "Paper"
    elif (choice == 2 and comp_choice == 2):
        print("It's a draw!\n",end="")
        result = "Draw"
    elif (choice == 2 and comp_choice == 3):
        print("Computer wins! =>\n",end="")
        result = "Scissors"
    elif (choice == 3 and comp_choice == 1):
        print("Computer wins!\n",end="")
        result = "Rock"
    elif (choice == 3 and comp_choice == 2):
        print("You win!\n",end="")
        result = "Scissors"
    elif (choice == 3 and comp_choice == 3):
        print("It's a draw!\n",end="")
        result = "Draw"
    print("Would you like to play again? (Y/N) ")
    ans = input()
#if users inputs y the game restarts
    if ans =='n':
        break
print("thanks for playing")