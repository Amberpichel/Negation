import random
from random import shuffle
import glob
import os
import time
from math import floor
import csv

def get_paths(data_directory):
    """
    Stores all .txt files in a list
    Returns a list of strings of filepaths from the Text (volumes) folder
    :param inputfolder: inputfolder used in main
    """
    list_files = []
    conll_folder = glob.glob(data_directory + '/*')
    
    for filename in conll_folder:
        list_files.append(filename)

    return list_files

def randomize_files(list_files):
    shuffled_list = random.sample(list_files, len(list_files))
    
    return shuffled_list

#https://stackoverflow.com/questions/42471570/how-to-split-documents-into-training-set-and-test-set
def get_train_test_sets(shuffled_list):
    """
    Splits the sentences into a training and validation set
    param: sentences (list of list of sentences)
    param: train_percent (the percentage of the sentences, e.g.(80) that will be used for the training set (the remainder is for the validationset e.g.(20)))
    returns a tuple of the trainingset and the validationset
    """
    split = 0.8
    split_index = floor(len(shuffled_list) * split)
    training = shuffled_list[:split_index]
    testing = shuffled_list[split_index:]
    
    return training, testing

def preprocess(training, testing):
    """
    Preprocess the data (i.e. segmentize the longer sentences, if necessary by splitting the data on max length of tokens, then it shuffels the sentences per file, and finally split the input into two output folders = 'training' + 'validation')
    param: data_directory (path to the data),
    param: train_directory (path to where the training files are written to), 
    param: validation_directory (path to where the validation files are written to), 
    writes output to the training and validation directories
    """ 
    train_directory = 'Train'
    validation_directory = 'Test'
    
    if not os.path.exists(train_directory):
        os.makedirs(train_directory)
    if not os.path.exists(validation_directory):
        os.makedirs(validation_directory)
        
    for element_train in training:
        base = os.path.basename(element_train)
        conll_str_train = '.conll'
        basename = base + conll_str_train
        with open (os.path.join(train_directory, basename), "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(basename) 
    
    for element_test in testing:
        base = os.path.basename(element_test)
        conll_str_test = '.conll'
        basename = base + conll_str_test  
        with open (os.path.join(validation_directory, basename), "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(basename) 
                
def main():
    
    data_directory = '/data/homedirs/amber/Data_Amber'
    
    paths = get_paths(data_directory)
    training, testing = get_train_test_sets(paths)
    pre = preprocess(training, testing)

main()  
