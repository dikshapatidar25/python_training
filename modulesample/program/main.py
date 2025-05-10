'''#import mod1
from mod1 import suml,prod1
#from modulesample.module.mod1 import  suml as sum_list,prodl as multi_list
print("i AM FROM MAIN FILE!!")
context=__name__
print(context)
if context =="__main__":
    print("main file was executed")
else:
    print("main i am acting as a module only!!")
print("Counter:",mod1.__counter)

my_list = [i+1 for i in range(5)]
print(my_list)
print(suml(my_list) == 15)
print(prodl(my_list) == 120)

my_list = [i+1 for i in range(5)]
print(my_list)
print(sum_list(my_list) == 15)
print(multi_list (my_list) == 120)'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module import mod1

my_list = [i+1 for i in range(5)]
print(my_list)
print("calling module function :",mod1.suml(my_list))
print("calling module function :",mod1.prodl(my_list))