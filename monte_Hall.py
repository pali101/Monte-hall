# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:58:39 2019

@author: pali101
"""

import random

doors=[0]*3
goatdoors=[0]*2
swap=0      #Number of swap wins
dont_swap=0     #Number of don't-swap wins

x=random.randint(0,2)   #xth door will contain prize
doors[x]="car"
for i in range(0,3):
    if i==x:
       continue
    else:
       doors[i]='goat'
       goatdoors.append(i)
    
choice=int(input("Enter your choice(Door 0, Door 1 or Door 2): "))
door_open=random.choice(goatdoors)      #Open a door that comprises of goat
while door_open==choice:        #Door_open and user choice should not be equal
     door_open=random.choice(goatdoors)
ch = input("Do you want to swap? (y or n): ")
if ch == 'y':
    if doors[choice]=='goat':
        print("You WON")
    else:
        print("You lost")
else:
    if doors[choice]=='goat':
        print("You lost")
    else:
        print("You WON")