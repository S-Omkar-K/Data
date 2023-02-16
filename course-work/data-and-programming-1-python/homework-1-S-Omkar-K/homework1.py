# PPHA 30535
# Spring 2021
# Homework 1

# Sai Omkar Kandukuri
# S-Omkar-K

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

# Grader: Valeria Balza
# [-1pt] Q3: Else statement unecessary. 
# [-0pt] Q3: Better practice to use "while True:" or "while cond:" instead of "while 1:"
# [-1pt] Gen: Too many comments, code should be self-explanatory
# Grade: 98/100pts

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.


#Method 1 - By allowing user to input the list manually
inputList = ['python', 3.9, 'An@c0nd@!', 5]
length = len(inputList)
for i in range(0,length):
    print('The value at position ' + str(i) + ' is ' + str(inputList[i]))



#Method 2 - By allowing user to input the list through input() 
inputList = []
length = int(input("Enter number of elements in your list : "))
for i in range(0, length): #iterating till the range
    print('Enter value of element one by one')
    value = input()
    inputList.append(value) #adding the element
for i in range(0,length):
    print('The value at position ' + str(i) + ' is ' + str(inputList[i]))















# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.


#Method 1  Using the isalpha() method 
#input_str = 'A man, a plan, a canal, Panama!'
#input_str = 'Apple'
#input_str = 'radar'
input_str = "This isn't a palindrome"

new_string = '' # Declaring a new string
for i in range(0, len(input_str)): #For loop to iterate over the length of input string
    if input_str[i].isalpha(): #Checking if the character at position i is alphabet or not
        new_string+= input_str[i].lower() #Converting each encountered alphabet to lower case

for j in range(0, int(len(new_string)/2)): #Iterating over the new string
    if new_string[j] != new_string[ len(new_string) - j -1]: #Comparing the characters in new string from both sides
        print("This isn't a palindrome") #If one match fails, then the string is not a palindrome
        break
    elif j == int(len(new_string)/2)-1 : #If we reach the end of iterations without match failure, then the string is palindrome
        print('This is a Palindrome')



#Method 2 #Same as Method 1 but with using a character list
#input_str = 'A man, a plan, a canal, Panama!'
input_str = 'Apple'
#input_str = 'radar'
#input_str = "This isn't a palindrome"
char_list = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper()
#Defining a character list with lower case and upper case alphabets

new_string = '' #Declaring an empty new string
for i in range(0, len(input_str)):
    if input_str[i]in char_list:
        new_string+= input_str[i].lower()

for j in range(0, int(len(new_string)/2)):
    if new_string[j] != new_string[ len(new_string) - j -1]:
        print("This isn't a palindrome")
        break
    elif j == int(len(new_string)/2)-1 :
        print('This is a Palindrome')
 


#Method 3, without a new string
input_str = 'A man, a plan, a canal, Panama!'
#input_str = 'Apple'
#input_str = 'radar'
#input_str = "This isn't a palindrome"

i = 0
j = len(input_str)
left_char = ''
right_char = ''
count = 0
for i in range(0,int(len(input_str))):
    
    if j <= i:
        break
    
    if input_str[i].isalpha():
        left_char = input_str[i].lower()
    else:
        i = i + 1
        continue
    
    for j in range(len(input_str)-count,0, -1):
         if input_str[j - 1].isalpha():
            right_char = input_str[j - 1].lower()
            print(left_char)
            print(right_char)
            if left_char != right_char:
                print("This is not a palindrome")
                break
            count += 1
            break
         else:
            j = j - 1
            count += 1
    
    if left_char != right_char:
        print("This is not a palindrome")
        break
    print("Left and right characters match!")
    
if left_char != right_char:
    print("This is not a palindrome")
else:
    print("This is a palindrome")











# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')

while 1: #Run the loop till a break occurs
    if choice in available_vegetables:#Checking if the vegetable of choice is present in list
    #if choice.lower() in available_vegetables: #Checking if the vegetable input in lower case is present in list
        print('Vegetable is available, you can have it')
        break
    else: #Vegetable not present in list, so provide invalid promt and ask to pick again
        choice = input('Vegetable is not available or Invalid Choice, Please pick again: ')
        
        
        
        
        
        
        
        
        
        
# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

start_list = ['Apple', 'banana', 'Coward','aBBBBB'] #Defining a list of strings
new_list = [i.lower() for i in start_list if i[0] in ('a', 'b')]
print(new_list)


#If the first letters are 'a', 'b', 'A' , 'B'. 
#Giving this example due to Professor comments on Ed Discussion
start_list = ['Apple', 'banana', 'Coward','aBBBBB', 'Box'] #Defining a list of strings
new_list = [i.lower() for i in start_list if i[0] in ('a', 'b', 'A', 'B')]
print(new_list)






# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]

#Method 1
start_list = [3, 5, 7, 9, 11, 13]
#Using (len - i - 1) indexing to access values of list in reverse order
start_list = [start_list[len(start_list) - i - 1 ]*2 for i in range(0,len(start_list))]
print(start_list)

#Method 2
start_list = [3, 5, 7, 9, 11, 13]
start_list = [start_list[-i]*2 for i in range(1,len(start_list)+1)]
#Using negative indexing to access values in list in reverse order
print(start_list)










# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

our_dictionary = {short_names[i]:long_names[i] for i in range(0, len(short_names))}
#Picking values (in short_names for key, long_names for value) by index from 0 -> lenght to create a dictionary
print(our_dictionary)
