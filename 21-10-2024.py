#Functions 
#A function in Python is a block of code that performs a specific task
#  and can be called multiple times from anywhere in a program
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#Example:
def my_function():
  print("Hello")
my_function()

#adding two numbers using functions
def addnum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum = a + b
    print("The sum of ",a,"and ",b,"is ",sum)
addnum()

#example 2
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Madhumitha", "Vankayalapati")

#return statement :
#A return statement is used to end the execution of the function call and “returns” the result.
# The statements after the return statements are not executed.


#Write a Python program to create a dictionary from a string.  
# Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares' using functions
def char_count(string):
    l=len(string)
    count={}
    for i in string:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
string='skywavessoftwares'
print(char_count(string))


#Write a python program to unpack atuple into several variables  using functions
def print_employee_name(name):
    print(f"Employee Name: {name}")
def print_age(employee_age):
    print(f"Age: {employee_age}")
def print_company_name(company):
    print(f"Company Name: {company}")
a = ("Madhumitha", 24, "skywaves")
employee_name, age, company_name = a
print_employee_name(employee_name)
print_age(age)
print_company_name(company_name)
