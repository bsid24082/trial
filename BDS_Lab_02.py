# def fun1():
#     print("Inside the function")
#     a = 5
#     b = 14
#     c = a +b
#     print("Sum of above 2 numbers:", c)
#
# fun1()
#
# def evenOROdd(x):
#     if(x%2 == 0):
#         print("The number is even")
#     else:
#         print("The number is odd")
#
# x = int(input("Enter a number:"))
# evenOROdd(x)
# def fun3():
#     x1 = int(input("First number is:"))
#     x2 = int(input("Second number is:"))
#     x3 = int(input("Third number is:"))
#     x4 = x1 + x2 +x3
#     print("The sum of given three numbers is:",x4)
# fun3()
#
# def sum1():
#     print('Sum Explanation')
#     a = int(input("Enter num1:"))
#     b = int(input("Enter num2:"))
#     c =  int(input("enter num3: "))
#     d = a + b + c
#     print("Sum of three number is: ", d)
# sum1()

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):

    print("My first name is",firstname)
    print("My last name is",lastname)

firstname="Siddarth"
lastname="Bhardwaj"
student(firstname,lastname)


###############
# An empty function that does nothing,
# This is referred to as stub,
# A temporary placeholder, that may be fully implemented at a later time.

def f():
    pass

f()

#############
# Argument Passing
def f(qty,item, price):
    print(f'{qty} {item} cost$ {price:.2f}')

f(6, 'bananas', 1.74)

# f(6, 'bananas')
#f(6, 'bananas;, 1.74, 'kumquats')

# Keyword Arguments
f(qty = 6, item = 'bananas', price = 2.745)
f(item = 'apple', qty = '1kg', price = 20.7)



# When positional and keyword arguments are both present, all the positional arguments must come first:

#f(6, item = 'bananas', 1.74)

## Default Parameters
def f(qty = 6, item = 'bananas', price = 1.74):
    print(f'{qty} {item} cost$ {price: .2f}')

f(4, 'apples', 2.24)

f (4, 'apples')
f(4)
f(item = 'kumquats', qty = 9)

# A return statement in a python function serves two purposes:

#It immediately terminates the function and
# passes execution control back to the caller
# It provides a mechanism by which the function can pass data back to the caller.

def f1():
    print('Hello there, Whats your name?')
    print("Hello to you too! My name is Siddharth")
    return
f1()

def f(x):
    if x < 0:
        return "negative"
    if x > 100:
        return "above 100"
    print(x)

print(f(-3))
f(69)
f(10)
f(3)
print(f(267))

# Returning Data to the caller
def f2():
    return 'Kobra'
s = f2()
print(s)



