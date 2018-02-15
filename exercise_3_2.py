# -*- coding: utf-8 -*-
"""
To do this, we need to generate a list of trials in which some proportion is
 masked and some is not masked. Within each condition, we want the image on
 the left side displayed with some proportion of the time, and on the right the remaining times.

Let's begin by having 2/3 masked trials and 1/3 non-masked trials. 
Within each level of the masking factor, half of the targets should
 be on the left and half on the right. Let's have 5 blocks with each 
 block having all the possible trial types.

The code you write should output to the terminal output that looks
 just like this (that first number is the block number).
"""

#import os 
#os.chdir('C:\Users\pablo\Documents\GitHub\exercise-3-pabloinsente')

#to export output
import sys
orig_stdout = sys.stdout      

#Function
def generateTrials(blocks, maskedT, position):
    for i in range(1,blocks+1):
        for ii in maskedT:
            for iii in position:
                print str(i)+',', str(ii)+',', str(iii)


#print to text file
sys.stdout = open('trialList.txt', 'w') #output file    

#Arguments: number of blocks, list with type of trials, list with positions
generateTrials(5, ['masked','masked','nonmasked'], ['right','left'])

#console back to normal
sys.stdout.close()
sys.stdout=orig_stdout 
    
