import nltk
import pandas as pd
import numpy as np

def merge_txt_files():
    """merge txt files in one file from a directory"""
    
    corpus = sys.argv[1]
    txt = glob.glob(os.path.join(corpus + sys.argv[2]))
    
    with open(sys.argv[3], 'w', errors="ignore") as outfile:
        for fname in txt:
        print(fname)
            with open(fname, errors="ignore") as infile:
                for line in infile:
                    outfile.write(line)

merge_txt_files()

def remove_duplicate_rows():
"""remove all duplicate rows from corpus"""

    with open(sys.argv[4], 'r') as infile, open(sys.argv[5], 'w') as outfile: 
        seen = set()
        for line in infile:
            if line in seen:
                continue  
            seen.add(line)
            outfile.write(line)

remove_duplicate_rows()

def split_train_test():
    """split corpus in randomized train and test set"""

    df = pd.read_csv(sys.argv[6], delimiter = ',')
    msk = np.random.rand(len(df)) <= 0.8

    train = df[msk]
    test = df[~msk]

    train.to_csv(sys.argv[7], sep = ',', index = False)
    test.to_csv(sys.argv[8], sep = ',', index = False)

split_train_test()