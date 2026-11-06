#...que 1) 1 to 50
# for num in range(1,51):
#     print(num)


#.... que 2)50 to 1

# i=50
# while i>=1:
#     print(i)
#     i-=1




#... que 3)even num
# for num in range(0,101,2):
#      print(num)


#.... que 4)odd num
# for num in range(1,100,2):
#      print(num)


# ...Que 5) divisible by 5
# i=5
# while i<=100:
    
#     print(i)
#     i+=5


# ...Que 6)1 to 10 total sum
# i=1
# sum=0
# while i<=50:
    
#     sum=sum+i
#     i=i+1

# print(sum)



# ...Que 7)1 to 20 even sum
# sum=0
# for i in range(1,21,):
#     if i%2==0:
#         sum=sum+i
        
# print(sum)



# ...Que 8)1 to 20 odd sum

# sum=0
# for i in range(1,20):
#     if i%2 != 0:
#         sum=sum+i
        
# print(sum)


# ...que 9)1 to 20 natural numbers
# for i in range(1,21):
#   print(i)


# ...Que 10)multiplication table

# num=int(input("Enter a number :"))
# i=1
# while i<=10:

#  print(i*num)
#  i=i+1


# ...Que 11) count number 1 to  n
# num=int(input("Enter a number :"))
# i=1
# count=0
# while i<=num:
#     count+=1
#     i=i+1
# print("Total Numbers:",count)



# ..Que 12) square of 1 to 10 numbers
# i=0
# while i<=10:
#     i=i+1
#     print(i*i)


#.. ..Que 13) cube of 1 to 10 numbers
# i=0
# while i<=9:
#     i=i+1
#     print(i**3)



# ...Que 14) 100 to 1 numbers decresing 5
# for num in range(100,0,-5):
#      print(num)

# ...que 15) print numbers between 1 to 100 which is divisible by 3 and 4
# for num in range (1,100):
#     if num%3==0 and num%4==0:
#         print(num)


# ...Que 16)Print first 10 numbers multiple of n 
# num=int(input("Enter a number : "))
# for i in range(1,11):
#    print(i*num)


#.. 17)print 1 to n numbers divisible by 2
# num=int(input("Enter a number : "))
# for i in range(1,num):
#    if i%2==0:
#     print(i)


# ...18)print 1 to n numbers skib disible by 3
# num=int(input("Enter a number : "))
# for i in range(1,num+1):
#    if i%3==0:
#      continue
#    print(i)


# que 19)print 1 to n numbers and stop when the number reaches 20
# num=int(input("Enter a number : "))
# for i in range(1,num+1):
#    print(i)
#    if i==20:
#      break
# print(i)



# ...que 20)
for i in range(1,6):

 print(str(i)*i)
