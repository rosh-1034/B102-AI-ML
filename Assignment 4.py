# 1.even or odd program
# num=int(input("enter a number : "))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")   

# 2) largest of three numbers
# a=int(input("enter a number1 : "))
# b=int(input("enter a number2 : "))
# c=int(input("enter a number3 : "))
# if a>=b and a>=c:
#     print("a is a largest")
# elif b>=c:
#     print("b is largest")
# else :
#     print("c is a largest")

# 3)prime number
# num=int(input("enter a number : "))
# if num>1 :
#     for i in range(2,num):
#         if num % i==0:
#             print("Not prime number ")
#             break
#     else:
#             print("Prime Number")
# else:
#             print("Not prime number ")

# 4)fibonancci series
# num=int(input("enter a number : "))
# a=0
# b=1
# for i in range(num):
#     print(a, end=" ")
#     c=a+b
#     a=b
#     b=c

# 5)factorial of a number using loop
# num=int(input("enter a number : "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("Factorial =", fact)

# 6) reverse string 
# s="Roshani"
# rev=""
# for i in s:
#     rev=i+rev
# print("Reversed string is : ",rev)

# 7)pelindrom
# str=input("Enter a string : ")
# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 8)Vowels and Consonants
# ch = input("Enter a character: ")
# vowels=0
# consonants=0
# for ch in ch:
#    if ch.lower()in "aeiou":
#       vowels+=1
#    elif ch.isalpha():
#       consonants +=1
# print("Vowels :",vowels)
# print("Consonants", consonants)

# 9)sum of all elements in a list
# list=[4,7,8,5,9,43,1]

# sum=0
# for i in list:
#     sum=sum+i
# print("Sum=",sum)  

# 10)find largest and smallest Elements in a list
# list=[4,7,8,1,5,9,43,2,99]

# largest=list[0]
# smallest=list[0]

# for i in list :
#     if i> largest:
#         largest=i
#     if i<smallest:
#         smallest=i

# print("Largest:",largest)   
# print("Smallest:",smallest)   

# 11) remove duplicate element from the list
list=["roshani",22,"Jit",10,"roshani","10"]
new_list=[]
for i in list:
    if i not in new_list:
            new_list.append(i)
print(new_list)
