#print("Hello")
'''
this is sample
comment for
multi line

'''
'''
print("Hello")
print("Hello")
print("Hello")
age= 21
#print(age)
print("my age i:", 21)
age="Five"
print("my age i:",age)
name= "Diksha"
Profeion= "student"
eperienced=0
print("Hello,I Am ",name,". i am a ",Profeion," profeionaly. And i have around ",eperienced," year eperienced with it")

var=0
print(not(var<=0))
'''

'''
# LIST 
number= [10,5,7,2,1]
number[0]=111
print (number[0])
print (number[1])
print (number[2])
print (number[3])
print (number[4])
del number[1]
print(len(number))
print(number)
print(number[-4])


#LIST
number=[1,2,3,4,5]
var=int(input("Enter a number:"))
number[len(number)//2]=var
print(number)
del number[len(number)-1]
print(number)


list=[1,2,3,4,5]
print("CUrrent list", list)
list.append(6)
print("updated list", list)
list. insert(3,9)
print("updated list after insert", list)

# Traversing
list=[1,2,3,4,5,6,7,8,9]
for i in range (len(list)):
    print(list[i])

# Updating using for loop

list=[]
for count in range (10):
    list.append(count+1)
print(list)

# write a program to update all elemnt of the list to add one to all element
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for count in range(len(my_list)):
    my_list[count] += 1
print(my_list)

# write a program to calculate the sum of the elemnet
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum=0
for count in range(len(my_list)):
    sum += my_list[count]
    print(sum)

#practice Question
numbers= [111,7,2,1]
print(len(numbers))
print (numbers)
numbers.append(4)
print(len(numbers))
print (numbers)
numbers.insert(0,222)
print(len(numbers))
print (numbers)
'''
'''
list=[1,2,3,4,5,6,7,8,9]
print(list[0])


for i in range (len(list)):
    print(list[i])
'''
#list=[]
#for i in range(10):
 #   list.append(i+1)
#print(list)

'''write a program to calculate the sum of the elemnet
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum=0
for count in range(len(my_list)):
    sum += my_list[count]
print(sum)

print(len(my_list))
'''
#1
'''mylist=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for count in my_list:
    sum += count
print(sum)'''


'''list={10,1,8,3,5}
for count in range (len(list)):
    print("List[",count,"]=>",list[count])
'''
'''list=[8,10,6,2,4]
list.sort()
print(list)

#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
words=["abc","xyz","aba","1221"]
count=0
for word in words:
    if  word[0] == word[-1]:
       count += 1
print(count)
  
       



#Write a Python function that takes two lists and returns True if they have at least one common member.using loop
def common_member(list1, list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
            return False

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]
print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2
print(list_3)'''

num_patterns = [
     """
###
# #
# #
# #
###""",
 """
  #
  #
  #
  #
  #""",
 """
###
  #
###
#  
###""",
     """
###
  #
###
  #
###""",
"""
# #
# #
###
  #
  #""",
    """
###
#  
###
  #
###""",
   """
###
#  
###
# #
###""",
"""
###
  #
  #
  #
  #""",
"""
###
# #
###
# #
###""",
    """
###
# #
###
  #
###"""
    ]
'''
# Eception
def badfun(n):
    if n==0:
        raise ZeroDivisionError
    else:
        return 1/n
try:
    badfun(0)
except ArithmeticError:
    print("ArithmeticError")
  
print("THE END")

from time import sleep
second =0
while True:
    try:
        print(second)
        second+=1
        sleep(1)
    except KeyboardInterrupt:
        print("dont do that")

from math import exp
ex=1
try:
    while True:
      print(exp(ex))
      ex +=2
except OverflowError:
    print("the no is too big")

dictionary={"a": "b","b":"c","c":"d"}
ch='a'
try:
    while True:
        ch=dictionary[ch]
        print(ch)
except KeyError:
    print("no such key")


#oop concept
class Myclass:
    pass

myclassobject=Myclass()
print(myclassobject)
print(type(myclassobject))

tack=[]
def push(val):
    tack.append(val)
    print(tack)
def pop():
    val=tack[-1]
    del tack[-1]
    return val
push(3)
push(2)
push(1)
print(pop())
print(tack)
print(pop())
print(tack)
print(pop())
print(tack)

#constructor
class Myclass:
    def __init__(self): #constructor predefined init
        print("constructor running")
        self.__Myclass=[] #__ encapulation
Myclassobject= Myclass()
print(Myclassobject.Myclass) #output:constructor running []
print(len(Myclassobject.Myclass))
print(type(Myclassobject.Myclass))
'''


stack=[]
class Stack: 
    def __init_(self):
        print("Constructor running!")
        self.__stack = []

def push(self, val):
    self.__stack.append(val)

    print(self.__stack)

def pop(self):
    val = self.__stack[-1]
    del self.__stack[-1]
    return val

def travers(self):

    print(self._stack)

stack_object = Stack()
print(stack_object)
stack_object.push(1)
