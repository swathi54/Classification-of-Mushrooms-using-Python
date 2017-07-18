#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:48:28 2017

@author: SwatzMac

@Program: Naive Bayes Classifier algorithm on classifiying Mushroom Dataset 
Purpose: Part of FINAL PROJECT - ML using Python
"""

from math import log
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random
import time

DATASET = '/Users/SwatzMac/Desktop/agaricus-lepiota.data'
ATTRIBUTES = '/Users/SwatzMac/Desktop/agaricus-lepiota.names'

attributes_yes_list = []
attributes_no_list = []

positive_dataset = []
negative_dataset = []

pos_train = []
neg_train = []

training_data = []
test_data = []

g_attributes = [] #doesn't include poisonous or edible columns
g_attributes_dictionary = {}

def prepare_datasets():
    with open(DATASET, 'r+') as dataset_file:
        dataset_lines = dataset_file.readlines()
        
    for line in dataset_lines:
        attributes = line.split(',')

        # Get rid of newline character on last attribute
        attributes[-1] = attributes[-1].strip()

        if attributes[0] == 'e':
            positive_dataset.append((attributes[0], attributes[1:]))
        else:
            negative_dataset.append((attributes[0], attributes[1:]))
        
    while len(positive_dataset) and len(negative_dataset):
        rand_pos = random.randint(0, min(len(positive_dataset),len(negative_dataset))-1)
        training_data.append(positive_dataset.pop(rand_pos))
        training_data.append(negative_dataset.pop(rand_pos))
        
        if len(positive_dataset) and len(negative_dataset):
            rand_pos = random.randint(0, min(len(positive_dataset),len(negative_dataset))-1)
            training_data.append(positive_dataset.pop(rand_pos))
            training_data.append(negative_dataset.pop(rand_pos))

        if len(positive_dataset) and len(negative_dataset):
            rand_pos = random.randint(0, min(len(positive_dataset),len(negative_dataset))-1)
            training_data.append(positive_dataset.pop(rand_pos))
            training_data.append(negative_dataset.pop(rand_pos))

        if len(positive_dataset) and len(negative_dataset):
            rand_pos = random.randint(0, min(len(positive_dataset),len(negative_dataset))-1)
            test_data.append(positive_dataset.pop(rand_pos))
            test_data.append(negative_dataset.pop(rand_pos))
 
            
def parse_attributes():
    with open(ATTRIBUTES, 'r+') as attributes_file:
        #print(attributes_file)
        attributes_lines = attributes_file.readlines()
        #print(attributes_lines)
    for line in attributes_lines:
        print(attributes_lines)
        pair = line.strip().split()
        g_attributes.append(pair[0])
        g_attributes_dictionary[pair[0]] = pair[1].split(',')

#            
#def parse_attributes():
#    attributes_file = pd.read_csv('/Users/SwatzMac/Desktop/labels.csv')
#    print(attributes_file)
##    with open(ATTRIBUTES, 'r+') as attributes_file:
#    attribute_lines = attributes_file.readlines()
##    print (len(attribute_lines))
#    for line in attribute_lines:
#        print (line)
#        pair = line.strip().lower().split(',')
#        print (pair)
#        g_attributes.append(pair[0])
#        g_attributes_dictionary[pair[0]] = pair[1].split(',')
            
def prepare_attribute_lists():
    attr_count = 0
    val_count = 0
    
    for i in range(len(g_attributes)):
        attributes_yes_list.append([])
        attributes_no_list.append([])
        
    for i in attributes_yes_list:
        for j in range(12):
            i.append(0)
    for i in attributes_no_list:
        for j in range(12):
            i.append(0)
    
    for attr in g_attributes:
        val_count = 0
        for value in g_attributes_dictionary[attr]:
            for example in training_data:
                if value == example[1][attr_count] and example[0] == 'e':
                    attributes_yes_list[attr_count][val_count] += 1
            val_count += 1
        attr_count += 1
    attr_count = 0
    
    for attr in g_attributes:
        val_count = 0
        for value in g_attributes_dictionary[attr]:
            for example in training_data:
                if value == example[1][attr_count] and example[0] == 'p':
                    attributes_no_list[attr_count][val_count] += 1
            val_count += 1
        attr_count += 1
    
def naive_bayes(example,neg,pos):
    count = 0
    pos_prob = 1.0
    neg_prob = 1.0
    
    for attr in example:
        pos_prob *= attributes_yes_list[count][g_attributes_dictionary[g_attributes[count]].index(attr)]
        neg_prob *= attributes_no_list[count][g_attributes_dictionary[g_attributes[count]].index(attr)]
           
        count += 1
    if neg_prob > pos_prob: 
        return 'p'
    else:
        return 'e'

if __name__ == '__main__': 
    start = time.time()
    prepare_datasets()
    parse_attributes()
    prepare_attribute_lists()
    print ("done with tables")
    
    num_pos = 0
    num_neg = 0
    
    #correct1 = 0
    for i in training_data: 
        if i[0] == 'e':
            num_pos += 1
            pos_train.append(i[1])
        else:
            num_neg += 1
            neg_train.append(i[1])
#        actual = i[0]
#        calculated = naive_bayes(i[1],num_neg,num_pos)
#        print ("actual: %s classified: %s "%(actual, calculated))
#        if actual == calculated:
#            correct1 += 1
#        
    correct = 0
    
    for ex in test_data:
        actual = ex[0]
        calculated = naive_bayes(ex[1],num_neg,num_pos)
        print ("actual: %s classified: %s "%(actual, calculated))
        if actual == calculated:
            correct += 1
            
    #print ("Percent correct: %f "%(float(correct*100)/float(len(training_data))))            
    print ("Percent correct: %f "%(float(correct*100)/float(len(test_data))))
    print ("Runtime: %s" % (time.time() - start))
    
    
        





                                       
                                        
                                        
                                        
    
    
            
            
            
            
            
            
            
            
            