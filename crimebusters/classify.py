# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:31:48 2015

@author: andrew_woizesko
"""

class EventClassifier(object):
    """
    Class that will be used to classify user input
    events. The event classifier will use the model 
    from build.py
    """
    
    def __init__(self, model=None):
        """
        Initialize the event classifier with the model
        created in build.py
        """
        pass
    
    def classify(self):
        """
        This is the function that will take the user 
        input and return the probability that the 
        user will encounter a crime on their trip
        """
        pass
    
    def explain(self):
        """
        Not sure if we'll need this.
        """
        pass
    

if __name__ == "__main__":
    print "Need to code this up!"
    raw_input("\nPress enter to quit.")