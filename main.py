import random

 
while True:
    list = ["R", "P", "S"]
    print("R for Rock, P for Paper, S for scissors")
    UserOption = input("Enter an option ('R' is for rock, 'P' is for paper, 'S' is for Scissors): ")
    user_option = UserOption.upper()
    computer_option = random.choice(list)
    if user_option not in list:
        print("Enter the valid option")
    elif user_option in list:
       print(f"\nPlayer ({user_option}) : CPU ({computer_option})\n")  
       
    if user_option == computer_option:
        print(f"Both players selected {user_option}. It's a tie!")


    elif user_option == "R":
        if computer_option == "S":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_option == "P":
        if computer_option == "R":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
    elif user_option == "S":
        if computer_option == "P":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break
        

        