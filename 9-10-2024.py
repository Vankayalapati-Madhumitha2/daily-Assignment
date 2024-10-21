# List : It is used to store multiple variables in a single variable.List is mutable.
# Mutable: Mutable means we can modify the data
# List operations:
# Manipulating elements: 
# Append: to add element at the last position
# insert: to insert element at the specific index
# extend: to add elements from one list to another list
# remove: to remove specific element from the list
# pop: it returns the last element from the list
# ordering elements:
# reverse: to reverse the string
# sort : order the elements from ascending order to descending order
# len : it returns the length of the list
# index : it returns the index of elements
# min: it returns the minimum valkue from the list
# max : it returns the maximum value from the list
# mathematical operations :
# concatentation: two add two strings
# repetitrion : it repets the string
# comparing operator : compare two lists
#Example for list operations:
a=[1,2,3,4,5,6,7,8]
print(type(a))
print(a[0])
print(a[-1])
a[5]=60
print(a)
print("----------------------------")
for i in a:
    print(i)
print("------------------")
i=0
while i<len(a):
    print(a[i])
    i=i+1
print("append function")
a.append(70)
print(a)
print("insert function")
a.insert(0,90)
print(a)
print("extend function")
b=[30,40,50]
a.extend(b)
print(b)
print("remove function")
a.remove(8)
print("pop function")
print(a.pop())
print("reverse function")
a.reverse()
print(a)
print("sort function")
print(a.sort())
print(a)
print("concatenation function")
c=a+b
print(c)
print("repetition function")
d=a*3
print(d)
print("clear function")
print(a.clear())
print("list comprehension")
s=[x for x in range(1,11)]
print(s)
