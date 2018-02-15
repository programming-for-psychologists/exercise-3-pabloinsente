# -*- coding: utf-8 -*-
"""
4 - Simply randomizing the enture list messes up the block structure creating 
the possibility that participants will see the same trial multiple times in a row. 
For this part, randomize the trials within each block before printing the list.
@author: pablo
"""
#import os 
#os.chdir('C:\Users\pablo\Documents\GitHub\exercise-3-pabloinsente')

#to export output
import sys
orig_stdout = sys.stdout   

import random
names = open('trialList.txt', 'r').readlines()
blocks = []
start = 0
end = 6
for trials in range (1,6):
   
    seq = names[start:end]
    names_random_block = random.sample(seq, len(seq)) 
    blocks = blocks + names_random_block
    
    start =  start + 6
    end =  end + 6

#print to text file
sys.stdout = open('trialList_random_block.txt', 'w') #output file    
for i in blocks: 
    print i 
#console back to normal
sys.stdout.close()
sys.stdout=orig_stdout 

