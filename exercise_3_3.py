# -*- coding: utf-8 -*-
"""
3 - The trial list above has the trial structure you want, but obviously you wouldn't
 want to show someone trials in this order because it's completely predictable. 
 It's a good idea to have your generate trials routine do all the randomization
 ahead of time such that your trials file (here, trialList.txt) contains the 
 exact trial order that will be seen by a participant. There are two reasons. 
 First, this lets you modularize all the trial handling outside of your main experiment 
 script. Second, it allows you to save individual trial files that show the 
 trial order seen by a given participant. It comes in handy for making 
 sure your trial list is set up as you want it. So: let's go ahead and 
 randomize the trial list before printing.
 """
 
#import os 
#os.chdir('C:\Users\pablo\Documents\GitHub\exercise-3-pabloinsente')
 
#to export output
import sys
orig_stdout = sys.stdout     

import random

names = open('trialList.txt', 'r').readlines()
names_random = random.sample(names, len(names)) 
#print to text file
sys.stdout = open('trialList_random.txt', 'w') #output file   
for i in names_random: print i  
#console back to normal
sys.stdout.close()
sys.stdout=orig_stdout 
    
    
