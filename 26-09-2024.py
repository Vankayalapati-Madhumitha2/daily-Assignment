# 1.Write a program that prints the numbers from 1 to 100. 
#For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". 
#For numbers which are multiples of both three and five, print "FizzBuzz".

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
# 2.Write a program that checks if a number is prime. A prime number is a number 
# greater than 1 that is only divisible by 1 and itself.
n= int(input("enter a number"))
flag = 0
if n== 0 or n== 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if (n% i) == 0:
            flag = 1
            break
    if flag:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")
#  3.Write a program to check if a string is a palindrome. A palindrome is a word, phrase, or sequence 
# that reads the same forward and backward.
s=input("eneter a string")
if(s==s[::-1]):  
      print("The string  is a palindrome")  
else:  
      print("The string is not a palindrome")  
# 4.Write a program that generates a random number between 1 and 100, and asks the user to guess it. The program should give hints
# ("too high" or "too low") until the user guesses correctly.
guess_number=int(input("enter a guess number"))
guesses=-1
while guesses !=guess_number:
    guesses=int(input("guess the number"))
    if guesses<guess_number:
        print("too low! try again")
    elif guesses>guess_number:
        print("too high! try again")
    else:
        print("congratulations you guessed the number")
# 5.Write a program that takes a number as input and prints the sum of its digits.
s=input("enter a string")
sum=0
for i in s:
    sum=sum+int(i)
print(sum)
 
# 6.Write a program to calculate the factorial of a number using a for loop.
n=int(input("enter a number"))
factorial = 1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of",n,"is",factorial)
# 7.Write a program to find the largest of three numbers using if statements.
a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))
if a>b and a>c:
    print("a is large")
elif b>c:
    print("b is large")
else:
    print("c is large")
# 8.Write a program to check if a number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits
#  raised to the power of the number of digits.
t=int(input("enter a number"))
sum=0
temp=t
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp//10
 
if sum==t:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
#9.Write a program that prints the multiplication table for a given number.
# Multiplication table (from 1 to 10) in Python
 
num = int(input("enter a number"))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
#10.Write a program that counts the number of even and odd numbers in a list.
p=[12,24,35,46,51,6,7,8,9,10]
even_count=0
odd_count=0
for i in p:
    if i%2==0:
        even_count=even_count+1
   
    else:
        odd_count=odd_count+1
print(even_count)
print(odd_count)
 
 
     
 