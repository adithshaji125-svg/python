#1.print numbers from 50 to 1 in reverse order.

# for i in range(50,0,-1):
#     print(i)


#2.print all even numbers from 1 to 100.

# for i in range(2,101,2):
#     print(i)


#3.print all odd numbers from 1 to 100

# for i in range(1,101,2):
#     print(i)


#4.print all numbers btw 1 and 100 that are divisible by 7.

# for i in range(1,101):
#     if i%7 == 0:
#         print(i)


#6.sum of first natural numbers

# n = int(input("Enter N: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)


#7.product first N natural numbers

# n = int(input("Enter N: "))
# product = 1
# for i in range(1, n + 1):
#     product *= i
# print(product)

#8.count how many number from 1 to 100 are divisible by 3.

# count=0
# for i in range(1,101):
#     if i%3 == 0:
#         count += 1
# print('count=',count)


#9.find the sum  of all even numbers btw 1 to 100


# total = 0
# for i  in range(2,101,2):
#     total += i
# print('Sum=',total)

#10.count how many uppercase and lowercase numbers

# n = input("Enter string: ")
# upper = 0
# lower = 0
# for ch in n:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# print("Uppercase:", upper)
# print("Lowercase:", lower)


# 12. Second largest number without sort() or max()

# lst = [10, 50, 20, 40, 30]
# largest = second = lst[0]
# for num in lst:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num
# print(second)

# 13. Count numbers divisible by both 3 and 5
# n=(10, 15, 30, 22, 45, 60)
# count = 0
# for num in n:
#     if num % 3 == 0 and num % 5 ==0 :
#         count += 1
# print("Count =", count)


# 14. Count numbers divisible by both 3 and 5 in a tuple

# t = (15, 30, 45, 10, 9, 60)
# count = 0
# for i in t:
#     if i % 3 == 0 and i % 5 == 0:
#         count += 1
# print(count)



# 15. Student with highest mark

# students = {"Arjun": 80, "Adith": 95, "Arun": 88}
# highest = ""
# mark = 0
# for name in students:
#     if students[name] > mark:
#         mark = students[name]
#         highest = name
# print(highest)



# 16. Increase salary by 10% if less than 50000 print updated dict

# emp = {"A": 40000, "B": 60000, "C": 45000}
# for i in emp:
#     if emp[i] < 50000:
#         emp[i] = emp[i] * 1.10
# print(emp)


# 17. Elements in first set but not second

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1 - set2)


# 18. Perfect squares from 1 to 20

# s = set(range(1, 21))
# for i in s:
#     if i == int(i * 0.5) * 2:
#         print(i)


# 19. Separate even and odd numbers

# lst = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even:", even)
# print("Odd:", odd)




# 20. Word with highest frequency

# words = {"apple": 5, "banana": 2, "orange": 8}
# highest = ""
# freq = 0
# for w in words:
#     if words[w] > freq:
#         freq = words[w]
#         highest = w
# print(highest)


# 21. t1=(1,2,3,4,10)
# t2=(4,5,6,4,3)
# a=len(t1)
# for i in range(a):
#     if t1[i]>t2[i]:
#         print('t1 is largest')
#     elif t1[i]<t2[i]:
#         print('t2 is largest')
#     else:
#         print('equal')