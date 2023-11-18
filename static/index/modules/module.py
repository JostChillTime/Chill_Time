# CREATING A LIST OF OBJECTS AND ADDING A NEW OBJECT
# names = ["KON", "Stalovalova", "NeNIHUYA"]
# names.append("Tssss")
# names.sort()
# print(names)




#SET
# s = set()

# s.add(1)
# s.add(2)
# s.add(3)
# s.add(2) #it will not appear, as there are only UNIQUE objects in a SET

# s.remove(2)
# print(s)

# print(f"The set has {len(s)} elements")


#LOOPS

# for i in [0, 1, 2, 3, 4]:
#     print(i)

# for i in range(5):        they do the same, range(prints the number of values you put nto these brackets)
#     print(i)


# name = "sexyboy"

# for character in name:
#     print(character)   #prints every letter of a word





#DICTIONARY
# houses = {"Happiness": "Zafar", "Depression": "Mob"} # happines in Zafar (Zafar - house)

# houses["Nasib"] = "Zafar"

# print(houses["Nasib"])


# #FUNCTIONS
# def square(x):
#     return x * x
# DEF = DEFINE A FUNCTION
# # from functions import square #We basically take anything from another py file

# # for i in range(10):
# #     print(f"The square if {i} is {square(i)}")

# #OR     

# import functions

# for i in range(10):
#     print(f"The square if {i} is {functions.square(i)}")





#CLASSES

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(3, 7) 
# print(p.x)
    

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
    
#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True 

#     def open_seats(self):
#         return self.capacity - len(self.passengers)

# flight = Flight(2)

# people = ["KON", "Stalovalova", "NeNIHUYA"]
# for person in people:
#     if  flight.add_passenger(person):
#         print(f"Added {person} to flight succesfully")
#     else:
#         print(f"no seats for {person}")







#DECORATORS
# def announce(f):
#     def wrapper():
#         print("about to run a function")
#         f()
#         print("Done with the function")
#     return wrapper

# @announce
# def hello():
#     print("Hello, World!")

# hello()

#DECORATORS ARE TAKING THE FUNCTION, ADDING SOMETHING, AND THEN GIVING THEM BACK
# Взял-прокачал-вернул





# people = [
#     {"name": "Mob", "house": "Somewhere quite"},
#     {"name": "Zafar", "house": "Basement"}
# ]

# # def f(person): #person is an input
# #     return person["house"]
# # we can write the same in LAMBDA: key=lambda person: person["house"] it is a complete function

# people.sort(key=lambda person: person["name"]) #key - the way you can solve it, put in order

# print(people)









# #EXCEPTIONS ОХУЕТЬ БЛЯТЬ РАБОТАЕТ ЕБАТЬ
# import sys

# try:
#     x = int(input("x:   "))
#     y = int(input("y:   "))
# except ValueError:
#     print("Nahoi idi")
#     sys.exit(1)
    
# try:
#     result = x/y
# except ZeroDivisionError:
#     print("IDI NAHOI")
#     sys.exit(1)

# print(f"{x} divided by {y} is {result} ")
