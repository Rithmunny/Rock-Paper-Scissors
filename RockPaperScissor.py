import random

def play_game():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid input. Please choose rock, paper, or scissors."

result = play_game()
print(result)
