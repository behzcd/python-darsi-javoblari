# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:32:12 2022

@author: -
"""

import random as r

print("let's play 'Find the Number' game!")

def find_num(x = 10):
    my_tries = 0
    number = r.randint(1,x)
    start = f"I thought a number from 1 to {x}. Can you find the number I thought?"
    print(start)
    while start:
      taxmin = int(input(">>>"))
      my_tries += 1
      if taxmin > number:
        print("Wrong! The number I thought is LESS than the number you entered. Try again:")
      elif taxmin < number:
        print("Wrong! The number I thought is HIGHER than the number you entered. Try again:")
      else:
        print(f"You found! The number I thought actually was {number}. You found it with {my_tries} tries. Congrats!\n")
        break
    return my_tries

def find_num_pc(x = 10):
    print("Think a number from 1 to 10, I'll try to find it!")
    input("If you think a number already, then press any button >>>")
    high = x
    below = 1
    its_tries = 0
    while True:
        its_tries += 1
        guess = r.randint(below,high)
        answer = input(f"You thought {guess}. If it is TRUE (T), the number I thought is HIGHER(+) or LESS(-): ").lower()
        if answer == '+':
            below = guess + 1
        elif answer == '-':
            high = guess - 1
        elif answer == 't':
            break
    print(f"I found it with {its_tries} tries")
    return its_tries


def play(x = 10):
    yana = True
    while yana:
        fnum_me = find_num(x)
        fnum_pc = find_num_pc(x)
        if fnum_me<fnum_pc:
            print(f" You won with {fnum_me} tries")
        elif fnum_me>fnum_pc:
            print(f"I won with {fnum_pc} tries")
        else:
            print("Equal!")
        yana = int(input("Do you wanna play again? If Yes(1) or No(0)\n>>>"))
        
    
    