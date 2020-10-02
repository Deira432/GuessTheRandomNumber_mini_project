# Mini Project

#print statements..

def intro ():
    print("Hi there... May I know your name?.. :")
    user_name = str(input())
    print("\n\n")
    print("Hi " + user_name + " WELCOME TO THE GAME.........\n")
    print("*************************************************")
    print(" ***************GUESS THE NUMBER****************")
    print("*************************************************")
    print("\n")



#Rules of the game

def rules ():
    print("The Rules Of The Game Are As Follows :\n")
    print("User has to first select their difficulty")
    print("User will be given three chances to guess the number")
    print("In the first two attempts some clues will be given..")
    print("But third is the final attempt if its wrong, you lose...")
    print("\n")



# Random process


def game():
    intro()
    rules()

    #lev_choosing()
    print("\n")
    print("Choose your difficulty :")
    print("Difficulty 1 - Guessing number between 1 - 10 ")
    print("Difficulty 2 - Guessing number between 1 - 25 ")
    print("Difficulty 3 - Guessing number between 1 - 50 ")
    print("\n")

    #for loop for choosing the difficulty....

    for i in range(1,1000) :
        print("Choose your difficulty ")
        user_level = int(input())

        if user_level == 1 :
            print("You have selected Difficulty " , user_level )
            break
        elif user_level == 2 :
            print("You have selected Difficulty " , user_level )
            break
        elif user_level == 3 :
            print("You have selected Difficulty " , user_level )
            break
        else:
            print("Invalid input")

#importing random module...
    import random
    count = 0
    if user_level == 1 :
        answer = random.randint(1,10)
        print("Let's start the Game....")


        for a in range (1,4):

            print("Guess the number ")
            user_guess= int(input())
            count = count + 1
            if user_guess > answer :
                print("It is higher than the number")

            elif user_guess < answer :
                print("It is lower than the number")

            elif user_guess == answer :
                print("You guessed it right....!!!!!\n")
                print(".......*******YOU WIN********..........\n")
                break

            if count == 3:
                print("OOPS....Sorry you ran out off guess... \n")
                print("", answer, " is the answer\n")
                print("..........*********GAME OVER*********.............\n")

    elif user_level == 2 :
        answer = random.randint(1,25)
        print("Let start the Game....")


        for a in range (1,4):

            print("Guess the number ")
            user_guess= int(input())
            count = count + 1
            if user_guess > answer :
                print("It is higher than the number")

            elif user_guess < answer :
                print("It is lower than the number")

            elif user_guess == answer :
                print("You guessed it right....!!!!!\n")
                print(".......*******YOU WIN********..........\n")
                break

            if count == 3:
                print("OOPS....Sorry you ran out off guess...\n ")
                print("", answer , " is the answer\n")
                print("..........*********GAME OVER*********.............")


    elif user_level == 3 :
        answer = random.randint(1,10)
        print("Let start the Game....")


        for a in range (1,4):

            print("Guess the number ")
            user_guess= int(input())
            count = count + 1
            if user_guess > answer :
                print("It is higher than the number")

            elif user_guess < answer :
                print("It is lower than the number")

            elif user_guess == answer :
                print("You guessed it right....!!!!!\n")
                print(".......*******YOU WIN********..........")
                break

            if count == 3:
                print("OOPS....Sorry you ran out off guess...\n ")
                print("", answer ," is the answer\n")
                print("..........*********GAME OVER*********.............")


#...........MAIN PROGRAM :)..........

game()
