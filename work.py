# num = int(input("Enter a number:"))  # 1.Display Hello
# if num == 10:
#     print("Hello")
# else:
#     print("Number is not 10")


# num = int(input("Enter a number: "))    # 2.Number is positive
# if num > 0:
#     print("Positive")
# else:
#     print("Not Positive")



# num = int(input("Enter a number: "))      # 3.Number is between 1 to 10
# if 1 <= num <= 10:
#     print("Between 1 and 10")
# else:
#     print("Not Between 1 and 10")



# char = input("Enter a character: ")         # 4.character is vowels or not

# if char in "aeiou":
#     print("Character is a vowel")
# else:
#     print("Character is not a vowel")


# a = int(input("Enter first number: "))        #5.Find largest Number
# b = int(input("Enter second number: "))
# if a > b:
#     print("Largest =", a)
# else:
#     print("Largest =", b)



# num1=int(input("Enter first number:"))          #6.Find the smallest number
# num2=int(input("Enter second number:"))
# if (num1<num2):
#   print("number1 is smaller than num2")
# elif (num2<num1):
#   print("number2 is smaller than num1")


# age=int(input("Enter age:"))                      #7.whether a person is eligible for voting
# if age>= 18:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting!")     



# num=int(input("Enter a number:"))                #8.Given number is odd or even
# if num % 2==0:
#     print("Given number is even")
# else:
#      print("Given number is odd")



# num=int(input("Enter a number:"))                  #9.check the num divisible by 3
# if num % 3==0:
#     print("Divisible by 3")
# else:
#      print("Not divisible by 3")


# num=int(input("Enter a number:"))                   #10.check the number is divisible by 2 and 3
# if num % 2==0 and num % 3==0:
#     print("Divisible by both 2 and 3")
# else:
#      print("Not divisible by 2 and 3")


# num = int(input("Enter a number: "))                 #11.check the number positive or negative

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")



# mark=int(input("Enter your mark:"))                    #12.display grade
# if mark>=81 and mark<=100:
#     print("Grade=A+")
# elif mark>=71 and mark<=80:
#     print("Grade=A")
# elif mark>=61 and mark<=70:
#     print("Grade=B+")
# elif mark>=51 and mark<=60:
#     print("Grade=B")
# elif mark>=41 and mark<=50:
#     print("Grade=C")
# elif mark>=31 and mark<=40:
#     print("Grade=D")
# else:
#     print("Failed")



# a = int(input("Enter first number: "))                   #13.Largest of three numbers
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a > c:
#     print(a, "is the largest number")
# elif b > a and b > c:
#     print(b, "is the largest number")
# else:
#     print(c, "is the largest number")



# a = int(input("Enter the age of first person: "))           #14.Display youngest age of 4 peoples
# b = int(input("Enter the age of second person: "))
# c = int(input("Enter the age of third person: "))
# d = int(input("Enter the age of fourth person: "))

# youngest = min(a, b, c, d)

# print("Youngest age is", youngest)
# print("Minimum age is", youngest)



# cost=int(input("Enter the cost of bike:"))                   #15.Calculate bike road tax
# if cost>100000:
#     print("Tax=15%")
# elif cost>50000 and cost<=100000:
#     print("Tax=10%")
# else:
#     print("Tax=5%")



# salary=float(input("Enter salary:"))                          #16.Calculate employee bonus
# service=int(input("Enter years of services:"))
# if service > 10:
#     bonus = salary * 10 / 100
#     print("bonus= ", bonus)
# elif service >=6 and service <= 10:
#      bonus = salary * 8 / 100
#      print("bonus=", bonus)
# else:
#      bonus = salary * 5 / 100
#      print("bonus=", bonus)



# num=int(input("enter a number="))                              #17.Display hello the num is multiple of 5 otherwise Bye
# if num %5 == 0:
#     print("Hello")
# else:
#     print("Bye")



# num=int(input("Enter a number="))                                #18.Check last digit of number is divisible by 3
# last_digit = num % 10
# if last_digit % 3 == 0:
#    print("Last digit is divisible by 3")
# else:
#    print("Last digit is not divisible by 3")



# a = int(input("Enter first number: "))                             #19.Accept two numbers and an operator
# b = int(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")

# if operator == "+":
#     print(a + b)
# elif operator == "-":
#     print(a - b)
# elif operator == "*":
#     print(a * b)
# elif operator == "/":
#     print(a / b)
# else:
#     print("Invalid operator")


# age=int(input("Enter age="))                                       #20.calculating wage
# gender=(input("Enter gender(male/female)="))
# wday=int(input("Enter the no.of working days="))
# if age>=18 and age<=29:
#     if gender == "male":
#         wage = 700 * wday
#         print("Total wage is= " ,wage)
#     elif gender == "female":
#         wage = 750 * wday
#         print("Total wage is=" , wage)
# elif age>=30 and age<=40:
#     if gender == "male":
#         wage = 800 * wday
#         print("Total wage is=" , wage)
#     elif gender == "female":
#         wage = 850 * wday
#         print("Total wage=",wage)
# else:
#        print("Not applicable")



# age=int(input("Enter age="))                                        #21.calaculate wages using nested if
# gender=(input("Enter gender(male/female)="))
# wday=int(input("Enter the no.of working days="))
# if age>=18 and age<=29:
#     if gender == "male":
#         wage = 700 * wday
#         print("Total wage is=" ,wage)
#     elif gender == "female":
#         wage = 750 * wday
#         print("Total wage is=", wage)
# elif age>=30 and age<=40:
#     if gender == "male":
#         wage = 800 * wday
#         print("Total wage is=", wage)
#     elif gender == "female":
#         wage = 850 * wday
#         print("Total wage=",wage)
# else:
#      print("Enter age between 18 and 40")




# age=int(input("Enter age="))                                            #22.place of employee service using nested if
# gender=(input("Enter gender(male/female)="))
# status=(input("Enter status(married/unmarried)="))
# if age>=20 and age<=39:
#  if gender == "male":
#     print("Employee works anywhere")
# elif age>=40 and age<=60:
#     print("Employee works in urban area")
# elif gender== "female":
#     print("Employee works in urban area")
# else:
#     print("Error")