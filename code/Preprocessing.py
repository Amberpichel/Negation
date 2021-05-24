from transformers import AutoTokenizer
import argparse
import random
from random import shuffle
import glob
import os
import time
import shutil
from math import floor

def load_sentences(dataset):
    """
    Load sentences of dataset
    param: dataset (file name) 
    returns a list of a list that are the sentences
    """
    sentences = []

    with open(dataset, "rt") as f_p:
        sentence = []
        for line in f_p:
            sentence.append(line)
            if line == '\n':
                sentences.append(sentence)
                sentence = []
    
    return sentences

def randomize_files(sentences):
    shuffle(sentences)

def write_dataset(outputset, sentences):
    """
    write the dataset to an outputset 
    param: outputset (file name of the file where the sentences are written to)
    param: sentences (outputted sentences)
    """
    with open(outputset, "w") as f_o:
        for sentence in sentences:
            for element in sentence:
                f_o.write(element)

#https://stackoverflow.com/questions/42471570/how-to-split-documents-into-training-set-and-test-set
def get_train_test_sets(sentences):
    """
    Splits the sentences into a training and validation set
    param: sentences (list of list of sentences)
    param: train_percent (the percentage of the sentences, e.g.(80) that will be used for the training set (the remainder is for the validationset e.g.(20)))
    returns a tuple of the trainingset and the validationset
    """
    randomized_sentences = randomize_files(sentences)
    split = 0.8
    split_index = floor(len(randomized_sentences) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    
    return training, testing

def preprocess(data_directory, train_directory, validation_directory):
    """
    Preprocess the data (i.e. segmentize the longer sentences, if necessary by splitting the data on max length of tokens, then it shuffels the sentences per file, and finally split the input into two output folders = 'training' + 'validation')
    param: data_directory (path to the data),
    param: train_directory (path to where the training files are written to), 
    param: validation_directory (path to where the validation files are written to), 
    param: train_percentage (the percentage of the sentences, e.g.(80) that will be used for the training set (the remainder is for the validationset e.g.(20)), 
    param: model_name_or_path (name of transformer model that is used for tokenizing), 
    param: max_len (segment length)
    writes output to the training and validation directories
    """
    #timestamp :):
    tmp_path = "./tmp" + str(round(time.time() * 1000))
    os.mkdir(tmp_path)

    file_paths = glob.glob(os.path.join(data_directory, "x*"))
    for file_path in file_paths:
        file_name = os.path.basename(file_path) 

        sentences = load_sentences(file_path)
        train, validation = get_train_test_sets(sentences)
        
        if not os.path.exists(train_directory):
            os.makedirs(train_directory)
        if not os.path.exists(validation_directory):
            os.makedirs(validation_directory)
        write_dataset(os.path.join(train_directory, file_name), train)
        write_dataset(os.path.join(validation_directory, file_name), validation)

    shutil.rmtree(tmp_path)
                
def main():
    
    dataset = 'Data'
    outputset = 'Output'
    data_directory = 'Documents'
    train_directory = 'Train'
    validation_directory = 'Test'
    
    # See: https://docs.python.org/3/library/argparse.html
    #parser = argparse.ArgumentParser(description='Script for preprocessing conll files.')
    #parser.add_argument('--datadirectory', dest='data_directory', required=True, help="Directory to process")
    #parser.add_argument('--traindirectory', dest='train_directory', required=True, help="Directory to write training data to")
    #parser.add_argument('--validationdirectory', dest='validation_directory', required=True, help="Directory to write validation data to")
    #parser.add_argument('--trainpercentage', dest='train_percentage', type=int, required=True, help="Percentage of data that should be outputted as training")
    #parser.add_argument('--modelname', dest='model_name_or_path', default="bert-base-uncased", help="Model name or location")
    #parser.add_argument('--maxlength', dest='max_len', type=int, help="Maximum segment length")
    
    #args = parser.parse_args()
    #preprocess(args.data_directory, args.train_directory, args.validation_directory, args.train_percentage, args.model_name_or_path, args.max_len)    
    #print("Done preprocessing.")
    
if __name__ == "__main__":
    main()
