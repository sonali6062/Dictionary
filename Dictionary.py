#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from difflib import get_close_matches
df = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in df:
        return df[word]
    elif word.title() in df:
        return df[word.title()]
    elif word.upper() in df:
        return df[word.upper()]
    elif len(get_close_matches(word, df.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, df.keys())[0])
        decide = input("Press y for yes or n for no  ")
        if decide == "y":
            return df[get_close_matches(word, df.keys())[0]]
        elif decide == "n":
            return("You have picked a wrong key")
        else:
            return("You have entered wrong input Please enter just y or n ")
    else:
        print("You have picked up a wrong key")
        
word = input("Enter the word you want to search ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)
        
        

