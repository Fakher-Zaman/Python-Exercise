import random
LIST = ["rock", "scissor", "paper"]

'''
-----------Game Rules------------
rock v/s paper -> paper wins
rock v/s scissor -> rock wins
paper v/s scissor -> scissor wins
'''
print("\n\t************_Game Start_************")

while True:
    compCount = 0
    userCount = 0
    choose = str(input("""
    Enter
    y/Y for Yes
    n/N for No | Exit
    :"""))

    if choose == 'y' or choose == 'Y':
        for round in range(1, 6):
            print("\n----> Round #", round, ":")
            userInput = int(input("""
            Enter
            1 for rock
            2 for scissor
            3 for paper
            :"""))
            if userInput == 1:
                userChoice = "rock"
            elif userInput == 2:
                userChoice = "scissor"
            elif userInput == 3:
                userChoice = "paper"
            else:
                print("Unexpected Input!")
            compChoice = random.choice(LIST)
            if (compChoice == userChoice):
                print("Computer Choice:", compChoice)
                print("User Choice:", userChoice)
                print("Game Draw")
                compCount = compCount + 1
                userCount = userCount + 1
            elif (userChoice == "rock" and compChoice == "scissor") or (userChoice == "rock" and compChoice == "scissor") or (userChoice == "rock" and compChoice == "scissor"):
                print("Computer Choice:", compChoice)
                print("User Choice:", userChoice)
                print("User Winner *")
                userCount = userCount + 1
            else:
                print("Computer Choice:", compChoice)
                print("User Choice:", userChoice)
                print("Computer Winner *")
                compCount = compCount + 1

        if userCount == compCount:
            print("\n\tFinally, Game Draw!")
            print("\tComputer Score:", compCount)
            print("\tUser Score:", userCount)
        elif userCount > compCount:
            print("\n\tFinally, User Win the Game")
            print("\tUser Score:", userCount)
            print("\tComputer Score:", compCount)
        else:
            print("\n\tFinally, Computer Win the Game")
            print("\tComputer Score:", compCount)
            print("\tUser Score:", userCount)

        print("\n\t************_Game End_************")

    elif choose == 'n' or choose == 'N':
        break

    else:
        print("Unexpected Input!")
