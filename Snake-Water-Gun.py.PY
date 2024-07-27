import random

# Dictionary to map user input to game values
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

# Taking user input
user_choice = input("Enter your choice (s for snake, w for water, g for gun): ")

if user_choice in youdict:
    you = youdict[user_choice]
    computer = random.choice([1, -1, 0])
    
    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")
    
    if computer == you:
        print("It's a draw")
    else:
        if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You win")
        else:
            print("You lose")
else:
    print("Invalid choice. Please enter 's' for snake, 'w' for water, or 'g' for gun.")
