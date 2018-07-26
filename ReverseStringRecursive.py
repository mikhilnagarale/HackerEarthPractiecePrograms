#!/usr/bin/python
#Ref: http://interactivepython.org/courselib/static/pythonds/Recursion/WhatIsRecursion.html

#Q: Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

def rev(val):
    if len(val)==1:
        return val[0]
    else: 
        return rev(val[1:])+val[0]

    
if __name__=="__main__":
    print(rev('abcdef'))
