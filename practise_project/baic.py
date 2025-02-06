"""
print("Hello")
print("H")
print("e")
print("l")
print("l")
print("o")

print("Hello", "Rajat","ho","are","You")
print('******')
print('******')
print("******\n******\n******\n******\n")
print("******\n"*5)
print("my", "name", "i", "kritika" ,sep="-")
print("my", "name", "i", "kritika" ,end="-")
print(2)
print(2.2)
print("2")
print(True)
AGE =4
print(AGE)
print(type (AGE))
age="four "
print(age)
print(type (age))
name="Aditya"
profession="Software developer"
experience=10
print("Hello, I am", name,". I am a",profession,"professionaly. And I have around",experience ,"with it.")
print(type (name))
"""

"""
# user input
name=input("Enter your name:")
print("Hello",str(name))

#Add two numbers // type casting
'''sum1= input("Enter first no:")
sum2= input("Enter second no:")
print("sum of two no is:",int (sum1)+int(sum2))


'''
# sum two floating number
sum1= input("Enter first no:")
sum2= input("Enter Second no:")
print("sum of two floating no:",float(sum1)+float(sum2))
"""
"""
# Write a program to calculate  hypotenenus to sides
a= input("Enter first side:")
b = input("Enter second sides:")
cal= ((float(a)**2) + (float(b)**2))**0.5
print("hypotenuse of two sides is:", cal)
"""
# comparison Operator
var=0
print(var==0)
var=1
print(var==0)

# Control flow statement
'''
num1=int(input("Enter the no1:"))
num2=int(input("Enter the no2:"))
if num1>num2:larger_number=num1
else:larger_number=num2
print("The larger number is:", larger_number)
'''

# if-else statement
'''
num1=int(input("Enter the no1:"))
num2=int(input("Enter the no2:"))
num3=int(input("Enter the no3:"))
largest_number= num1
if num2 >= largest_number:
    largest_number= num2
if num3 >=largest_number:
    largest_number= num3 
print("The largest number is:",largest_number)
'''

#elif statement
num1=int(input("Enter the no1:"))
num2=int(input("Enter the no2:"))
num3=int(input("Enter the no3:"))
if num1>num2:
        print("num1 is largest:")
elif num2>num3:
        print("num2 is largest:")
else:
    print("num3 is largest")


num1=int(input("Enter the no1:"))
num2=int(input("Enter the no2:"))
num3=int(input("Enter the no3:"))
print(max(num1,num2,num3,))
print(min(num1,num2,num3))


