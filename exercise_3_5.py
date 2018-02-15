# -*- coding: utf-8 -*-
"""
5 - Double the number of trials in each block (so that the repetitions are not
 quite so predictable), and then randomize within each block as in part 4.
"""

#import os 
#os.chdir('C:\Users\pablo\Documents\GitHub\exercise-3-pabloinsente')

"""Double Trials"""

#to export output
import sys
orig_stdout = sys.stdout

#duplicate trials           
def generateTrials(blocks, maskedT, position):
    for i in range(1,blocks+1):
        for ii in maskedT:
            for iii in position:
                print str(i)+',', str(ii)+',', str(iii)

sys.stdout = open('trialListDouble.txt', 'w') #output file
generateTrials(5, ['masked','masked','nonmasked']*2, ['right','left'])

#console back to normal
sys.stdout.close()
sys.stdout=orig_stdout 


"""Double Trials /  randomize within each block"""

#to export output
import sys
orig_stdout = sys.stdout

#randomize within blocks for new trial list (double)
import random
import os 
os.chdir('C:\Users\pablo\Documents\GitHub\exercise-3-pabloinsente')
names = open('trialListDouble.txt', 'r').readlines()
blocks = []
start = 0
end = 12
for trials in range (1,6):
   
    seq = names[start:end]
    names_random_block1 = random.sample(seq, len(seq)) 
    blocks = blocks + names_random_block1
    
    start =  start + 12
    end =  end + 12

#print to text file
sys.stdout = open('trialListDoubleRandom.txt', 'w') #output file    
for i in blocks: print i 

#console back to normal
sys.stdout.close()
sys.stdout=orig_stdout 
    
