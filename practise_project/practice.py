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


#LIST
number=[1,2,3,4,5]
var=int(input("Enter a number:"))
number[len(number)//2]=var
print(number)
del number[len(number)-1]
print(number)
'''
#FUNCTION
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



