#s = "learning python is very easy"
#output = "ysae yrev si nohtyp gninrael"
#output = "easy very is python learning"
s="learning python is very easy"
print(s[::-1])
s1=' '.join(s.split()[::-1])
print(s1)


#s = "learning python is very easy"
#output = "learningpythonisveryeasy"

s2="learning python is very easy"
s3=s2.replace(" ","")
print(s3)

#s1 = "learning"
#output = l = 1
      #  e = 1
       # a = 1
       # r = 1
       # n = 2
       # i = 1
       # g = 1"""
m="learning"
m1=set(m)
for i in m1:
    count=m.count(i)
    print(f"{i} = {count}")

# second logic
S = "learning"
count_value = {}
 
# Count occurrences of each character
for char in S:
    if char in count_value:
        count_value[char] += 1
    else:
        count_value[char] = 1
 
# Print the counts
for char, count in count_value.items():
    print(f"{char} = {count}")