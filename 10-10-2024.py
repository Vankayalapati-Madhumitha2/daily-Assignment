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

#2.Write a Python program to demonstrate how changes in a list's alias affect both lists,
#  while changes in a cloned list do not.
l1=[10,20,30,40]
l2=l1
l3=l1.copy()
l2.append(4)
l3.append(5)
print(l2)
print(l3)

#5. Mathematical Operations:
#1.Create two lists of numbers, and use the + operator to concatenate them. 
#Then, use the * operator to repeat the elements of one list 3 times.
s1=[1,2,3,4,5,6,7]
s2=[40,50,60,76]
print(s1+s2)
print(s1*3)
#2.Given a list of numbers, write a Python program to create a new list where each element is doubled 
# (i.e., each element is multiplied by 2).
numbers=[2,3,4,5,6,7]
l=[i*2 for i in numbers]
print(l)
#6. Membership Operators:
#1.Write a Python program to check if a specific element (e.g., 5)
#  exists in a given list using the in operator. If it exists, 
# print its position; otherwise, print "Element not found."
#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.
a=["john","sara","madhu","gopi"]
list_numbers=[1,2,3,4,]
exist_element=2
if exist_element in list_numbers:
    position=list_numbers.index(exist_element)
    print("element",exist_element ,"found at",position)
else:
    print("element not found")
names=["john","sara"]
for i in names:
    if i in a:
        position=a.index(i)
        print(i,"found at position:",position)
    else:
        print("element not found")

#7. Nested Lists:
#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix.
#  Then, access and print the element at row 2, column 3.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    print(i)
s=matrix[1][2]
print("element at row 2 and column 3:",s)

#2.Create a nested list representing a list of students' names and their respective grades. 
# Write a Python program to print each student's name along with their grade.
students=[["madhu",96],["gopi",97],["sai",67]]
for i in students:
    name,grade=i
    print("name:",name,"grade:",grade)

#8. Advanced Challenges:
#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers.
n=list(range(1,21))
even_numbers=[i for i in n if i%2==0]
odd_numbers=[i for i in n if i%2!=0]
print(n)
print(even_numbers)
print(odd_numbers)

#2.Write a Python program that reads a list of integers and returns 
# a new list containing only the unique elements (i.e., removing duplicates).
#Given a list of tuples representing (name, age), sort the list by age in ascending order
a=[1,2,2,3,4,5,6,6,7,6,8,9,6]
unique_elements=set(a)
students=[("madhu",23),("gopi",24),("sai",25),("sri",12)]
s1=sorted(students,key=lambda i:i[1])
print(unique_elements)
print(s1)