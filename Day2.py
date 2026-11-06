# operators
# type casting
# taking user inputs 
# calculator
# 1.Sum of 2 numbers
number1 = int(input("Enter the first number:"))
number2 = int(input("enter the 2nd number:"))
sum = number1+number2
print(sum)

# 2.Area of Rectangle
length = int(input("Enter the length"))
Breadth = int(input("Enter the breadth"))
Area = length * Breadth
print(Area)

# 3.Simple Interest
amount = int(input("Enter the amount"))
Rate = int(input("Enter the Rate"))
time= int(input("Enter the time"))
SI = amount*Rate*time/100
print(SI)

# 5.Swap two numbers
number1 = int(input("Enter the first number:"))
number2 = int(input("enter the 2nd number:"))
temp = number1
number1 = number2
number2 = temp
print(number1)
print(number2)

# 6.Find the average
total = 0
for i in range(5):
    num = float(input("enter a number"))
    total = total+num
average = total/5
print("Average=",average) 

# 7.find last digit
n = int(input("enter the number"))
last_digit = n%10





