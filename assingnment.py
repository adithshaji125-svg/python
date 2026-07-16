#1.find the length of a string
# a='string'
# count=0
# for i in a:
#     count+=1
#     print(count)


#2.print each character on a new line
# string=input('enter a string:')
# for i in string:
#     print(i)

#3.concatenate two string without using +operator
# a=input("Enter first string:")
# b= input("Enter second string:")
# c="".join([a, b])
# print(c)


#4.Reverse a string
# a=input("Enter a string:")
# print(a[::-1])



#5.covert a string to uppercase
# a=input("enter a string:")
# c=a.upper()
# print(c)



#6.convert a string to lowercase
# a=input("enter a string:")
# c=a.lower()
# print(c)

   

#7.check if a string contains only digits
# a=input("Enter a string:")
# c=a.isnumeric()
# print(c)



#8.count the number of spaces in a string
# a=input("Enter a String:")
# print(a.count(" "))




#9.remove all spaces from string
# a=input("Enter a string:")
# c=a.replace(" ","")
# print(c)

#10.replace all occurences of a given character string
# a=input("Enter a string:")
# b=input("Enter the character to replace:")
# c=input("Enter the new character:")
# print(a.replace(b,c))


#11.count the numbers of vowels in a string
# a=input("Enter a string:")
# count=0
# for i in a:
#     if i in "aeiou":
#         count+=1
# print(count)


#12.count the n.of upper and lowercae letters in a string
# a=input("Enter a string:")
# upper=0
# lower=0
# for i in a:
#     if i.isupper():
#         upper=upper + 1
#     elif i.islower():
#         lower =lower + 1
# print(upper)
# print(lower)


#15.check if a string start with vowel
# s = input("Enter a string: ")
# if s[0] in "aeiou":
#     print("Start with a vowel")
# else:
#     print("Not start with a vowel")


#16.check if string is palindrome
# a=input("Enter a string:")
# if a==a[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#17.count the n.of words in a string(words separated by spaces)
# a= input("Enter a string: ")
# count=1
# for i in a:
#     if i==" ":
#         count+=1
# print("Number of words:",count)