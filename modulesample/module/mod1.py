'''import main
print("i AM INSIDE MOD1 !!yAH!")

print("I like to be a module.")
print(__name__)
context=__name__
print(context)
if context =="__main__":
    print("mod1 file was executed")
else:
    print("mod1 i am acting as a module only!!")


__counter = 0
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")'''
#!/usr/bin/env python3
#"" module.py - an example of a Python module ""
__counter = 0
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum
def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod
