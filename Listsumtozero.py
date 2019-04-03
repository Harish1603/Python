# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:36:42 2019

@author: user
"""

# Python code to generate 
# random unique numbers and 
# append them to a list 
from numpy.random import randint

def solution(N):
    # write your code in Python 3.6
    
    if N >= 2 and N <= 100:
        while True:
           
            A = randint(-100,100,N+1)
            A.sort()
            A = list(dict.fromkeys(A))
            if sum(A) == 0 :
                print(A)
                break
            else:
                continue
       
        
X = int(input("Please enter number:"))
solution(X) 
        
  
