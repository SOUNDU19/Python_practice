# name = "Soundarya"
# Age = 22
# city = "Bengaluru"
# College = "EWIT"
# print("Name:",name)
# print("Age:",Age)
# print("City:",city)
# print("College:",College)
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# sum = num1 + num2
# print("sum",sum)
# # finding squares and cubes
# num3 = int(input("enter the number to be square"))
# square = num3**2
# cube = num3**3
# print("Square:",square)
# print("qube",cube)
# #find even or odd
# num4 = int(input("enter the number:"))
# if num4 % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# #check positive neg or zero
# num5 =int(input("enter the number"))
# if num5 < 0:
#     print("Negative")
# elif num5 == 0:
#     print("Zero")
# else:
#     print("positive")
# #finding greator
# if num1 > num2:
#     print(num1," is graetor")
# elif num2 > num1:
#     print(num2," is greator")
# else:
#     print("Both are equal")

# #checking voting eligibility
# age = int(input("enter the age:"))
# if age >= 18:
#     print("Eligible to vottttte")
# else:
#     print("not eligible")

# #print multiplication table
# num6 = int(input("enter the number:"))
# for i in range(1, 11):
#     print(num6, "x", i, "=", num6*i)

# # 9. sum of first natural numbers
# n =int(input("Enter the n"))
# total = 0
# for i in range(1, n+1):
#     total = total+i
# print(total)

n1 = int(input("enter the n value"))
total1 = 0
for i in range(1, n1+1):
    total1 +=i
print(total1)

#reverse the given number
number1 = int(input("enter the number"))
rev = 0
while number1 > 0:
    last_digit = number1 % 10
    rev = rev*10+last_digit
    number1 = number1 // 10
print(rev)


input n = 8977
rev = 0
while n > 0
last_digit=n%10 #8977%10 __---->7
rev = rev *10 +last_digit # ---> 0*10+7=7
n = n/10

n = 897
last_digit = 7#------>7
rev = 7*10+7 #--->77
n = 89

89%10=ld ->9
ld =9
rev =77*10+9-->770+9=779