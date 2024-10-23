#Recursive function: a function calling it self is known as recursive function

#example factorial of a given number:
# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))
n = 5
result = factorial(n)
print("The factorial of", n, "is", result)

#map  function
#The map() function executes a specified function for each item in
# an iterable. The item is sent to the function as a parameter.
#Syntax
#map(function, iterables)
#examnple:
def fruits(a, b):
  return a + b
x = map(fruits, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)
print(list(x))

#2.
n=[1,2,3,4,5,6,7,8,9,10,11,12]
def squr(n):
    return n*2
m=map(squr,n)
print(list(m))

#filter function:
#The filter() function returns an iterator where the items are 
# filtered through a function to test if the item is accepted or not.
#syntax:
#filter(function, iterable)
#example:
def even(n):
    if n%2==0:
        return True
    else:
        return False
n=[1,2,3,4,5,6,7,8,9,10,11,12]
l=filter(even,n)
print(list(l))


#lambda :A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression
#syntax:
#lambda arguments : expression
#example 
x = lambda a: a + 10
print(x(5))


l=lambda x,y:x if x>y else y
print(l(35,20))

#reduce :The reduce(fun,seq) function is used to apply a particular function
#  passed in its argument to all of the list elements mentioned in the sequence
#  passed along.This function is defined in “functools” module.
from functools import *
t=[1,2,3,4,5,6,7,8,9]
r=-reduce(lambda x,y:x+y,t)
print(r)




