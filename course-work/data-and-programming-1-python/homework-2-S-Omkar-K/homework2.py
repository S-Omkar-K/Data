# PPHA 30535
# Spring 2022
# Homework 2

# Sai Omkar Kandukuri
# S-Omkar-K

# Due date: Sunday April 17th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]
end_list = []
def sum_size(a, b):
    sum = a + b
    
    if sum < 10:
        return 'small'
    elif sum == 10:
        return 'just right'
    elif sum > 10:
        return 'big'
    

end_list = [sum_size(element[0], element[1]) for element in start_list]
print(end_list)


    

# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 30
    return a + b
x = my_func()


#Answer
#a = 10
def my_func(a = 10):
    b = 30
    return a + b
x = my_func(10)

#Code readability becomes better 
#Code complexity reduces as the global variable can be accessed 
#and modified by a different function/class which directly affects the result of my_func


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.



import random
def generate_password(length, special_chars = True, numbers = True):
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '1234567890'
    special_characters = '(!@#$%^&*)'
    password = ''
    
    if length <8 or length >16:
        return("Error: Password length should be between 8 and 16")
    
    if special_chars == False :
        if numbers == False:
            for i in range(length):
                password += random.choice(alphabets)
        else:
            for i in range(length):
                password += random.choice(alphabets + digits)       

    else:
         if numbers == False:
             for i in range(length):
                 password += random.choice(alphabets + special_characters)
         else:
             for i in range(length):
                 password += random.choice(alphabets + special_characters + digits)
   
    return password


new_random_password = generate_password(12, True, True)
print(new_random_password)

#Another way for this question is by importing random, string
#import random
#import string
#from numpy import random
  
#def random_pwd(length, special_chars = True, numbers = True):
#    if length <8 or length >16:
#        return("Error: Password length should be between 8 and 16")
    
#    if special_chars == False :
#        if numbers == False:
#            password_strings = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
#        else:
#            password_strings = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

#    else:
#         if numbers == False:
#             password_strings = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
#         else:
#             password_strings = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
   
#    password_combination = random.sample(password_strings,length)
#    password = "".join(password_combination)
#    return password

#x = random_pwd(10, True, False)
#print(x)







  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 1, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes any number of these instances and 
# returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])



class VaccineRecord:
    def __init__(self, name, vaccine, doses, covid):
        self.name = name
        self.vaccine = vaccine
        self.doses = doses
        self.covid = covid
        
    def get_record(self):
        if self.covid:
            print( self.name + ' has ' + str(self.doses) + ' doses of ' + self.vaccine +' and has had covid before')
        else:
            print( self.name + ' has ' + str(self.doses) + ' doses of ' + self.vaccine + ' and has never had covid before')
        
    def same_shot(self, another_person):
        if self.vaccine == another_person.vaccine:
            print(self.name + ' and ' + another_person.name + ' have same kind of vaccine')
        else:
            print( self.name + ' and ' + another_person.name + ' does not have same kind of vaccine')
 
def all_data(*argv):
    my_list = []
    for arg in argv:
        my_list.append([arg.name, arg.vaccine, arg.doses, arg.covid])
    return my_list
   



     
Aaron = VaccineRecord('Aaron', 'Moderna', 1, False)
Ashu = VaccineRecord('Ashu', 'Pfizer', 2, False)
Alison = VaccineRecord('Alison', 'none', 0, True)
Asma = VaccineRecord('Asma', 'Pfizer', 1, True)

Asma.get_record()
Aaron.same_shot(Alison)
Aaron.same_shot(Asma)
all_data(Alison, Aaron, Asma)
all_data(Alison, Aaron)



#If asked for 3 methods instead of 2 methods and a function
#class VaccineRecord:
#    def __init__(self, name, vaccine, doses, covid):
#        self.name = name
#        self.vaccine = vaccine
#        self.doses = doses
#        self.covid = covid
#        
#    def get_record(self):
#        if self.covid:
#            print( self.name + ' has ' + str(self.doses) + ' doses of ' + self.vaccine +' and has had covid before')
#        else:
#            print( self.name + ' has ' + str(self.doses) + ' doses of ' + self.vaccine + ' and has never had covid before')
#        
#    def same_shot(self, another_person):
#        if self.vaccine == another_person.vaccine:
#            print(self.name + ' and ' + another_person.name + ' have same kind of vaccine')
#        else:
#            print( self.name + ' and ' + another_person.name + ' does not have same kind of vaccine')
# 
#   def all_data(*argv):
#       my_list = []
#       for arg in argv:
#           my_list.append([arg.name, arg.vaccine, arg.doses, arg.covid])
#       return my_list



