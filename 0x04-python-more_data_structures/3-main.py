#!/usr/bin/python3
''' Write a function that returns a set of common elements in two sets.Write a function that returns a set of common elements in two sets.'''

common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

