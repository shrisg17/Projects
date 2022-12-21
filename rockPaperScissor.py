import random

#starting the game..
print("Welcome to the game!")
score = 0

#continuos loop till user loses
while 1 == 1 :
    choices = ["rock","paper","scissor"]

    #random selection of choices
    s = random.randrange(0,2)
    random_choice = choices[s]

    #taking inputs(user_choices)from user
    user_choice = input("enter your choice:")
    user_choice = user_choice.lower()

    #validating the input and scoring accordingly
    if user_choice != "paper" and user_choice != "scissor" and user_choice != "rock":
        print("invalid entry, Try again!")
    elif random_choice == "paper" and user_choice == "scissor":
        score += 1
        print("it's paper,YOU WIN! continue playing..")
    elif random_choice == "rock" and user_choice == "paper" :
        score += 1
        print(f"it's rock,YOU WIN! continue playing..")
    elif random_choice == "scissor" and user_choice == "rock":
        score += 1
        print(f"it's scissor,YOU WIN! continue playing..")
    elif random_choice == "paper" and user_choice == "scissor":
        score += 1
        print("it's paper,YOU WIN! continue playing..")
    elif user_choice == random_choice:
        print(f"Go ahead,it's {user_choice}")
    else:
        print(f"it's {random_choice} YOU LOSE! Better luck nextime!")
        break

#ends the game by displaying score of a user
print(f"Your total score is: {score},come back again!")
