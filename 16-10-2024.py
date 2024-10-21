# set:set is unordered collection and set contaions no duplicate element.set is mutable.
# set functions
#Add: to add the element to the  set
#update : to update the multiple elements to the set
#clear:removes all the elements from the set
#copy: returns the elments from the set
#pop: removes the random element from the set
#remove: it removes the specific element from the set
#discard : it also removes the specific element from the set

#examples
#empty 
n=set()
print(type(n))
m={4,2,8,1,9,6}
print(type(m))
print("add function")
print(m.add(10))
print("update function")
r={20,40,25,10,6}
m.update(r,range(5))
print(m)
print("copy function")
x=m.copy()
print(x)
print("pop function")
print(m.pop())
print("remove function")
print(m.remove(6))
print(m)
print("discard function")
print(m.discard(20))
print("clear function")
print(m.clear())
print("union function")