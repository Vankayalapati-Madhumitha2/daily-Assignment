# control statements:list of statements executed sequentially we 
# can execute certain block conditionally or repeaatedlybis known as control flow statements
#while loop: it is used to repeatedly execute a block of statements
# for loop: for loop is used to iterate a sequence of items
#transfer statements:
#break: to exit out of the loop the statements after break can not execute
#continue: jumps the current itteration to the begin of the loop
#pass: we don't have any statements we can use pass keyword or we don't adda ny methods or functions we can 
#use pass


#print("break")
for i in range(1,15):
    if i==10:
        break
    print(i)
print("----------------------")
#continue 
for i in range(1,10):
    if i==6:
        continue
    print(i)
# guess number by using while loop and if :
a=int(input("enter a number"))
guess=-1
while guess!=a:
    guess=int(input("enter a guess number"))
    if guess<a:
        print("too low try again")
    elif guess>a:
        print("too high try  again")
    else:
        print("congratualatiopns we have guessed the correct guess number")
    
# guess number by using for loop and if :
t=int(input("enter a number"))
attempts=int(input("enter a number of attempts"))
for i in range(1,attempts+1):
    guess=int(input("enter a guess number"))
    if guess<t:
        print("too low try again")
    elif guess>t:
        print("too high try  again")
    else:
        print("congratualatiopns we have guessed the correct guess number")
else:
    print("sorry no.of attempts are completed")