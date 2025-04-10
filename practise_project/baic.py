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
'''var=0
print(var==0)
var=1
print(var==0)'''

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


# max min function
num1=int(input("Enter the no1:"))
num2=int(input("Enter the no2:"))
num3=int(input("Enter the no3:"))
print(max(num1,num2,num3,))
print(min(num1,num2,num3))
'''
'''
# while loop
while True:
    print("I am stuck in a loop")
'''



 # store the current largest number here.
    
'''
largest_number = -999999999
number= int(input("Enter a number or type -1 to stop: "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to stop: "))
print("The largest number is:", largest_number)
'''


'''
number=int(input( "Please enter the number,0 to exist:" ))
even=0
odd=0
while number != 0:
    if number % 2==0:
        even += 1
    else:
        odd+=1
    number=int(input("Please enter the number,0 to exist:"))
print("even number",even)
print("odd number",odd)
'''
'''
#for loop
counter = 0
while counter < 100:
    counter += 1
    print(counter)

# 1 number include
for counter in range(100):
    print("counter: ",counter+1)

#2 number include
for counter in range(2, 8):
    print("The value of counter is currently", counter)


#3 number include
for counter in range(2, 8, 3):
    print("The value of counter is currently", counter)

#No output
for counter in range(1, 1):
    print("The value of counter is currently", counter)

for counter in range(2, 1):
    print("The value of counter is currently", counter)

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

power = 1
for expo in range(16):
    print("3 to the power of", expo, "is", power)
    power *= 3


 #break and countinue 
#7
print("The break instruction:")
for counter in range(1, 6):
        if counter == 3:
            break
        print("Inside the loop.", counter)
print("Outside the loop.")

#8
print("\nThe continue instruction:")
for counter in range(1, 6):
    if counter == 3:
        continue
    print("Inside the loop.", counter)
print("Outside the loop.")

# GUESS OUTPUT
print(var > 0)
print(not (var <= 0))

print(var != 0)
print(not (var == 0))

i = 1
j = not not i
print(i, j)
'''
'''
#list
numbers=[10,5,7,2,1]
print("list content", numbers)
print("list content", numbers[0])
print("list content", numbers[1])
print("list content", numbers[2])
print("list content", numbers[3])
print("list content", numbers[4])

count=0
print("list content", numbers[count])
count+=1
print("list content", numbers[count])
count+=1
print("list content", numbers[count])
count+=1
print("list content", numbers[count])
numbers[0]=111
print(numbers)
numbers[1]=numbers[4]
print(numbers)
del numbers[2]
print(numbers)
del numbers
print(numbers)'''
#
'''list=[1,2,3,4,5]
num=int(input("Enter the no:"))
list[len(list)//2]= num
print(list)
    
print(len(list))
del list [len(list)-1]
print(list)'''

'''list=[10,1,8,3,5]
for count in range (len(list)):
    print("list[",count,"]=>",list[count])

for element in list:
    print("element =>",element)

var1=1
var2=2

print("var1 :",var1)
print("var2 :",var2)

auxillary=var1
var1=var2
var2=auxillary
print("var1 :",var1)
print("var2 :",var2)

var1,var2=var2,var1
print("var1 :",var1)
print("var2 :",var2)

mylist=[10,1,8,3,5]
print(mylist)
mylist[0],mylist[4]=mylist[4],mylist[0]
mylist[1],mylist[3]=mylist[3],mylist[1]
print(mylist)

'''
#beatles
'''beatles=[]
print(beatles)
beatles.append('John Lannon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(beatles)

for i in range(1):
    beatles.append('Stu Sutcliffe')
    beatles.append('Pete Best')
print(beatles)
del beatles[3]
print(beatles)
del beatles[3]
print(beatles)
beatles.insert(0, 'Ringo Starr' )
print(beatles)

#GUESS OP
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)
print(lst)

lst = []
del lst
print(lst)'''

#BUBBLE SORT ALGORITHM
'''lst=[9,1,3,4,7,8,6,5,2]
i=0
for count in range(len(lst)-1):
    for count1 in range(len(lst)-1-count):
        if lst[count1] > lst[count1+1]:
            lst[count1],lst[count1+1]=lst[count1+1],lst[count1]
        i +=1
print(lst) 
print("loop range for :",i,"times")  

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)



lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)

lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

a = 3
b = 1
c = 2
lst = [a, c, b]
lst.sort()
print(lst)'''

#Reverse a list
#list=[1,2,3,4,5,6,7,8,9,10]
list=[1,2,3,4,5,6,7,8,9]

'''if len(list)//2 %2==0:
    t= len(list)/2
else:
    t= len(list)//2-1
print("Debugging:type(t):",type(t)) 
t=int(t)
print("Debugging:type(t):",type(t))
for index in range(t):
    list[index],list[-(index+1)]=  list[-(index+1)],list[index]
print("list after reverse =",list)
'''
'''print(list)
list.reverse()
print(list)

list1=[1]
list2=list1
list1[0]=2
print(list2)

list1=[1]
list2=list1[:]
list1[0]=2
print(list2)

list=[1,2,4,7,8]
newlist= list[1:3]
print(newlist)

#Maximum 
mylist=[17,3,11,5,1,9,7,15,13]
max=-1
for element in mylist:
    if max< element:
        max=element
        print(max)

#To find 5
mylist=[17,3,11,5,1,9,7,15,13]
found=0
for i in range(len(mylist)):
    if mylist[i]==5:
        print("Found 5 at index :",i)
        found=1
        break
if found==0:
    print("sorry, 5 is not found!")

lottery=[3,7,11,42,34,49]
drawn =[5,11,9,42,3,49]
hit=0
count=0
for i in range(len(lottery)):
    for j in range(len(drawn)):
        if lottery[i]==drawn[j]:
            hit+=1
        count+=1
print(hit)
print(count)


for element in lottery:
    if element in drawn:
        hit+=1
print(hit)
print(count)

#Remove dublicate 
mylist=[1,2,4,4,1,4,2,6,2,9]

deleted=[]
for index in range(len(mylist)-1):
    for index1 in range(index+1,len(mylist)):
        if index1 not in deleted:
            if mylist[index]==mylist[index1]:
                deleted.append(index1)
print(mylist)
print(deleted)
deleted.sort()
print(deleted)
for index in range(len(deleted)):
    del mylist[deleted[len(deleted)-(index+1)]]
print(mylist)'''

#remove dublicate using loop
'''my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list1 = []
for element in my_list:
    if element not in my_list1:
        my_list1.append(element)
print(my_list1)'''


'''squares = [x ** 2 for x in range(10)]
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)


temps=[[0.0 for h in range(24)] for d in range(31)]
print(temps)

total=0.0
for day in temps:
    total+=day[11]
    average=total/31
    print("Average Temperature at nonn:",average)

highest=-100
for day in temps:
    for temps in day:
        if temps > highest:
            highest=temps
print("The hifghest Temperature was :",highest)

rooms=[[False for r in range(20)]for f in range(15) for t in range(3)]
print(rooms)

for i in range(1):
    print("#")
else:
    print("#")
'''
#Questions
'''nums=[1,2,3]
vals =nums[-1:-2]
print(vals)

list1=[1,2,3]
list=[]
for v in list1:
    list.insert(1,v)
print(list)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
'''

#Function
'''def message():
    print("Enter the value :")
print("We start here")
message()
print("we end here.")'''

'''print("We start here")
message()
print("we end here.")
def message():
    print("Enter the value :")
'''

'''def message():
    print("Enter the value :")

message()
a= int(input())
message()
b= int(input())
message()
c= int(input())
'''
def hello (name):
    print("Hello :",name)

name=input("enter the name:")
hello(name)
