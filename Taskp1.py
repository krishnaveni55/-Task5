#1.To calculate the total number of vowels and count od each individual vowel#
count=0
a="Guvi Greeks Network Private Limited"
for i in a:
    if(i=='a'):
       count=count+1
       print (count,"a")
    elif (i=="e"):
          count=count+1
          print (count,"e")
    elif (i=='i'):
          count=count+1
          print(count,"i")
    elif (i=='o'):
          count=count+1
          print(count,"o")
    elif (i=='u'):
          count=count+1
          print(count,"u")
print(count)

#2.program to write pyramid of number from 1 to 20#
k=20
for i in range(1,k+1):
  print(" "*(k-i),end="")
  for j in range(1,i+1):
    print(j,end=" ")
  print()

#3.program to take a string and return a new string with all the vowel removed#
string=input("enter  a string:")
vowels=['a','e','i','o','u']
result=" "
for character in string.lower():
    if character not in vowels:
        result += character
print(result)

#4.program that takes the string and return the unique character in it #
strs = input("Enter a sentence : ")
Lt = []
for i in strs:
    if i not in Lt:
        Lt.append(i)
print("no of letters",len(Lt)-1)

#5.program that takes the a string and return true if it is a palindrome or falsde otherwise #
strs = input("Enter a sentence : ")
print(strs)
print(strs[: : -1])
if strs == strs[: : -1]:
    print("True")
else:
    print("False")

#6.program that takes 2 string and retrun the longest common substring between them#

#7.program that takes a string and return most frequent character in it#
def most_frequent_character(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_count = 0
    most_frequent_char = None
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_frequent_char = char
    
    return most_frequent_char
string = "butter bitter better"
result = most_frequent_character(string)
print("The most frequent character is:", result)

#8.program that takes astring amd return ture if it is an anagram of other string false otherwise#

strs_1 = input("Enter a sentence : ")
strs_2 = input("Enter a sentence : ")
if set(strs_1) == set(strs_2):
    print("True")
else:
    print("False")

#9.program that takes a string and return the number of word in it#

s="hi welcome to python class"
count=0
for i in s.split(" "):
    print(i)
    count+= 1
print("The total number of words are :",count)






            

