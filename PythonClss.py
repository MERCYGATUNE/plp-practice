# Python Class
import math
import random
import datetime

Babe= "Rodgers"
if Babe == "Rodgers":
    print("My guy!!")
else:
    print("Just another guy!") 
        
Rich = 90000
if Rich >= 70000:
    print("Grind hard")
else:
    print("you're rich!!")
    
         
         
               
  # Prompt the user for student marks
marks = int(input("Enter the student's marks (0-100): "))

# Grading system based on the marks
if marks > 70:
    print("Grade: Flying colours🏆")
elif marks >= 60:
    print("Grade: Credit 🎖️")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")
    
# Print numbers 0 to 4
# For loop
for i in range(6):
    print(i)   
     
# While loop

countdown = 15

while countdown > 10:
    print("Counting down:", countdown)
    countdown -= 1

print("Blast off! 🚀") 

name="Mercy"
print(name)
age_1=18
print(age_1)

# LISTS IN PYTHON

fruits=["apple","banana","melon"]
print(fruits)

# Accessing individual elements
print(fruits[0])
# Accessing the last element
print(fruits[-1])

# Modifying element
fruits[1]="Strawberry"
print(fruits)

# Adding an element
fruits.append("grape")
print(fruits)


# TUPLES IN PYTHON

# Tuples are like lists but unchangeable.
coordinates=(10,20)
print(coordinates)

# Accessing individual tuple elements
print(coordinates[0])


# Sets
# Collection of unique items, NO DUPLICATES allowed
num={1,2,2,3,9,9,45}
print(num)

# DICTS/Dictionaries
# Stores key-value pairs.
students={"name":"Kat","age":20,"grade":"B+","name":"Stella","age":22,"grade":"A"}
print(students)
print("The students in the school are:", students)

# PYTHON FUNCTIONS
# Functions are reusable blocks of code
def greet(name):
    print("Hello,"+ name +" !!")
greet("Mercy")
greet("Rodgers")

def old(age):
    print("How old are you" ,age)
old(25)    
old(30)

def score(number):
    print("What is your grade ?",number)
score(85) 
score(90)   

def name(letter):
    print("What is your name?",letter)
name("Shiko")  



def dinner(food):
    print("What will we have for supper ?",food)
dinner("Githeri")
dinner("Rice")
dinner("What do you like")    

def add_num(x,y):
    return x+y
m=add_num(15,20)
print(m)
      
    # MODULES IN PYTHON
    
 # Math module is for mathematical functions.  
print(math.sqrt(25)) 
print(math.sqrt(36))      

# RANDOM MODULES for generating random numbers.

# Generate a random number between 1 and 6 (like rolling a die)
dice_roll = random.randint(4, 9)
print("You rolled a", dice_roll)

count_down=random.randint(10,200)
print("Countdown begins now!",count_down)

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even! ⚖️")
    else:
        print(number, "is odd! 🎯")

check_even_odd(21)  # Try with different numbers!
def morning(greetings):
     print("What is Good morning in your language?",greetings)
morning("Habari ya asubuhi?")
morning("Guten morgen")

site_name="Mercy"
print(site_name)

site_name="New website"
print(site_name)

#  DATA TYPEES IN PYTHON


# NUMBERS
num1 = 55
num2 = 5.3
print(num1)
print(num2) 

# LISTS IN PYTHON
languages = ["Python", "Dart", "Web", 23]
print(languages)
print(languages[0])

# TUPLE

shoe=("Air-force",40,"colour-black")
print(shoe)
print(shoe[1])

# STRINGS 

name="Mercy Ariri"
print(name)

# SETS
student_ids = {112, 114, 117, 113}
print(student_ids)

# DICTIONARIES /DICT

student={
    "name":"John",
    "class": 7,
    "age":12
}
print(student)


# ARITHMETIC OPERATORS


# ADDITION
a=7
b=6
print(a+b)

# MODULUS/Remainder

nm=90
nm1=4
print(nm % nm1)

# DIVISION
price=600
unit=30
print(price//unit)

#  ASSIGNMENT OPERATORS

x =5
print(x)

x +=3
print(x)

x-=3
print(x)

x *=3
print(x)

x/=3
print(x)

x%=3
print(x)

x//=3
print(x)

x**=3
print(x)

#  COMPARISON OPERATORS

A=7
print(A)
A!=7
print(A)

A > 5
print(A)

# LOGICAL OPERATORS

x < 5 or x < 10
print(x)
