import numpy as np
import sys
import datetime
import platform
import math
import calendar
from datetime import date
import random
import os
import string
## TODO Exercices basic 1
# First Exercice print twinkle little star in a specefic manner
def exo1():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\
    \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\
    \nTwinkle,twinkle, little star,\n\tHow I wonder what you are")
# Write a Python program to find out what version of Python you are using.
def exo2():
    print(sys.version)
    print(platform.python_version())
# Write a Python program to display the current date and time.
def exo3():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
def exo4():
    r = float(input("Input the radius of the circle : "))
    print(f"Area: {math.pi * r**2}")
# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
def exo5():
    
    fname = input("Input your first name : ")
    lname = input("Input your last name : ")
    print(f"{lname} {fname}")
# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
def exo6():
    str = input("Input the list of numbers separed by commas : ")
    mylist = str.split(',')
    mytuple = tuple(mylist)
    print(mylist)
    print(mytuple)
# Write a Python program that accepts a filename from the user and prints the extension of the file.
def exo7():
    str = input("Input the file's name : ")
    print(f"L'extension du fichier est {repr(str.split('.')[-1])}")
# Write a Python program to display the first and last colors from the following list.
def exo8():
    color_list = ["Red","Green","White" ,"Black"]
    print(repr(color_list[0])+' '+repr(color_list[-1]))
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
def exo9():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : %i / %i / %i"%exam_st_date)
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def exo10():
    n = input("Input a value : ")
    n.join(n)
    print(n,n)
    print(f"Result : {int(n)+int(n*2)+int(n*3)}")
# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
def exo11():
    n = int(input("Input a value : "))
    print(f"Result : {pow(n,2)}")
    print(pow.__doc__)
# Write a Python program that prints the calendar for a given month and year.
def exo12():
    year, month = input("Input year and month (separted by a space) : ").split(' ')
    calendar.prmonth(int(year), int(month))
# Write a Python program to print the following 'here document' => """""" garde le format du text.
def exo13():
    print("""
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example
    """)
# Write a Python program to calculate the number of days between two dates.
def exo14():
    d1 = (2014, 7, 2)
    d2 = (2014, 7, 11)
    date1 = datetime.date(d1[0],d1[1],d1[2])
    date2 = datetime.date(d2[0],d2[1],d2[2])
    diff = date2 - date1
    print(diff.days)
# 15. Write a Python program to get the volume of a sphere with radius six.
def exo15():
    rad = int(input("Input sphere radius : "))
    print("Volume of the sphere is : ", (4/3) * math.pi * rad**3)
# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
def exo16():
    n = int(input("Input a value : "))
    cond = (n <= 17)
    temp = (17 - n) if cond else 2*(abs(n-17))
    return temp
# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
def exo17():
    n = int(input("Input a value : "))
    return ((abs(1000 - n) <= 100) or (abs(2000-n) <= 100))
#18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def exo18():
    a = int(input("Input a value : "))
    b = int(input("Input a value : "))
    c = int(input("Input a value : "))
    sum = a+b+c
    return ((sum*3) if (a == b == c) else sum)
# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
def exo19():
    mystr = input("Input a string : ")
    if(not mystr.startswith("Is")):
        mystr = "Is" + mystr
    return mystr
# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def exo20():
    n = int(input("Input a number : "))
    mystr = input("Input a string : ")
    return (mystr*n)
# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
def exo21():
    n = int(input("Input a number : "))
    print("The number is : ", "even" if (n % 2 == 0) else "odd")
# 22. Write a Python program to count the number 4 in a given list.
def exo22():
    mylist = [1,2,3,4,5,6,7,8,9,4,4,4,4]
    count = mylist.count(4)
    print(f"There are {count} four in the list {mylist}")
# 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
def exo23():
    n = int(input("Input a number : "))
    mystr = input("Input a string : ")
    print(mystr[:2]*n if (len(mystr) > 2) else mystr*n)
# 24. Write a Python program to test whether a passed letter is a vowel or not.
def exo24():
    mychar = input("Input a letter : ")
    print(mychar+" is a vowel" if (mychar in ['a','e','i','o','u']) else mychar+" is consonant")
# 25. Write a Python program that checks whether a specified value is contained within a group of values.
def exo25():
    n = int(input("Input a value : "))
    print("Exist" if (n in [1, 5, 8, 3] ) else "Doesn't exist")
# 26. Write a Python program to create a histogram from a given list of integers.
def exo26(mylist):
    for i in range(len(mylist)):
        print('*'*mylist[i])
# 27. Write a Python program that concatenates all elements in a list into a string and returns it.
def exo27(mylist):
    mystr = ""
    for i in range(len(mylist)):
        mystr = mystr + str(mylist[i])
    print(mystr)
# 28. Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
def exo28():
    numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
    for x in numbers:
        if x == 237:
            break
        else: 
            print(x)
# 29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
def exo29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(color_list_1.difference(color_list_2))
# 30. Write a Python program that will accept the base and height of a triangle and compute its area.
def exo30():
    base = float(input("Input the base : "))
    height = float(input("Input the height : "))
    print(f"The area of the triangle is {0.5 * base * height}")
# 31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
def exo31():
    a = int(input("Input the first number : "))
    b = int(input("Input the second number : "))
    print(f"The GCD of {a} and {b} is {math.gcd(a,b)}")
# 32. Write a Python program to find the least common multiple (LCM) of two positive integers.
def exo32():
    a = int(input("Input the first number : "))
    b = int(input("Input the second number : "))
    print(f"The LCM of {a} and {b} is {math.lcm(a,b)}")
# 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
def exo33():
    a = int(input("Input the first number : "))
    b = int(input("Input the second number : "))
    c = int(input("Input the third number : "))
    print(f"The sum of {a} and {b} and {c} is {0 if (a == b or b == c or a == c) else a+b+c}")
## TODO Builtin modules
# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class circle():
    def __init__(self,r):
        self.r = r
    def print_details(self):
        print(f"This circle has a radius of {self.r}")
    def calcul_area(self):
        print(f"The area of this circle is {(self.r**2) * math.pi}")
    def calcul_permimeter(self):
        print(f"The permimeter of this circle is {self.r * math.pi * 2}")
# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
class person():
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country 
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - \
         ((today.month, today.day) < \
         (self.date_of_birth.month, self.date_of_birth.day))
        print(f" {self.name}'s age is {age}")
# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class calculator():
    def add(self, a,b):
        print(f"{a} + {b} = {a + b}")
    def sub(self, a,b):
        print(f"{a} - {b} = {a - b}")
    def multi(self, a,b):
        print(f"{a} * {b} = {a * b}")
    def divide(self, a,b):
        print(f"{a} / {b} = {(a/b) if (b!=0) else 'Error'}")
# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
class shape:
    def calcul_area(self):
        pass
    def calcul_permimeter(self):
        pass
class circle2(shape):
    def __init__(self, radius):
        self.radius = radius
    def calcul_area(self):
        print(f"This is a circle and it's area is {(self.radius**2) * math.pi}")
    def calcul_permimeter(self):
        print(f"This is a circle and it's perimeter is {2 * math.pi * self.radius}")
class triangle(shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height
    def calcul_area(self):
        print(f"This is a triangle and it's area is {0.5 * self.b * self.height}")
    def calcul_permimeter(self):
        print(f"This is a triangle and it's perimeter is {self.a + self.b + self.c}")
class square(shape):
    def __init__(self, a):
        self.a = a
    def calcul_area(self):
        print(f"This is square and it's area is {self.a**2}")
    def calcul_permimeter(self):
        print(f"This is square and it's perimeter is {self.a*4}")
## TODO --Data structure following exercices 5 -- 11-- 
# 1. Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()
def gen_1():
    print(f"Generates a random color : ({format(random.randint(0,255), 'x')}{format(random.randint(0,255), 'x')}{format(random.randint(0,255), 'x')})")
    print(f"Generates a random alphabetical string : {chr(random.randint(0,255))}")
    print(f"Generates a random number between 0 and 100 : {random.randint(0,100)}")
    print(f"Generates a random multiple of 7 between 0 and 70 : {random.randint(0,10) * 7}")
# 2. Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory. Use random.choice()
def random_elem():
    # !! set and dictionaries are invalide input because they are no sequences can't be accessed using indexes
    my_list = [1,2,3,4,5,6]
    print(f"{random.choice(my_list)}")
    my_set = set(my_list)
    d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    my_dlist = list(d)
    print(f"{random.choice(my_dlist)}")
    print(f"{random.choice(tuple(my_list))}")
    print(f"{random.choice(os.listdir('.'))}")
# 3. Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()
def random_char():
    max_length = random.randint(0,255)
    print(f"Random char : {chr(random.randint(ord('A'), ord('z') + 1))}")
    s = ""
    for a in range(max_length):
        s += random.choice(string.ascii_letters)
    print(f"Random generated string : {s}")
# TODO data type string
# 1. Write a Python program to calculate the length of a string.
def calculate_len():
    my_string = "Zipzop"
    print(f"The length of {my_string} is {len(my_string)}")
# 2. Write a Python program to count the number of characters (character frequency) in a string.
def count_freq():
    my_string = "www.google.com"
    counter = {}
    for char in my_string:
        # specify return value if there is no element in the dictionary (by default it returns None)
        counter[char] = counter.get(char,0) + 1
    print(counter)
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
def combine_string():
    my_str1 = input("Input a string : ")
    if len(my_str1) < 2:
        print("Empty string")
    else:
        print(f"The new string is {my_str1[:2]+my_str1[-2:]}")
# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def replace_dollars():
    my_str = input("Input a string with dollars : ")
    if len(my_str) < 2:
        print("Empty or too short")
        return 0
    my_table = str.maketrans("$", my_str[0])
    print(my_str.translate(my_table))
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def special_swap():
    my_str1 = "abcdefg"
    my_str2 = "xyz"
    n1 = len(my_str1)
    n2 = len(my_str2)
    print(f"The output is : {my_str2[0:n2-1]+my_str1[-1:]} {my_str1[0:n1-1]+my_str2[-1:]}")
# TODO JSON exercices
import json
# 1. Write a Python program to convert JSON data to Python object.
def convert_json_to_python():
    my_json = '{"name":"Mehdi", "age":23, "city":"Reims"}'
    to_python = json.loads(my_json)
    print(to_python)
    return to_python
# 2. Write a Python program to convert Python object to JSON data.
def convert_python_to_json():
    python_format = convert_json_to_python()
    json_format = json.dumps(python_format)
    print(type(json_format))
    print(json_format)
# 3. Write a Python program to convert Python objects into JSON strings. Print all the values.
def universal_convert_json():
    mydict = {"name":"mehdi","age":23,"city":"Reims"}
    print(type(mydict))
    mylist = ["Red", "Blue", "Yellow"]
    print(type(mylist))
    mytuple = (1,)
    print(type(mytuple))
    print(json.dumps(mydict))
    print(json.dumps(mylist))
    print(json.dumps(mytuple))
# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
def convert_dict_to_json():
    j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
    print(j_str)
    j_str_sorted = dict(sorted(j_str.items()))
    print(j_str_sorted)
    j_json = json.dumps(j_str_sorted, indent = 4)
    print(j_json)
    # or
    print(json.dumps(j_str, sort_keys = True, indent = 4))
## TODO List exercies
import numpy as np
# 1. Sum of a list
def sum_list():
    mylist = [1,2,3,4,5]
    print(np.sum(mylist))
# 280. Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list.
def pairs_of_three():
    mylist = [0,3,5,8,10,7,4,1,9,25]
    pair_list = []
    for n in mylist:
        for x in mylist:
            if abs(n-x) == 3:
                if [x,n] not in pair_list:
                    pair_list.append([n,x])
    
    print(pair_list)
# Print the solution of the exercice
if __name__ == "__main__":
    pairs_of_three()
#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#https://www.w3resource.com/python-exercises/