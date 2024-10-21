#union:combine two sets
#intersection:returns the element opresent in both sets
#difference: returnbs the elements  present in one set not in two sets
#symmetric difference : returns the elements present in either set1 or set2 not in both sets
#examples
m={4,2,8,1,9,6}
r={20,40,25,10,6}
print(type(m))
print("union function")
print(m.union(r))
print(m|r)
print("intersection function")
print(m.intersection(r))
print(m&r)
print("difference function")
print(m.difference(r))
print(m-r)
print("symmetric difference function")
print(m.symmetric_difference(r))
print(m^r)
print("set comprehension")
t={v*v for v in range(5)}
print(t)
