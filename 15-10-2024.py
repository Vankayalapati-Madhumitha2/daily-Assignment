#tuple:to store mutiple values in a single varaiable. list is immutable.
#immutable: we cannnot modify the data
#Len: to return the length of elements from the tuple
#count: to return the number of occurance of the given element
#max:it returns the largest element from the tuple
#min:it returns the smallest element from the tuple
#sorted:to sort the elements that is asscending order from the tuple

#examples
l=(100,200,300,400,800,600,700,960,340)
print(type(l))
print("len function")
print(len(l))
print("count function")
print(l.count(400))
print("index function")
print(l.index(300))
print("max function")
print(max(l))
print("min function")
print(min(l))
print("sorted function")
l1=sorted(l)
print(l1)
