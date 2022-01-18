from gensim.models import KeyedVectors
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import sys
from sklearn.svm import SVC
import csv
from csv import writer
from csv import reader
import gensim
import numpy as np
import gensim.downloader as api
from sklearn.metrics import classification_report

def extract_embeddings_as_features_and_gold(conllfile,word_embedding_model):
    '''
    Function that extracts features and gold labels using word embeddings
    
    :param conllfile: path to conll file
    :param word_embedding_model: a pretrained word embedding model
    :type conllfile: string
    :type word_embedding_model: gensim.models.keyedvectors.Word2VecKeyedVectors
    
    :return features: list of vector representation of tokens
    :return labels: list of gold labels
    '''
    labels = []
    features = []

    conllinput = open(conllfile, 'r')
    csvreader = csv.reader(conllinput, delimiter=',', quotechar='|')
    
    for row in csvreader:
        if len(row) > 1 :
            if row[0] in word_embedding_model:
                #print(row)
                vector = word_embedding_model[row[0]]
            else:
                vector = [0]*100
            
            features.append(vector)
            labels.append(row[-1])
            
    return features, labels

def extract_features_and_labels(trainingfile):
    """Extract features from the Reuters trainingdata
    Extract labels from NER column from Reuters trainingdata"""
    
    data = []
    targets = []
    with open(trainingfile, 'r', encoding='utf8') as infile:
        for line in infile:
            components = line.rstrip('\n').split(',')
            if len(components) > 0:
                token = components[0]
                feature_dict = {'token':token}
                data.append(feature_dict)
                targets.append(components[-1])
    return data, targets

def create_classifier(embedding_features, embedding_targets, modelname):
    """Create classifier, feed it with the training features and labels"""   
    
    modelname == 'Embeddings SVM'
    model = SVC()
    #vec = DictVectorizer()
    model.fit(embedding_features[:1000], embedding_targets[:1000])
    #features_vectorized = vec.fit_transform(train_features)#.toarray()
    #model.fit(features_vectorized, train_targets)
    
    return model#, vec

def get_predicted_and_gold_labels(model, inputdata, word_embedding_model): #outputfile):
    """Make predictions from the test data and write it to an outputfile"""  

    embeddings, gold_labels = extract_embeddings_as_features_and_gold(inputdata, word_embedding_model)
    predictions = model.predict(embeddings)

    return gold_labels, predictions

    
def main(argv=None):
    """Run all the above functions"""    

    trainingfile = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]#'outputfile_emb' + '.csv'

    word_embedding_model = KeyedVectors.load_word2vec_format(sys.argv[4], binary=True, encoding='utf-8')
    print('Vector size =', word_embedding_model.vector_size)
    print('Vocabulary size =', len(word_embedding_model.vocab))

    train_emb, train_labels = extract_embeddings_as_features_and_gold(trainingfile, word_embedding_model)
    
    for modelname in ['Embeddings SVM']:
        ml_model = create_classifier(train_emb, train_labels, modelname)
        predictions, goldlabels = get_predicted_and_gold_labels(ml_model, inputfile, word_embedding_model)
        outfile = open(outputfile, 'w')
        counter = 0
        for line in open(inputfile, 'r'):
            if len(line.rstrip('\n').split()) > 0:
                outfile.write(line.rstrip('\n') + ',' + predictions[counter] + '\n')
                counter += 1
        outfile.close()
        
        data = {'Gold': goldlabels, 'Predicted': predictions}
        df = pd.DataFrame(data, columns=['Gold', 'Predicted'])

        confusion_matrix = pd.crosstab(df['Gold'], df['Predicted'], rownames=['Gold'], colnames=['Predicted'])
        print('matrix:') 
        print(confusion_matrix)
        print()
        
        report = classification_report(goldlabels, predictions, digits = 3)
        print('metrics:')
        print(report)
        
if __name__ == '__main__':
    main()
    