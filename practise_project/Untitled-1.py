#operator
'''Write a program to create 2 variables, initialize them with integer values, Print the sum of both
variables
○ Write a program to create 2 variables, initialize them with integer values, Print the difference of
both variables
○ Write a program to create 2 variables, initialize them with integer values, Print the multiplication of
both variables
○ Write a program to create 2 variables, initialize them with integer values, Print the division of both
variables
○ Write a program to create 2 variables, initialize them with integer values, Print the division floored
value of both variables
○ Write a program to create 2 variables, initialize them with integer values, Print the remainder after
division of both the variables
○ Write a program to create 2 variables, initialize them with integer values, Print the value which is
first variable to the power of second variable
'''
# Solution
'''a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("sum of a and b is :",a+b)
print("difference of a and b is :",a-b)
print("multiplication of a and b is :",a*b)
print("division of a and b is :",a/b)
print("floor division of a and b is :",a//b)
print("remainder of a and b is :",a%b)
print("power of a and b is :",a**b)
'''
import random

def get_max_attempts(difficulty):
    if difficulty == 'easy':
        return 10
    elif difficulty == 'medium':
        return 7
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid difficulty.")
        return 7

def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.\n")

    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
    max_attempts = get_max_attempts(difficulty)
    
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"\nYou have {max_attempts} attempts to guess the number.\n")

    while attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!\n")
        elif guess > secret_number:
            print("Too high!\n")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} tries.")
            break
    else:
        print(f"❌ Out of attempts! The number was {secret_number}.\n")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
