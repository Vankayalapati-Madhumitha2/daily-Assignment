#Strings: strings are collection of alphabets ,and words .
# strings are represented by double quotations””.
#Some important functions in string:
#1. Slicing: it used to slice the string .that means fetching a substring
#2. Count: it returns the occurance of specific character
# 3.Split: it is used to split the string
4#. Join: it is used to join the string
#5. Strip: it is used to remove the white spaces in a string
#6. Lstrip : lstrip function removes the leading whitespaces on the left
#7. Rstrip : rstrip removes the tariling whitespaces on the right
#8. Upper :returns the upper case letters.
#9. Lower: returns the lower case letters
#10. Title: returns the capital letter of each word
#11. Swapcase: returns if the string contains uppercase letters it turns in to lowercase and lowercase letters turns into
#uppercase letters.

#examples:
x= input("Enter a word or sentence: ")
print("uppercase - ", x.upper())
print("lowercase - ", x.lower())
print("title - ", x.title())
print("count - ", x.count("p"))
print("split - ", x.split())
print(type(x))
print(len(x))
print(x[10:5])