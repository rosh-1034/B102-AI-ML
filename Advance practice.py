# ********....1]DATA TYPE....***********

# 1)Find Data type of every value in a mixed list 

list=["roshani",23,True,22.8]
for i in list:
 print(type(i))

#              *******

# 2)convert a nested list into a tuple of tuples

list=[[1,2],[3,4],[5,6]]
result=tuple(tuple(i)for i in list)
print(result)

#              *******

# 3)Remove all duplicate values from a mixed list while preserving the original order.

my_list = [10,20,10,30,20,40,30]
new_list=[]

for i in my_list:
    if i not in new_list:
       new_list.append(i)
print(new_list)       

#              *******


# ********...2].Operators....***********

# 4)check whether a number is a power of 2 using operators

num=int(input("Enter a number: "))

if num > 0 and (num &(num-1))==0:
    print("Power of 2")
else:
    print("Not a power of 2")

#              *******

# 5)Swap two numbers using bitwise XOR

a=10
b=20

a=a^b
b=a^b
a=a^b

print("a=",a)
print("b=",b)

#              *******


# 6)Find whether a number is divisible by both 4 and 6 using logical operators

num=int(input("enter a num :"))
if (num%4==0) and (num%6==0):
    print(f"{num} is divisible by 4 and 6")
else:
    print("not divisible by both")

#              *******

# 7)Calculate the total electricity bill using different unit rates

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total electricity bill:", bill)

# ********...3].Conditional Statements....***********

# 8. Check whether three sides form a triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle is possible")
else:
    print("Triangle is not possible")

# 9. Determine type of triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")

# 10. Simple ATM menu

balance = 5000

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    elif choice == 2:
        amount = int(input("Enter amount: "))
        balance = balance + amount
        print("Deposit successful")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")

# 12. Menu-driven calculator using if-elif

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Addition:", a + b)
elif choice == 2:
    print("Subtraction:", a - b)
elif choice == 3:
    print("Multiplication:", a * b)
elif choice == 4:
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")

# ********...4].Loops....***********

# 13. Print all prime numbers between 1 and n

n = int(input("Enter number: "))

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)

# 14. Factorial using a loop

n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

# 15. Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

# 16. Check Armstrong number

n = int(input("Enter number: "))

temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# 17. Reverse a number and check palindrome

n = int(input("Enter number: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse:", rev)

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 18. Find GCD of two numbers    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD:", a)

# ********...5].Function....***********

# 19. Function to check string palindrome

def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

s = input("Enter string: ")

palindrome(s)

# 20. Function to count vowels and consonants

def count(s):
    vowels = 0
    consonants = 0

    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

s = input("Enter string: ")

count(s)

# 21. Calculate simple and compound interest

def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    print("Simple Interest:", si)
    print("Compound Interest:", ci)

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

interest(p, r, t)

# 22. Return all factors of a number

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

n = int(input("Enter number: "))

factors(n)

# 23. Find second-largest number in a list

def second_largest(lst):
    largest = lst[0]
    second = None

    for i in lst:
        if i > largest:
            second = largest
            largest = i
        elif i < largest:
            if second == None or i > second:
                second = i

    return second

lst = [10, 20, 5, 30, 15]

print("Second largest:", second_largest(lst))

# ********...6].List....***********

# 24. Merge two lists without duplicates

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = []

for i in a + b:
    if i not in c:
        c.append(i)

print(c)

# 25. Find second-largest and second-smallest elements

lst = [10, 20, 5, 30, 15]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

unique.sort()

print("Second smallest:", unique[1])
print("Second largest:", unique[-2])

# 26. Rotate a list to the left by k positions

lst = [1, 2, 3, 4, 5]

k = int(input("Enter k: "))

k = k % len(lst)

new = lst[k:] + lst[:k]

print(new)

# 27. Separate even and odd numbers into two lists

lst = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)

# 28. Find common elements between two lists

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for i in a:
    if i in b and i not in common:
        common.append(i)

print("Common elements:", common)

# ************..... 7]. Tuples & Sets....**************
# 29. Count frequency of each element in a tuple

t = (1, 2, 2, 3, 3, 3, 4)

for i in t:
    if t.count(i) > 0:
        print(i, ":", t.count(i))

# 30. Union, intersection and difference of two sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# 31. Check whether one set is a subset of another

a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("A is subset of B")
else:
    print("A is not subset of B")

# ***********....8]. Dictionaries...**************
# 32. Count frequency of words in a sentence

s = input("Enter sentence: ")

words = s.split()

d = {}

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# 33. Create dictionary from two lists

keys = ["name", "age", "city"]
values = ["Roshani", 22, "Nashik"]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)

# 34. Sort dictionary by values

d = {"A": 50, "B": 20, "C": 40}

result = dict(sorted(d.items(), key=lambda x: x[1]))

print(result)

#**********....... 9]. File Handling........*********

# 35. Count lines, words and characters in a text file

f = open("demo.txt", "r")

data = f.read()

lines = data.split("\n")
words = data.split()
characters = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

f.close()

# 36. Copy only even-numbered lines from one file to another

f1 = open("demo.txt", "r")
f2 = open("output.txt", "w")

lines = f1.readlines()

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        f2.write(lines[i])

f1.close()
f2.close()

print("File copied successfully")

# ***********....10]. Exception Handling...***********
# 37. Handle invalid integer input using try-except

try:
    n = int(input("Enter number: "))
    print("Number:", n)

except ValueError:
    print("Please enter a valid integer")

# 38. Handle file-not-found errors

try:
    f = open("demo.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File not found")

# ************.....11]. Modules.....************
# 39. Random password generator using random and string modules

import random
import string

characters = string.ascii_letters + string.digits

password = ""

for i in range(8):
    password += random.choice(characters)

print("Password:", password)

# 40. Calculate number of days between two dates

from datetime import date

d1 = date(2026, 1, 1)
d2 = date(2026, 12, 31)

difference = d2 - d1

print("Total days:", difference.days)





















































