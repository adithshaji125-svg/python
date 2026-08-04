#1.create a list of numbers from 1 to 20 using list comprehension.

# numbers = [i for i in range(1, 21)]
# print(numbers)


#2.create a list of even numbers between 1 to 50.

# even = [i for i in range(1, 51) if i % 2 == 0]
# print(even)

#3.create a list containing the square of each number from 1 to 10

# square = [i * i for i in range(1, 11)]
# print(square)


#4.numbers=[12,5,18,7,20,3]
 #create a new list containing only numbers greater than 10

# numbers=[12,5,18,7,20,3]
# result=[i  for i in numbers if i > 10]
# print(result)



#5.create a dictionary where the keys are  numbers from 1 to 5 AND values their squares

# d = {i: i * i for i in range(1,6)}
# print(d)


#6.name=['"Anu","Rahul","Diya"]create a dictionay each name is key and length s the value


# names = ["Anu","Rahul","Diya"]
# d = {name: len(name) for name in names}
# print(d)


#7.Create a set of square of numbers from 1 to 10


# squares = {i * i for i in range(1, 11)}
# print(squares)


#8.words=["apple","banana","apple","orange","banana"] create a set containing the first letter of each word

# words = ["apple", "banana", "apple", "orange", "banana"]
# first_letters = {word[0] for word in words}
# print(first_letters)


#9.
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


#10. 
# for i in range(4):
#     for k in range(i+1):
#         print(' ',end='')
#     for j in range(4-i):
#         print('*',end=' ')
#     print()


#11.
# for i in range(1,6):
#     for j in range(6-i):
#         print(' ', end=' ')
#     for k in range(i):
#         print('*', end=' ')
#     print()


#12.
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# #13.
# for i in range(6):
#     for k in range(6-i):
#         print('',end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


#15.
# for i in range(6):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()