# #10-100
# even_count = 0
# odd_count = 0

# for i in range(10, 100):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

#     print(even_count)
#     print(odd_count)




# a=10
# b=5

# c=a
# a=b
# b=c
# print(a)
# print(b)





# a='hello python'
# print(a)
# print(type(a))


# #lower
# b=a.lower()
# print(b)


# #upper
#  

# #swapcase
# d=b.swapcase()
# print(c)


# #title
# d=a.title()
# print(d)     


#capitalize
# d=a.capitalize()






# #count
# a='hello'
# print(a.count('e'))

# #replace
# a='python programming'
# print(a.replace('python','java'))


# #split
# a='python programming'
# print(a.split())
# a='python_prog_ramming'
# print(a.split('_'))


# #strip
# a='         python    '
# print(a.strip())



# #lstrip
# a='      python   '
# print(a.lstrip())


# #rstrip
# a='        python  '
# print(a.rstrip())



# #index
# a='string' #012345
# print(a.index('g'))


#find
# a='string'#012345
# print(a.find('o'))


#string concatination
# a='hello'
# b='world'
# print(a+b)
# print(a,b)

# c=5
# print(a,c)



 #string checking methods
#isalpha
# a=input('enter a string')
# print(a.isalpha())


#isnumeric
# a=input('enter a string')
# print(a.isnumeric())
# print(a.isnumeric()) 



#isalnum
# a=input('enter a string')
# print(a.isalnum())



#istitle
# a=input('enter a string')
# print(a.istitle())


#isupper
#islower


#isspace
  

#string iteration
# a='string'
# for i in a:
#     print(i)


#accessing
# a='string'
# print(a[1])


#slicing
# a='welcome to python'
# print(a[0:7])
# print(a[0:6])
# print(a[2:])





#find the length of string without using len()
# a='string'
# count=0
# for i in a:
#     count+=1
# print(count)


#write a proggram to count the charactersnina string excluding whitespace

# a="python programming"
#print (len(a))
# count=0
# for i in a:
#     if i!="":
#         count+=1
#         print(count)



#List
#li=[]

#append
# li=[1,2,3,4,5]
# print(type(li))
# print(len(li))
# li.append('abc')
# print(li)

# n=input('enter the element')
# if n.isalpha():
#     li.append(n)
# elif n.isnumeric():
#     li.append(int(n))

#     print(li)



#write a progrm to ask the user how many elements they  want in a list,accept those elements from the user,append each element to the list and display the final list

# li=[]
# n=int(input('enter the number='))
# for i in range(n):
#     e=input('enter the element=')
#     li.append(e)
#     print(li)



#insert
 
# li=[1,2,3]
# li.insert(1,5)
# print(li)


# #extend
# li1=[1,2,3]
# li2=[4,5,6]
# li1.extend(li2)
# print(li1)



# #pop
# li1=[1,2,3]P
# li1.pop()
# print(li1)


# #remove
# li1=[1,2,3,4,5]
# li1.remove(3)
# print(li1) 


#count
# li=[1,2,3,2,4,2,5]
# print(li.count(2))



# #index
# li=[1,2,3,2,4,2,5]
# print(li.index(3))



# #reverse
# li=[1,2,3,2,4,2,5]
# li.reverse()
# print(li)


#sort (ascending)
# li=[10,2,3,2,4,2,5,0]
# li.sort()
# print(li)

 #sort (descending)
# li=[10,2,3,2,4,2,5,0]
# li.sort(reverse=True)
# print(li)


#iteration
# li=[10,2,3,2,4,2,5,0]
# for i in li:
#     print(i)


#acccessing
# li=[10,2,3,2,0,4,2,5,]#forward:0123,back: -,-2,1
# print(li[5])
# print(li[-3])




#slicing
# li=[10,2,3,2,0,4,2,1,2]
# print(li[0:6])
# print(li[0:])
# print(li[::-1])



#create a list with at leaset 3 items.Display the following using if elif else
#menu 1.add 2.delete 3.update 4.exit

# items=["leo","messi","suii"]
# print(items)
# print("choices\n1.add\n2.delete\n3.update\n4.exit")
# choice=int(input("Enter your choice:"))
# if choice==1:
#     print("Add elements:")
#     additems=input("Enter item to add:")
#     items.append(additems)
#     print(items)
# elif choice==2:
#      print("Delete elements:")
#      delitems=input("Enter item to delete:")
#      items.remove(delitems)
#      print(items)
# elif choice==3:
#      print("Update elements:")
#      olditems=input("Enter item to be updated:")
#      newitems=input("Enter new item:")
#      b=items.index(olditems)
#      items[b]=newitems
#      print(items)
# elif choice==4:
#      print("exit")
# else:
#      print("invalid choice")



# li[1,2,3,4,5,6]
# c=[]
# a=len(li)-1
# for i in range(a,-1,-1):
#     c.append(li[i])
#     print(c)



#Tupple Example
#immutable
#ordered
#()
# t=('a', 'b', 1, 2.2, 2,2)
# print(t)
# print(type(t))


# #len
# print(len(t))


# #count()
# print(t.count(2))


# #index()
# print(t.index(1))


# print('hello')
# for i in range(1,10):
#     print('hello')


#     #tupple iteration

#     for i in t:
#            print(i)


#Element Accessing
# print(t[1])#forward
# print(t[-1])#backward


#slicing
# t=[1,2,3,4,6,7,8,9,10]
# print(t[0:3])
# a=[1,2,3,4,6,7,8,9,10]
# print(a[4:7])
# print(t[::2])


# #Tuple reversing
# print(t[::2])


#Another method:
#Tuple concatenation

# t1=(1, 2, 3, 4, 5)
# t2=(6,)
# type(t2) #we can use a comma because only tuple can be concatenated with tuple
# t3 = t1 + t2
# print(t3)


# t1 = (91, 2, 3, 4, 5)
# t2 = ('adith', 900)

# t3 = t1 + t2
# print(t3)
 

#Dictionary Example
#key-value pair
#mutable
#ordered

# person = {
#     'name': 'adith',
#     'phone': 956227,
#     'email': 'adith@gmail.com'
# }

# print(person)
# print(type(person))

# #keys()-used to access all key in a dictionary.
# print(person.keys())

# #values()-used to access all values in a dictionary.
# print(person.values())

# #get()-Returns the value of a specific key.

# key = input("Enter the key: ")
# print(person.get(key))

# #print(person.get('name))

# #pop()-Removes an element using the specified key.

# person.pop('phone')
# print(person)

# #popitem()-Removes the last key-value pair.

# person.popitem()
# print(person)

# #Update()-used to add a new key-value pair
# #or update the value of an existing key.

# person.update({'age':23})
# print(person)




# #Set example
# set({})
# #unordered
# #duplicate
# s=set({}) # empty set

# s = {'a', 'b', 'c', 'a', 'b'}
# print(s)
# print(type(s))
# print(len(s))


# #add

# s.add('d')
# print(s)


# #discard() / remove()

# s.discard('a')
# print(s)


# s.remove('b')
# print(s)


# s.pop()
# print(s)


#symmetric_difference_update()

# x = {'a', 'b', 'c', 'd'}
# y = {'a', 'b', 'e', 'f'}

# x.symmetric_difference_update(y)
# print(x)


#intersection_update()

# x1 = {'a', 'b', 'c', 'd'}
# y1 = {'a', 'b', 'e', 'f'}

# x1.intersection_update(y1)
# print(x1)