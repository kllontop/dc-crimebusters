# -*- coding: utf-8 -*-
"""
Created on Tue., Feb. 24, 2015

@author: kathleen_llontop
"""
########################################################################
import pandas as pd
import numpy as np
from sklearn import cross_validation

########################################################################
class BuildEventPlanner(object):

	filename = 'CrimeEventsWCensusMetDistAndName.csv'
	
	def __init__(self, filename):
		self.filename = filename
		
	def featureset(self, filename):
		# Produce the test and training sets
		# Read csv file into a structured pandas dataframe
		df = pd.read_csv(filename, sep = ",", quotechar = '"',skipinitialspace = True)

		# For the purpose of using scikit learn functions on this data,
		# tranform dataframe into a numpy array
		df_array = np.array(df)

		## Split data into test and train sets using KFold
		# We can decide on the n and k
		# Setting random_state=0 sets the seed so the splits are reproducible
		# Not sure if we want shuffle = True before splitting
		kf = KFold(n, k, indices = True, random_state=0)
		
		##The featureset output referenced in the train method should then be the train set
	
	def train(self, featureset=None):
        """
        This is where the algorithmn will be trained using
        an input featureset. The data should come from
        self.featureset() but the input parameter 
        allows for reuse.
        """
        featureset = featureset or self.featureset()
        pass
		
	def build(self):
        """
        This is where the class will build the output and write
        to disk likely using pickle. 
        """
        pass
    
    def cross_validate(self):
        """
        A function to test the accuracy of the 
        model.
        """
        pass
    
    def get_output_paths(self):
        """
        function that returns where the model outputs
        are written
        """
        pass
    
    def write_details(self):
        """
        Function to write model stats such as date and runtime.
        """
        pass
    
if __name__ == "__main__":
    print "You need to code first!"
    raw_input("\nPress enter to quit.")
        
		