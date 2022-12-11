# ****************************************************************
# Project 1: Learning the basics in Python
# ****************************************************************


# ############
# Task #1
#############

# A program that prints out a user's fullname
print("Task 1")
print()  # indicates a space
print("My fullname is Temitope Alamu")
print()  # indicates a space
# A program that prints out a burger recipe
print("""A burger recipe includes:
      1. One slightly burnt bread.
      2. Salads.
      3. Two cheese.
      4. Two burger meats. """)
print()  # indicates a space
# A program that prints out the current weather update of Lagos
print("Today at Lagos, we are currently at 1 degree celsius")
print()  # indicates a space
# A program that performes perfoms 3 basic arithmetic calculations using +, - and *
addition = 30 +20
print(addition)  # adds up 30 and 20
print()  # indicates a space
subtraction = 100 - 30
print(subtraction)  # subtracts 30 from 100
print()  # indicates a space
multiplication = 200 * 80
print(multiplication)  # multiplies 200 with 80
print()  # indicates a space
# ############
# Task #2
#############
# This program stores the names of three cities in a particular variable
# It also formats the output using .title() and .upper()
# goal: to practice .title() and .upper()
print("Task 2")
print()  # indicates a space
city_name = "lagos"  # name of the first city
print(city_name)  # first city printed
print()  # indicates a space
city_name = "toronto"  # name of the second city in the same variable
print(city_name.title())  # printed and formatted using the title() method
print()  # indicates a space
city_name = "ottawa"  # name of the third city in the same variable
print(city_name.upper())  # printed and formatted using the upper() method
print()
# ############
# Task #3
############
print("Task 3")
print()  # indicates a space
# This program stores a name in a variable
# Name is printed within a sentence using f strings for three times
# Name is modified to print in uppercase, lowercase and title 
# goal: getting familiar with f strig, uppercase, lowercase and title method

my_name = "Temitope Alamu"  # name stored in a variable my_name
sentence = "My name is"  # the sentence to use dtored in a variable sentence
my_fname = f"{sentence} {my_name}" 
print(my_fname)  # My name prints using an f string
print()  # indicates a space
print(my_fname.upper())  # My name printed in uppercase
print()  # indicates a space
print(my_fname.lower())  # My name printed out in lowercase
print()  # indicates a space
print(my_fname.title())  # My name printed out in title case
print()  # indicates a space

# ############
# Task #4
############
print("Task 4")
print()  # indicates a space
# A program that prints a canadian food with spaces at the beginning and end
# This program also uses the following methods(.rstrip(),
# .lstrip(), .strip()) to add and remove spaces in the program.

canadian_food = "\tButter Tarts\n"  # name of canadian food with spaces at the beginning and end
print(canadian_food)  # canadian food printed with spaces at beginning and end
print()  # indicates a space
print(canadian_food.lstrip())  # canadian food printed with cleaned white spaces at the left
print()  # indicates a space
print(canadian_food.rstrip())  # canadian food printed with cleaned white spaces at the right
print()  # indicates a space
print(canadian_food.strip())  # canadian food printed with no white spaces
print()  # indicates a space
# ############
# Task #5
############
print("Task 5")
print()  # indicates a space
# This program performs four different operations that results to 2022
# It prints out a message explaining my results
# Also it prints out the results using the f string and + method to concatenate.

operation1 = 2020 + 2  # addition operation that results to 2022
statement1 = "Addition of 2020 and 2 would give"
print(f"{statement1} {operation1}")
print()  # indicates a space
operation2 = 2024 - 2  # subtraction operation that results to 2022
statement2 = "Subtracting 2 from 2024 would give"
print(f"{statement2} {operation2}")
print()  # indicates a space
operation3 = 1011 * 2  # multiplication operation that results to 2022
statement3 = "Multiplying 2 with 1011 would give "
print(statement3 + str(operation3))
print()  # indicates a space
operation4 = 4044 / 2  # division operation that results to 2022
statement4 = "Dividing 4044 with 2 would give "
print(statement4 + str(operation4))
print()  # indicates a space
# ############
# Task #6
############
print("Task 6")
print()  # indicates a space
# A program that prints the speed a dog covered at a given time
distance = 80.0  # distance the dog covered
time = 17.0     # time the dog covered
speed = distance / time     # formular for speed
print("The dog covered a distance of " f"{speed}" " m/s")   # result
