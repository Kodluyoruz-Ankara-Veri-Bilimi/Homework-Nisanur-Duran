# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd   #the data is loaded 
import numpy as np 

class Datainformation:  #information about the data section
    def __init__(self, df):
        self.dataframe = df
        
class Datadescribing:   #data type, size, properties
    def describeData(self):
        print(self.df.describe())
        print(df.head())
        print(df.len())
        print(df.describe())
        print(df.dtypes())
        
 class preprocessing:  #part of transformation,standardization,normalization
        def init(self)    
    def cleaning():   
    def cat_encoding():         
    def fillna():       
    def dummy_encoding():        
    def splitting():       
    def outlier():       
    def scaling():
        
class visualization:  #the part where the data is visualized, graphics
        def _init_(self):
    def boxplot(self):
    def PieChart(self):
    def barplot(self):
    def histogram(self):
    def countplot(self):
    def BubblePlot(self):  
    def scatterplot(self):
    def heatmap(self):
        
class model():   
    
class supervised(model):
    def regression():
    def classification():
        
class unsupervised(model):
    def clustering():

class GridsearchCV(): # results of the model 
