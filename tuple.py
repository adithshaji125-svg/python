#1.Create a tuple of five fruits. Check whether "Apple" is present in the tuple. If it is 
#present, print "Apple Found"; otherwise, print "Apple Not Found".

# friuts=( "Apple", "Orange", "Mango", "Banana", "Grapes" )
# n=("Apple")
# if n in friuts:
#     print("Apple Found")
# else:
#     print("Apple Not Found")

#2.Create a tuple of five marks. Print "Pass" if the first mark is greater than or equal to 40; 
#otherwise, print "Fail"

# marks=(40, 50, 60, 70, 80)
# if marks[0] >= 40:
#     print("Pass")
# else:
#     print("Fail")


#3.Create a tuple of five numbers. Add 100 to the tuple by converting it into a list. Print the 
#updated list. 

# numbers=(10, 20, 30, 40, 50)
# num=list(numbers)
# num.append(100)
# print(num)

#4.replace items in a tuple


# n=("Python", "Java", "C++")
# my_tuple=list(n)
# my_tuple[1]="SQL"
# n=tuple(my_tuple)
# print(n)


#5.create two tuples and joint them in a tuple

# a=(1, 2, 3)
# b=(4, 5, 6)
# c=(a+b)
# print(c)


#6.Create a tuple of three names. Print "Same" if the first and last names are the same; 
#otherwise, print "Different"


# n=("Apple", "Banana", "Apple")
# if n[0] == n[2]:
#     print("Same")
# else:
#     print("Different")
 

#7.Create a nested tuple and print the last elemnt

# n=((10,20,30),(40,50,60))
# print(n[1][2])


#8.How do we get the last item of a tuple


# n=(1,3,5,7,9)
# print(n[-1])


#9.How to find the position of a specific value in a tuple


# n=(1,2,3,4,5,6,7,8,9,10)
# print(n.index(6))


#10.convert tuple to list


# a=(10, 20, 30, 40, 50)
# b=list(a)
# print(b)
