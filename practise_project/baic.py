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

# Error 
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

def hello (name):
    print("Hello :",name)

name=input("enter the name:")
hello(name) 

# Leap year
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
           return True
    elif year % 400 == 0:
           return True
    else:
            return False
    
test_data = [1990,2000,2016,1987]
test_result=[False,True ,True ,False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"=>",end="")
    result = is_year_leap(yr)
    if result == test_result[i]:
            print("Ok")
    else:
            print("failed")

def scopetest():
    x=123
scopetest()
print(x)


def myfunction():
   print("Do I Know that Variable :",var)
var=1
myfunction()
print(var)

# Global variable
def myfunction():
    global var
    var=2
    print("Do I know that Variablle :",var)
var=1
myfunction()
print(var)

def myfunction(n):
    print("I got", n)
    n+=1
    print("I have",n)

var=1
myfunction(var)
print(var)

def  myfunction(mylist1):
    print("print #1:" ,mylist1)
    print("print #2:" ,mylist2)
    mylist1=[0,1]
    print("print #3:" ,mylist1)
    print("print #4:" ,mylist2)
mylist2=[2,3]
myfunction(mylist2)
print("print #5:", mylist2)  

def  myfunction(mylist1):
    print("print #1:" ,mylist1)
    print("print #2:" ,mylist2)
    del mylist1[0]
    print("print #3:" ,mylist1)
    print("print #4:" ,mylist2)
mylist2=[2,3]
myfunction(mylist2)
print("print #5:", mylist2) 

#BMI
weight=float(input("Enter the Weight in kilograms:"))
height= float(input("Enter the Height in meters:"))
def bodymaskindex(weight, height):
    if height < 1.0 or height >2.5 or \
        weight < 20 or weight>200:
        return None
        bodymaskindex=weight/height**2
    return bodymaskindex
print(bodymaskindex(weight,height))

# Function practie
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
           return True
    elif year % 400 == 0:
           return True
    else:
            return False


def days_in_month(year, month):
        if month == 2:
              if is_year_leap(year):
                    return 29
              else:
                    return 28
        elif month in [1, 3, 5, 7, 8,10, 12]:
            return 31
        else:   
             return 30
print(days_in_month(2020, 2))

 

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
     yr = test_years[i]
mo = test_months[i]
print(yr, mo, "->", end="")
result = days_in_month(yr, mo)
if result == test_results[i]:
    print("OK")
else:
    print("Failed")

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))


def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6))

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def lb_to_kg(lb):
    return lb * 0.4535923
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))
if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

# factorial
def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)
print("Factorial number is : ", factorial(5))
''''''
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product=1
    for i in range(2,n+1):
        product*=i
    return product
for n in range(1,6):
    print( n,factorial(n))

# Tuple
tuple1=(1,2,3,4,5)
tuple2=1,2,3,4,5
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))

#empty tuple
# tuple=()
# print(tuple)
# print(type(tuple))

newtuple=1,
print(newtuple)
print(type(newtuple))


mytuple=(1,10,100,1000)
#mytuple.append(10000)
#del mytuple[0]
#mytuple[1]=-10

print(len(mytuple))

#add and multiply
tuple1=(1,2,3,4,5)
tuple2=(5,6,7,8,9)
tuple3=tuple1+tuple2
print(tuple3)
tuple4=tuple3*2
print(tuple4)
for element in tuple1:
    print(element)

mylist=[1,2,3]
print(mylist)
print(type(mylist))
tup=tuple(mylist)
print(tup)
print(type(tup))

#swapping +var add
var=123
t1=1,
t2=2,
t3=3,var
t1,t2,t3=t2,t3,t1
print(t1)
print(t2)
print(t3)


#DICTIONARY
dictonary={"cat":"chat","dog": "chien","horse": "chevel"}
phoneno={"boss":456876,"suzy":146869}
emptydictonary={}
print(dictonary)
print(phoneno)
print(emptydictonary)
print(type(dictonary))
print(type(phoneno))
print(type(emptydictonary))
print(dictonary["cat"])
print(phoneno["suzy"])

words=["cat","lion","horse"]
for word in words:
    if word in dictonary:
        print(word, "->",dictonary[word])
    else:
        print(word ,"is not in dictonary")

dictonary={
    "cat": "chat",
    "dog": "chien", 
    "horse": "cheval"
}
print(dictonary)

#key method
for key in dictonary.keys():
    print(key, "->", dictonary[key])

#item method
for key, value in dictonary.items():
    print(key, "->", value)

#value method
for value in dictonary.values():
    print(value)
#copy method
copydictionary=dictonary.copy()
print(copydictionary)

#update
dictonary["cat"]="nochat"
item=dictonary["cat"]
print(item)

# key ADD
dictonary["adam"]= 436567
print(dictonary)

# delete
del dictonary["adam"]
print(dictonary)

#popitem
dictonary.popitem()
print(dictonary)
#Remove element
dictonary.clear()

dictonary.update({"duck":"swan"})
print(dictonary)

schoolclass={}
while True:
    name=input("Enter the student name :")
    if name == "":
        break
    score=int(input("Enter the student Score(0-10) :"))
    if score not in range(0,10):
        break
    if name in schoolclass:
        schoolclass[name] += (score,)
    else:
         schoolclass[name] = (score,)
for name in sorted(schoolclass.keys()):
    adding=0
    counter=0
    for score in schoolclass[name]:
        adding+=score
        counter+=1
    print(name,":",adding/counter)
    mytup'''
tup=(1,2,3)
print(tup[2])
tup=1,2,3

a,b,c=tup
print(a*b*c)

# count method
tup=1,2,34,5,6,7,5,2,8,9,5,3,2,2
duplicates=tup.count(2)
print(duplicates)

d1={"adam smith": 'a','judy paxton': 'b+'}
d2= {'marrie louis':'a','patrick white':'c'}
d3={}
for item in (d1,d2):
    d3.update(item)
print(d3)

mylist=["car",'ford','flower','tulip']
t=tuple(mylist)
print(t)

colors=(('green','#089564'),('blue', '#54677'))
colorsdictionary= dict(colors)
print(colorsdictionary)