'''
1.1  Repetition
Write a function called repetition which takes three arguments: 
letters (a list), numberBeforeSwitch (an integer), and numRepetitions (also an integer). 
The function should produce a sequences of letters, one per line, such that calls to
repetition with various parameters, generate the following outputs.
 (Note: There are built in functions that can do this. 
 Please do not use them for the exercise).

'''   
#import os 
#os.chdir('C:\Users\pablo\Documents\GitHub\exercise-3-pabloinsente')
       
def repetition(letters,numberBeforeSwitch,numRepetitions):
    for currentseq in range (numRepetitions):
        for curElt in letters:
            for curRepElem in range(numberBeforeSwitch):
                print curElt    
                
repetition(['A','B'],1,1)
repetition(['A','B'],2,1)
repetition(['A','B'],2,2)
repetition(['A','B','C'],3,1)