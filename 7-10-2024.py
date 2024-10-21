#convert list of strings into a single string without using join function
s=["learning"," ","python"," ","is"," ","very", " ","easy"]
t=""
for i in s:
    t=t+i
print(t)

#1.Python Program to count occurrence of a given characters in string. 

m="learning"
m1=set(m)
for i in m1:
    count=m.count(i)
    print(f"{i} = {count}")

# 2.Python Program to check if two Strings are Anagram. 
s1=input('enter a string1')
s2=input("enter a string2")
if(sorted(s1)==sorted(s2)):
    print("strings are anagrams")
else:
    print("strings are not anagrams")

#3.Python program to check a String is palindrome or not.
s=input("eneter a string")
if(s==s[::-1]):  
      print("The string  is a palindrome")  
else:  
      print("The string is not a palindrome")

#4. Python program to replace the string space with a given character. 
m="learning python is very easy"
print(m.replace(" ","@"))
  

# 5.Python program to replace the string space with a given character using replace() method. 
m="learning python is very easy"
print(m.replace(" ","-"))

#6.Python program to convert lowercase char to uppercase of string. 
n="python"
print(n.upper())

#7.Python program to check given character is digit or not using isdigit() method. 
l="143"
x="python3.12.5"
print(l.isdigit())
print(x.isdigit())


#8. Python program to separate characters in a given string. 
m1="learning"
m2=[i for i in m1]
print(m2)


#9.Python program to remove blank space from string. 
string="Hello world"
print(string.replace(" ",""))

#10.Python program to concatenate two strings using join() method. 
s1="Hi"
s2="Good morning"
s3=' '.join([s1,s2])
print(s3)

#11.Python program to concatenate two strings without using join() method. 
s1="Hi"
s2="Good morning"
s3=s1+s2
print(s3)

#12.Python program to remove repeated character from string. 
l="learning python is very easy"
y=set(l)
print(y)

#13.Python program to count alphabets, digits and special characters. 
string = input("Enter a String : ")
alphabets =0
digits =0
special_characters = 0
for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special_characters = special_characters + 1
print("total no.of alphabets",alphabets)
print("total no of digits",digits)
print("total npo.of special_characters",special_characters)


#14.Python program to check given character is digit or not. 
l1 = input("Enter Your Character : ")
if(l1 >= '0' and l1 <= '9'):
    print("The Given Character ", l1, "is a Digit")
else:
    print("The Given Character ", l1, "is Not a Digit")


#15.Python program to print all non repeating character in string. 
string1=input("enter a string")
for i in string1:
    count=0
    for j in string1:
        if i==j:
            count=count+1
        if count>1:
            break
    if count==1:
         print(i)

#16.Python program to copy one string to another string.  
string1=input("Enter Your a String1 : ")
string2 = ''
for i in range(len(string1)):
    string2 = string2 + string1[i]   
print(string2)

#17.Python program to print the highest frequency character in a String. 

string= input("enter a string")
frequency={}
for i in string:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i] = 1
s1= max(frequency, key = frequency.get)
print(" the highest frequency character in a String: ",s1)

#18.Python program to calculate sum of integers in string.
a=input("enter a string")
sum=0
for i in a:
    sum=sum+int(i)
print(sum)