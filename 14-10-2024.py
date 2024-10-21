#some list questions on basic list operations and adding elements
# 1.Basic List Operations:
#1.Write a Python program to create a list of 5 integers and print the sum of all elements in the list.
a=[1,2,3,4,5]
sum=0
for i in a:
    sum=sum+i
print(sum)

#2.Create a list of strings containing the names of 5 fruits. Access and print the second 
# and fourth elements using indexing.
a=["mango","grapees","apple","pineapple","grapes"]
print("second and fourth elements are:",a[2],a[4])

#3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers,
#  and every second number in the list.
a=[1,2,3,4,5,6,7,8,9,10]
print("to print the first three numbers",a[:3])
print("to print the last three numbers",a[-3:])
print("every second number in the list.",a[::2])

#2. Adding and Removing Elements:
#1.Write a Python program that initializes a list with some numbers and:
l=[1,2,3,4,5,6,7,8]
#.2.Adds a new number to the list using the append() method.
l.append(5)
print(l)
#3.Inserts a number at the second position using insert().
l.insert(0,40)
print(l)
#4.Extends the list with another list of numbers.
m=[30,40,50]
l.extend(m)
print(l)
#5.Remove all occurrences of the number 3 from a list of integers.
t=[]
for i in l:
    if i!=3:
        t.append(i)
print(t)
#6.Write a Python program to remove the last element of a list using pop() and print the updated list.
l.pop()
print(l)
#Sorting and Reversing Lists:
#1.Write a Python program to sort a list of 10 random integers in 
# ascending and descending order using sort() and reverse
s1=[50,29,40,78,21,35,60]
s1.sort()
print(s1)
s1.reverse()
print(s1)
#2.Create a list of strings and reverse the order of elements using
#  both reverse() and slicing [::-1]. Compare the results.
a=["madhu","gopi","sai","ram"]
c=a.copy()# with out changing the original list
c.reverse()
b=a[::-1]
print(c)
print(b)
print("both produces the same results")

#Aliasing and Cloning:
#1.Create a list of numbers. Assign the list to another variable and modify the original list. 
# Check if the second list also changes. Then, create a copy of the original list and show that 
# modifying the copy does not affect the original list.
l1=[10,20,30,40]
l2=l1
l1.append(50)
print(l1)
print(l2)
l3=list(l1)
l3.remove(20)
print(l3)
