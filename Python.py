# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16MnzEVKg1_9tEXjmmM9fUrB6Vpf5lE2M
"""



"""1. What is Python and why is it useful?
        

   Python is a high level programming language. Python is used for AI,   maching learning, operating system etc.

2. Are the following variable names allowed in python?
1_message - not allowed,
Greeting_message - allowed,
Message_1 - allowed,
First name - not allowed,
Full_name - allowed,
"""

var = "Hello There!"
print(var)

first_name = "umme"
last_name = "habiba"
email_extension = "@gmail.com"
print(first_name+last_name+email_extension)

name = "Umme"
print(name.lower())
print(name.upper())

date = 15
var = "Do you want to hang out on the " + str(date) +"th of this month?"
print(var)

list = ["sister sister", "how I met your mother", "the good doctor", "the originals", "agents of shield"]
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
len(list)