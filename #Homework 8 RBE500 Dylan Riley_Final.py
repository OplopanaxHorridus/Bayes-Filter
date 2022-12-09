#Homework 8 RBE500 Dylan Riley 
import numpy as np
import math



#ACTIONS:
    #actions probability for do nothing
    #prob of open, do nothing, is open = 1
    #prob of open, do nothing, is closed = 0
    #prob closed, do nothing, is open = 0
    #prob of closed, do nothing, is closed = 0

    #actions open
    #prob of open, push, is open = 1
    #prob of open, push, is closed = .8
    #prob is closed, push, is open = 0
    #prob of closed, push, is closed = .2

#MEASUREMENTS:
#sense open, is open = .6
#sense open, is closed = .2
#sense closed, is open = .4
#sense closed, is closed = .8  
#do_nothing, open | open, closed
# measurements[1] = [0,0]
#Note for Reader: actions[i] = [open probability, closed probability]
#Note for Reader: measurements[i] = [open probability, closed probability]
previous = 1
actions = np.array(["do_nothing", "open", "do_nothing","open", "do_nothing"])
measurements = np.array(["closed", "closed", "closed", "open", "open"])
def Bayes_Filter(actions, measurements, previous):
    #prediction using actions = 
    #(prob of state)*(initial state belief) + (prob of same state, is opposite)*(is opposite of initial state)
    #previous in open terms, so closed probability is 1 - previous

    previous = 0.5
    for i in actions:
        if i == "do_nothing":
            open_beliefbarisopen = 1*previous + 0*previous
            closed_beliefbarisopen = 1-open_beliefbarisopen
        else: 
            open_beliefbarisopen = 1*previous + 0.8*previous
            closed_beliefbarisopen = 1-open_beliefbarisopen
           
    for i in measurements:
        if i == "open":
            n1 = 1/(open_beliefbarisopen*0.6+closed_beliefbarisopen*0.2)
            updated= open_beliefbarisopen*0.6*n1
            
        else:
            n2 = 1/(open_beliefbarisopen*0.4 + closed_beliefbarisopen*0.8)
            updated= open_beliefbarisopen*0.4*n2 

    previous = updated
    print(previous)
            
Bayes_Filter(actions, measurements, previous)
