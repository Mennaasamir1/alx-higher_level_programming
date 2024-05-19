#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
       max_value = next(iter(a_dictionary))
       for key in a_dictionary:
           if a_dictionary[key] > a_dictionary[max_value]:
              max_value = key 
       return max_value
    else:
       return (None)
