#list programas 
#1. Write a python program to merge two list?
a=[1,2,3,4,5,6]
b=[7,8,9]
c=a+b
print(c)

# 2.Write a python program to delete element of given index in list ?

m=[10,20,50,60,70]
m.pop(3)
print(m)


# 3.Write a pytho program to delete given element from the list?
m=[10,20,50,60,70]
m.remove(20)
print(m)


# 4.Write a python programe to check if the two list are having atleast one common element?
l1=[1,2,4,5,6,7]
l2=[2,3,4,60,70]
l3=0
for i in l2:
    for i in l1:
        l3=1
if l3==1:
    print("common elements are there")
else:
    print("there is no common elements")


# 5.Write a python program to remove  specified column from the nestedlist?
l1=[[1,2,3,4],[5,6,7,8],[9,10,11]]
for i in l1:
    del i[1]
print(l1)

# 6. Write python program to convert a list of integers into single integer ?

l1=[10,20,30]
for i in l1:
    print(i,end="")

# 7.Write  a python programe to remove duplicates from the list ?
a=[10,20,30,10,40,30,10]
b=set(a)
print(list(b))

# tuple programs
#1. How do you create a empty tuple on python ?
a=(10,)
print(type(a))
print(a)

#2.Write a python program to unpack atuple into several variables ?
a=("Madhumitha",24,"skywaves")
employee_name,age,company_name=a
print(employee_name)
print(age)
print(company_name)

#3.write a python program to add an item to the tuple ?
a=(1,2,3,4,5)
a=a+(7,)
print(a)

# 4.Write a python proram to convert tuple into a string ?
a=('p','y','t','h','o','n')
b=''.join(a)
print(b)

#5.Write a python program to find most frequent element in tuple ?

t1 = (67, 7, 8, 67, 7, 10)
count=0
t2=t1[0]
for i in t1:
    t3=t1.count(i)
    if(t3>count):
        count=t3
        t2=i
print(t2)


# set programs
#1.Write a program to create a set.
#empty set
s1=set()
print(type(s1))
s2={10,20,30}
print(type(s2))
print(s2)

#2.Write program to iterate over sets.
s1=set("madhumitha")
for i in s1:
    print(i)

#3.Write a Python program to add member to a set.
s1={20,30,40,10}
s1.add(50)
print(s1)

#4.Write a Python program to remove item from a given set.

s1={20,30,40,10}
s1.remove(20)
print(s1)

#5.Write a python program to create a intersection of set ?
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(m.intersection(r))
print(m&r)

#6.Write a python program to createa unionof set ?
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(m.union(r))
print(m|r)

#7.Write a python program to create set differance ?
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(m.difference(r))
print(m-r)

#8.Write a python program to create a symmetric defferance ?
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(m.symmetric_difference(r))
print(m^r)

#9.write a python program to find max and min values in a set?
m={4,2,8,1,9,6}
s1=list(m)
print(max(s1))
print(min(s1))

#10. Given two Python sets, write a Python program to update the first set with items 
# that exist only in the first set and not in the second set.
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(m-r)

#11.Write a Python program to remove items 10, 20, 30 from the following set at once.?
S1={10, 20, 30, 40, 50, 60}
S2={10,20,30}
S1.difference_update(S2)
print(S1)

#12.Check if two sets have any elements in common. If yes, display the common elements?
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(m&r)

#13.Update set1 by adding items from set2, except common items?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result=set2.difference(set1)
set1.update(result)
print(set1)

#14. Remove items from set1 that are not common to both set1 and set2?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)


# dictionary programs

#1. Write a python program to  add a key to a dictionary ?
d1={"name":"madhumitha","age":24,"company_name":"skywaves"}
key="salary"
value=23000
d1[key]=value
print(d1)

#2.Write a python program to check weather the given value is present in the dictionary or not ?
d1={"name":"madhumitha","age":24,"company_name":"skywaves"}
value='madhumitha'
if value in d1.values():
    print(f"The value '{value}' is present in the dictionary.")

else:
    print(f"The value '{value}' is  not present in the dictionary.")

#3.Write a Python script to print a dictionary where the keys are numbers between
#  1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 
 #8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d1=dict()
for i in range(1,16):
    d1[i] = i ** 2
print(d1)

# 4.Write a python program to create a dictionary from the string ?
string = "name: madhumitha, age: 24, company: skywaves"
d2= {}
pairs = string.split(',')
for pair in pairs:
    key, value = pair.split(':')
    d2[key.strip()] = value.strip()
print(d2)

# Write a python program to combine two dictionaries by adding values of common keys ?
dict1 = {'a': 12, 'b': 25, 'f': 9}
dict2 = {'d': 100, 'e': 200, 'f': 300}
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)

#6.Write a python program to merge two python dictionaries ?

d1 = {'a': 12, 'b': 25, 'f': 9}
d2 = {'d': 100, 'e': 200, 'c': 300}
d3=d1|d2
print(d3)

#7.Write a Python program to create a dictionary from a string.  
# Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
string='skywavessoftwares'
count={}
for i in string:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)