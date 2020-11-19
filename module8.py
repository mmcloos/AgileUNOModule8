"""
Maggie Cloos
11-19-2020
Agile UNO Module 8
"""

# install pylint in venv (pip install pylint)
# use it to correct error & warnings
# achieve score of 7.5 or higher

import pdb

# 1
# import my_module & pprint
# add breakpoint to test data
# view the data in your variables to ensure they are correct
import my_module

import pprint

(Pdb) b 16

# 2
# use the greeting method from my_module to print out your name
# add breakpoint to test data
# view the data in your variables to ensure they are correct
name = "Maggie"
my_module.greeting(name)
pdb.set_trace()
print(name)

# 3
# use the letter_text module to print out a string
# add breakpoint to test data
# view the data in your variables to ensure they are correct
my_module.letter_text(name = "Maggie", amount = "10", denomination = "dollars")

# 4
# use the my_module.my_json_data and print it out
# add breakpoint to test data
# view the data in your variables to ensure they are correct
from my_module import my_json_data
print(my_json_data())

# 5
# import the my_json_data as my_data and print out the my_json_data using pprint
# add breakpoint to test data
# view the data in your variables to ensure they are correct
from my_module import my_json_data as my_data
pprint(my_data)
