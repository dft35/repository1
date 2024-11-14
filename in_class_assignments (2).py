# -*- coding: utf-8 -*-
"""In Class Assignments.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PqgmL15TQ7jSqypXgb7j4aEVidRzAyrQ
"""

pi = 3.1415
r = 3
h = 10

Area = 2*pi*r**2 + 2*pi*r*h
print(Area, )

x=2
y=3.14
s= 'abc'
print(x,y,s)

pi = 3.14
r = 5

Area = pi * (r**2)
print("Area =", Area, "square feet") #Display using only objects
print("Area = {} square feet" .format(Area) ) #Display using .format method
print(f"Area = {Area} square feet") #Display using f-strings
print("End of program...")

pi = 3.14
r = input("Provide a value for radius: ")
r = float(r)



type(r)

pi = 3.14
r = 5
c = 10
h = 8
shape = "triangle"


if shape == "circle":
  Area = pi * (r**2)
  print(Area)

elif shape == "sq":
  Area = c ** 2
  print(Area)

elif shape == "triangle":
  Area = .5 * c * h
  print(Area)

else:
  Area = 2*pi*r**2 + 2*pi*r*h
  print(Area)

gr = 91

if gr > 96:
  print("A+")
elif gr > 93:
  print("A")
elif gr > 90:
  print("A-")
elif gr > 88:
  print("B+")

amount = float(input("Enter investment amount in $:"))
customer_type= input("Enter customer type (n is new, e is existing):")

if amount <= 1000 and customer_type == 'e':
  ir = 0.03
  ret = (1 + ir) * amount

elif amount <= 10000 and customer_type == 'e':
  ir = 0.0325
  ret = (1 + ir) * amount

elif amount <= 100000 and customer_type == 'e':
  ir = 0.035
  ret = (1 + ir) * amount

elif amount > 10000 and customer_type == 'e':
  ir = 0.035
  ret = (1 + ir) * amount

else:
  ir = 0.04
  ret = (1 + ir) * amount

print(f'Annual return after 1 year: ${ret}')

p1 = input('Enter P1: Rock, Paper, or Scissors:')
p2 = input('Enter P2: Rock, Paper, or Scissors')

if p1 == p2:
  print("Draw")

elif (
    (p1 == 'Rock' and p2 == 'Scissors') or
    (p1 == 'Paper' and p2 == 'Rock') or
    (p1 == 'Scissors' and p2 == 'Paper')):
    print("P1 wins")

else:
  print("P2 wins")

print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("** for exponents")
operator = (input("Enter math operator: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':2
  print(num1 + num2):

elif operator == '-':
  print(num1 - num2)

elif operator == '*':
  print(num1 * num2)

elif operator == '/':
  print(num1/num2)

elif operator == '**':
  print(num1**num2)

!pip install ColabTurtlePlus

from ColabTurtlePlus.Turtle import *


clearscreen()


reset = True

if reset:
  clear()

color('black', 'green')
shape('blank')
begin_fill()
jumpto(0, 0)

for i in range(4):
  forward(100)
  left(90)


penup()
end_fill

for i in range(1,9999999):
  print(i, end=' ')

for i in range(1,11,2):
  print(i,end='')

i = 1
while i < 10:
  print(i, end='')
  i = i + 2

customer_type = input('Existing or new')

while customer_type == 'existing':
  print('.....')
  customer_type = input('Existing or new')

Emotion = input("Do you want to play: Yes or No ")

while Emotion == 'Yes':

  p1 = input('Enter P1: Rock, Paper, or Scissors:')
  p2 = random.choice(Rock, Paper, or Scissors:)

  print(f'Player Chose {p1}')
  print(f'Computer Chose {p2}')

  if p1 == p2:
    print("Draw")

  elif (
    (p1 == 'Rock' and p2 == 'Scissors') or
    (p1 == 'Paper' and p2 == 'Rock') or
    (p1 == 'Scissors' and p2 == 'Paper')):
      print("P1 wins")

  else:
    print("Computer wins")

  Emotion = input("Yes or No ")

print("Have a nice day")

#Garage Problem
flatrate = 5
hourlyrate = 2.5

for i in range (1,9):
  charge =flatrate + i*hourlyrate
  if charge < 10:
    charge = 10
  elif charge > 20:
    charge = 20
  print(i, charge)

  i = i + 1

# Movie Theatre Advertising

tixprice = 10
fixedcost = 200

for i in range(0,201,25):
  moreattendees = 2*round(i**.5)
  profit = tixprice * (moreattendees + 20) - i - fixedcost
  print(i, profit)

i = i +1

i = 0

while True:
  i = i + 1
  if 1 == 10:
    break
  print(i, end = ' ')

print('Done.')

s = "this is a string"
t = "123456"
f = "asdf124%6&&*"
# lets take a look at length
print(len(s))
print(len(t))
print(len(f))
s[2]

this = s[0:4:2]
this

string = s[10:len(s)]
string

len(t)

t[-1]

t[1:len(s)-1]

"123" + "abc"

for idx in range(len(s)):
  print(s[idx])

for char in s:
  print(char)

for idx in range(len(s)):
  if s[idx] == 'a':
    print('Letter a found')
    break

for char in s:
  if char == 'a':
    break

list = [1,2,3]
# this is a list with 3 items
another_1 = [1,3.14,'abc',True,[5,6,7]]
# this is a list with five items
empty_l = []

another_1[4]

list[1]=5

3*list

list.append(4)
1

list.insert(1,6)

l = [1,2,3]
l2 = [4,5,6]
l.extend(l2)
l

l.pop(6)
l

l = [1,5,2,7,4,9]
l.sort(reverse=True)
l

l = []
while True:
  user = int(input("Enter a number: "))
  if user == 0:
    break
  l.append(user)

print(l)

L1 = [1,2,3,4]
L2 = [1,2,5,6,]


for item in L1[:]:
  if item in L2:
    L1.remove(item)
print(L1)

#Easy way to fix it is to create a clone

#Tuple with five objects

t = (1, 'two', 3.0, [4,6,8], (1,2,3))
#Lets try to modify it
(1,2,3)+('one','two')
(1,2,3)+(1,2,3)

2*(1,2,3)

len(t)

t[1:4]

s = ""
l = []
t = ()

s = s + 'a'
s

l = l + [4]
l

t = t + ('three',)
t

d = {'John':95,'Jane':93,'Bob':87,'Anne':90}

d["Bryan"] = 85
d

del(d["Bryan"])
d

d['John'] = 93
d

db = {
    'davidturkel7@gmail.com':{
        'First':'David',
        'Last':'Turkel'
    }
}
        'Phone':'555-555-5555'
    },
    'example2@gmail.com':{
        'First':'John'
        'Last':'Doe'
        'Phone':'555-555-5555'
    }
)

months = {}

names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

for idx in numbers:
    months[idx] = names[idx-1]

months

months[3]

for key in months.keys():
    print(key)

for val in months.values():
    print(val)

for key, value in months.items():
    print(key, value)

#October 9. Learning about sets. It has {} like dictionaries
# Sets don't allow duplicated values

x = {1, 2.5, 3}

type(x)

L = [1, 1, 2, 3, 5]
# One is repeated. Turn it into a set. Cast

set(L)

s1 = set(L)
s2 = {1,4,8}

s1.intersection(s2)

s1.union(s2)

# What's in S1, but NOT in S2??
s1.difference(s2)

# What's in S2, but NOT in S1?
s2.difference(s1)

# Exist only in A or B but not in both
s1.symmetric_difference(s2)

x = input('.....')

def func(inp1,inp2,inp3): #Input part
  expr1                   #Process Part
  expr2
  result = final_expr
  return result           #Output Part



x = 2
y = 'hello'
z = [1,2,3]

w = func(x, y, z)

def adder(a, b):
  print("We are inside adder")
  c = a + b
  return c

x = 3 # A = X
y = 4 # B = Y
z = adder(x, y) # Z = C
                # C = A + b, or X + Y
                # what is outpu tis C
print(z)

def adder(a, b):
  print("We are inside adder")
  c = a + b
  return c

x = 3
y = 4
z = x + y
print(z)
# Function was never called.

#Exercise One
total_cost = 1,000,000
portion_down_payment = .25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary in $: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#Assignment Two

#Assignment Three

def adder(a, b):
  res = a + b
  return res

x = 3
y = 2.5

z = adder(3, 2.5)
print(z)

def range_check(num, low, high):
  if num >= low and num <= high:
    return True
  else:
    return False

print(range_check(2,1,3))

res = range_check(num =2, low=1, high=3)
print(res)

res = range_check(rn=[1,2,3], 2)

def inputs():
  annual_salary = float(input("Enter your annual salary in $: "))
  portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
  total_cost = float(input("Enter the cost of your dream home: "))
  return annual_salary, portion_saved, total_cost

annual_salary, portion_saved, total_cost = inputs()

def name(first,last,reverse=False):
  if reverse == True:
    print(last, ',', first)
  else:
    print(first, last)

name('David', 'Turkel', True)
#The complicated thing needs to come last in the function input

#PARKING GARAGE PROBLEM

def calcFee(hours):
  print(5 + hours * 2.5)





hours = float(input(("How many hours will you park? ")))

fee = calcFee(hours)

print(fee)

# More Advanced., worrying about decimals
def calcFee(hours,decimals=2):
  fee = 5 + hours * 2.5
  fee = round(fee, decimals)
  return fee


def displayFee(fee):
  print(fee)


hours = float(input(("How many hours will you park? ")))

fee = calcFee(hours)

displayFee(fee)

def f(x):
  y = 1
  x = x + y
  print('x =', x)
  return x



if __name__ == '__main__':
  x = 3
  y = 2
  z = f(x)
  print('z =', z)
  print('x =', x)
  print('y =', y)

def reverse(s):
  if len(s) == 1:
    return s
  else:
    return s[-1] + reverse(s[1:-1]) + s[0]
    return reverse(s[1:]) + s[0]
    return s[-1] + reverse(s[:-1])


reverse('Hello')

# WEDNESDAY November 6TH.

def wAvg(L,W):
  try:
    res = []
    for i in range(len(L)):
      res.append(L[i]*W[i])
    return sum(res) / sum(W)
  except ZeroDivisionError:
    print("Divided by Zero")
    return []
  except TypeError:
    print("Non-Numerical Obejcts Found")
    return []
  except Exception as e:
    print(f"Unkown Error: {e}")
    return float('nan')

wAvg([1,2,3],[0.1,0.3,0.4])

# Lecture Nine, Object-Oriented Programming (OOP)
# About Classes, use caps for the first word
#Self needs to be first, needs to be muscle memory

class Car:
  def __init__(self, n_doors, make, year, hp):
    self.n_doors = n_doors
    self.make = make
    self.year = year
    self.n_wheels = 4
    self.engine_running = False
    self.current_speed = 0
    self.hp = hp

  def start_engine(self):
    self.engine_running = True
    print("Engine Started")

  def stop_engine(self):
    self.engine_running = False
    print("Engine Stopped")

  def accelerate(self, new_speed):
    if self.engine_running == True:
      self.current_speed = self.current_speed + new_speed
      print(f'New Speed: {self.current_speed}')
    else:
      print("Engine is not running, start it first bro")

  def brake(self, speed_decrease):
    self.current_speed = max(0, self.current_speed - speed_decrease)
    print(f'New Speed: {self.current_speed}')


  def describe(self):
    print(f'Make: {self.make}')
    print(f'Year: {self.year}')
    print(f'Number of Doors: {self.n_doors}')
    print(f'Number of Wheels: {self.n_wheels}')

  def __repr__(self):
    return f'Car instance; Make:{self.make}, Year:{self.year}'

  def __lt__(self, other):
      return self.hp < other.hp

  def __add__(self, other):
    return self.hp + other.hp

c = Car(4, 'Chevrolet', 2023, 308)
d = Car(4, 'Hellcat', 2023, 700)

c.describe()
d.describe()
# or Car.Describe(C)

c.start_engine()

c.accelerate(50)

c.brake(100)

class Student:
  def __init__(self, name, number):
    self.name = name
    self.number = number
    self.__courses = []

  def enroll(self, NewCourse):
    if NewCourse not in self.__courses:
      self.__courses.append(NewCourse)
      # Append is how you add stuff to existing stuff
    else:
      print("You've already enrolled, no need to worry")

  def get_courses(self):
    return self.__courses

  def set_name(self, newName):
    self.name = newName

  def get_name(self):
    return self.name

  def __repr__(self):
    return f'Name: {self.name}'

s = Student('Bob', '12345')

s.enroll("Geometry")

s.get_courses()

S1 = Student('David', 117, "Geometry")
S2 = Student('Sara', 132, "MultivariableCalculus")

S2.get_name()
S1.get_name()

S2.set_name('Draymond')
S2.get_name()

S1.name = 'William'
S1.name

2+5

"abc"+"a"

2+8
