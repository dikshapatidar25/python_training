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

def play():
    number = random.randint(1, 100)
    tries = 7
    print("Guess a number between 1 and 100. You have 7 tries.")

    for i in range(tries):
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it!")
            break
    else:
        print(f"Sorry! The number was {number}")

play()
