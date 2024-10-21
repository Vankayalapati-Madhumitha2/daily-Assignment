# conditional statements:
# if : statements execute if the condition is true
# if else : if condition is true the statements after if block will execute otherwise else block will execute
# if elif else : it checks the multiple conditions


# to print all the even number elements in the list
a=[10,30,45,63,29,40,56,78]
for i in a:
    if i%2==0:
        print(i)
print("--------------------------------------")
#to find the squares of elements in the list
m=[1,2,3,4,5,6,7,8]
for i in m:
    print(i*i)
print("--------------------------------------")
# if else condition
n=int(input("enter a value"))
if n%8==0:
    print("number is divisible by 8")
else:
    print("number is not divisible by 8")

print("--------------------------------------")
# s="learning python is very easy " print only wherever we have a in a word using join function
s="learning python is very easy"
l=[]
for i in s:
    if i=="a":
        l.append(i)
print(''.join(l))
print("--------------------------------------")
# s="learning python is very easy " print only wherever we have a in a word using join function
s="learning python is very easy"
l=[]
for i in s:
    if i=="a":
        print(i)