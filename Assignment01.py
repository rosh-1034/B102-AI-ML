# Que 1..    even odd function

class EvenOdd:
   
    def Even(self):
        x=int(input("enter a no : "))
        
        if x%2==0:
           print("even")
        else:
           print("odd")
s=EvenOdd()
s.Even()   





# Que 2..  largest of Two Numbers

class Largest:
    def large(self):
        a=int(input("enter a no : "))
        b=int(input("enter a no : "))
        if a>b:
            print(a,"so a is a largest")
        else:
            print(b,"so b is a largest")
s=Largest()
s.large()



# Que 3... Print 1 to n numbers

class Numbers:
    def Print_numbers(self):
        n=int(input("Enter a number : "))
        i=1
        while i<=n:
           
            print(i)
            i=i+1
s=Numbers()
s.Print_numbers() 
          
#Que 4.... sum of n sumbers
class Sum:
    def Sum_n(self):
        n=int(input("Enter a number : "))
        i=0
        total_sum=0
        while i<=n:
            total_sum+=i
            
            i=i+1

        print(total_sum)
           
s=Sum()
s.Sum_n() 


# Que 5....Multiplication table
class Multiplication:
    def  table(self):
        n=int(input("Enter a number : "))
        i=1
        multi=1
        while i<=10:
    
         multi=n*i
         print(multi)
         i+=1
  
s=Multiplication()
s.table()        


# Que 6...Count Even Numbers
class EvenNum:
    def __init__(self):
    
     self.numbers=[3,7,8,4,96,66,43,46]
    def count_even(self):
        idx=0
        even_count=0
        while idx<len(self.numbers):

            if self.numbers[idx]%2==0:
              even_count+=1
           
            idx+=1

        print(even_count) 
          
s=EvenNum()  
s.count_even()  


# Que 7 .....find largest number

class Largest:
 
  def find_max(self,numbers):
      
      large=numbers[0]

      for num in numbers:
         if num > large:
            large=num
      return large   

s=Largest()  
numbers = [44,7,86,43,3,8,12,]  

print(s.find_max(numbers))



# Que 8. print 1 to 100
# print 1 to 100 numbers
class Numbers:
    def value():
        i=1
        while i<=100:
            
            print(i)
            i+=1

s=Numbers
s.value()




# 11)divisible by 3 and 5 print fizzbuzz

def FizzBuzz():
    for i in range(1,101):
        if i%3==0:
            print("Fizz")
        elif i%5==0:
            print("buzz")  
        elif i%3 and i%5 == 0:
            print("FizzBuzz")
        else:
            print(i)   

FizzBuzz()


# 12)check pelidrome

def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

print(palindrome("nayan"))




# que 13)Count Vowels

def Vowel():
    string=input("Enter a string : ")
    v="aeiouAEIOU"
    count=0
    for char in string:
        if char in v:
            count += 1
    print("Total vowels : ",count)
Vowel()


# 14) Second Largest Number
def second_largest(numbers):
    largest = second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num 
    return second

numbers = [10,80,30,90,50]

print("Second Largest Number:",second_largest(numbers))


# 15)Guessing game
import random

def gussing_game():
    number = random.randint(1,10)

    while True:
        guess = int(input("Guess a number between 1 and 10 :"))
        if guess == number:
            print("Congratulation! You guessed it right.")
            break
        elif guess<number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

gussing_game()



#16) Write a function grade(marks)


def Grade(marks):
    
    if marks >=90:
       return "A"
    elif marks >=80:
        return "B"
    elif marks >=70:
        return "C"
    elif marks >=60:
         return "D"
    else:
         return "F"                 

marks=int(input("Enter a marks :"))

result = Grade(marks)

print("Your Grade is:",result)


