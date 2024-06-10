"""
https://www.udemy.com/course/pythonforbeginnersintro/learn/lecture/38032726#content 
# Variables and strings
first_name = "avi"
last_name = "jain"

print(first_name + " " + last_name)
print("hi" * 10)

sentence = "avi was playing basketball"
print(sentence[0:3])  #this is taking idices [0,3) because the last is excluded

"""
"""
# Placeholders in Strings

name = "jake"
sent = "%s is 15 years old"
sent2 = "%s %s was the president"
sent3 = "%s is %d years old"
x=20
y=10

print(sent % name)
print(sent2 % ("barack", "obama"))
print(sent3 % (name, 23))

#format strings
print(f"hello, {name}")
print(f"the sum is {x+y}")

"""
"""
#EXERCISES 1

#1
sol1 = (15 + 30)/2
print(sol1)

#2
x = 18
y = 12

x + y
x - y
x * y
x / y
x % y

#3
first_name = "zoey"

#5
print("hello" * 10)

#7
last_name = "yelsky"
full_name = first_name + " " + last_name

#8
word = "beauty"
print(word[3])

#9
long_word = "concatenation"
print(long_word[0:6])

#10
print(long_word[1:])

"""
"""
# Intro to Lists

# ordered items, have an index, know the order

shopping_list = ["apples", "oranges", "bananas", "cheese"]

print(shopping_list[0])

print(shopping_list[0:2]) #again excludes the end index

#add item to list
shopping_list.append("blueberries")
print(shopping_list)

#alter item in a list
shopping_list[0] = "cherries"
print(shopping_list)

#delete item in a list
del shopping_list[1]
print(shopping_list)

#insert item into the list
shopping_list.insert(1, "strawberries")
print(shopping_list)

#length of list
print(len(shopping_list))

shopping_list_2 = ["bread", "jam"]

print(shopping_list + shopping_list_2)
print(shopping_list_2 * 2)

#max and min
list_num = [1,4,7,23,6]
print(f"the max is {max(list_num)} and the min is {min(list_num)}")

"""
"""
# Intro to Dictionaries

#every key is linked/associated with a value

students = {"bob": 12, "rachel": 13, "emily": 15}
print(students)
print(students["rachel"])

#reassign value of a key
students["rachel"] = 14
print(students)

#delete an entry
del students["emily"]
print(students)

#number of entries in dictionary
print(len(students))

#if keys are not unique python will default to last instance

"""
"""
# Intro to Tuples

# tuples are immutable, we can't add, remove, or change elements once initialized

fruits = ("oranges", "apples", "bananas")
print(fruits)

#they are used for consistency and/or safety

print(fruits[0])
print(fruits[0:2])

tup = (12, 14)
tup3 = fruits + tup

print(tup3)

"""
"""
# EXERCISES

#1
names = ["zoey", "candice", "celine"]
print(names[1])

#2
sports = ["vball", "bball", "soccer"]
sports[1] = "football"
print(sports)

#3
nums = [1,2,3,4,5,6,7]
del nums[4]
print(nums)

#4
list1 = [1,2,3,4]
list2 = [5,6,7,8, 99]
list_merged = list1 + list2
print(list_merged)

#5
print(len(list_merged), min(list_merged), max(list_merged))

#6
scores = {"zoey": 95, "candice": 99, "celine": 100, "atta": 69}
print(scores["celine"])

#7
del scores["candice"]
print(scores)

#8
print(list(scores.keys()))
print(list(scores.values()))

#9
shows = ("aot", "vamp diaries", "lain")
print(shows)

#10
more_shows = ("aot", "vamp diaries", "lain", "csm", "adventure time")
print(more_shows[1:4])

"""
"""
# Conditional Statements

#this is dependent on indentations
if 3 < 2:
    print("hello")
else:
    print("condition not true")

#relational operators
# > < >= <= == !=
    
#logical operators
# and, or
 
#else if statements:

age = 16

if age <= 15:
    print("younger than 16")
elif age == 16:
    print("you are 16")
elif age == 17:
    print("you are 17")
else:
    print("older than 16")

if age < 13:
    print("child")
elif age >= 13 and age <= 18:
    print("also child")
else:
    print("adult")

if 5 > 3 or 2 < 1:
    print("hi")

"""
"""
# Intro to For Loops

list1 = ["apples", "bananas", "cherries"]
tup1 = (2,6,10)

#indentation dependent as well

for item in list1:
    print(item)

for item in tup1:
    print(item)

for i in range(0,10):
    print(i) #once again excludes the final value in the range

for i in range(0,11, 2): #the 2 here is the increment number
    print(i)

#nested for loops

for i in range(0,5):
    for j in range(0,3):
        print(i * j)

"""
"""
# Intro to While Loops and Control Statements

#control statements
#break, continue, pass

c = 0
d = 0 
e = 0
f = 0 

while c < 5:
    c = c + 1
    print(c)

while d < 5:
    d = d + 1
    if d == 3:
        break #breaks out of loop
    print(d)

while e < 5:
    e = e + 1
    if e == 3:
        continue #skips everything else in the iteration and starts the enxt iteration
    print(e)

while f < 5:
    f = f + 1
    if f == 3:
        pass #placeholder and does nothing, you can structure your code without implementing it
    print(f)

"""
"""
# Try and Except

#similar to if else statement but having to do with errors

try:
    if name > 3:
        print("hello")
except:
    print("error detected")

"""
"""
# Functions

def hello_world(): #function takes no input parameters
    print("hello world")

hello_world()

def greeting(name):
    print("hi " + name + "!")

greeting("zoey")

def add(num1, num2):
    return num1 + num2

num_sum = add(12,34)
print(num_sum)

def mult(num1, num2):
    return num1 * num2

print(mult(add(1,2),add(3,4)))

"""
"""
# Built in Python Functions

#absolute value
print(abs(-21))

#truth checker, 0 or None gives False
#None gives absence of value
print(bool(None))
print(bool(200))

#dir, shows all methods you can use with a particular object
print(dir("hello"))

#help, shows detailed description of given method
#print(help("hello".upper)) #where upper is a method

#eval, pythons way to run code disguised as a string
sent = "print(\"hello\")"
eval(sent)

#exec, eval but multiple lines

#data type converters: str, int, float
print("hello " + str(100))
print(123 + int("456"))
print(float("3.14"))

"""
"""
# Coding Exercise: make a function that returns the a numbers factorial
#i wrote two options

def calculate_factorial(num):
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num = num - 1 
    return factorial

def calculate_factorial2(num):
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial * i
    return factorial

print(calculate_factorial(5))
print(calculate_factorial2(5))

"""
"""
# Object Oriented Programming - Classes and Objects

#Class: Dog
#Properties: name, age, breed
#Methods: bark, eat, sleep

#an object is an instance of a class
#Object
#Properties: fido, 5, dalmation

#person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
p1 = Person("zoey", 22) #now p is an instance of the Person class
print(p1.getName())
print(p1.getAge())

"""
""""""
# Class Inheritance

class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5

    def drive(self):
        print("Driving a car")

my_car = Car()
my_car.drive()

#now lets create a sporty car class that inherits from the base car class

class SportsCar(Car):
    def __init__(self):
        super().__init__() #ensures you don't lose attributes of the parent class
        self.engine_power = "400 HP"
        self.seats = 2

    def drive(self): #overrides the drive method in the car class
        print("Driving a sports car")

my_sports_car = SportsCar()
my_sports_car.drive()