from scipy.stats import entropy
from pathlib import Path
import pathlib
import os
import operator
import shutil
import argparse
import numpy as np

#def calculate_entropy(pk):
#    '''calls the scipy entropy for entropy calculation but does a zero check. Do if there is no entropy at all it returns zero compareable to save division function.'''
#    if len(set(pk)) == 1: #future improvement check if the actual value is 0 as well
#        return 0
#    else:
#        return entropy(pk)

def calculate_mean_for_files(file_name_1, file_name_2):
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    ''' 
    calculates mean for transformer output files
    param: file_name_1 (file name of annotator 1)
    param: file_name_2 (file name of annotator 2)
    
    return means for files, list with differences #returns a tuple
    '''
    pk = []
    with open(file_name_1, "rt") as f_p1:
        with open(file_name_2, "rt") as f_p2:
                for line1 in f_p1:
                    labels1 = line1.split(" ")
                    try:
                        labels2 = f_p2.readline().split(" ")
                    except:
                        print("Getting a line for file 2 fails, probably the files do not align!")

                    lengths = set([len(labels1), len(labels2)
                    if len(lengths) > 1:
                        print("Rows do not align, row is skipped for mean!")
                        break
                    else:
                        length = lengths.pop()
                    
                    for i in range(0, length):
                        
                        labels = set([labels1[i], labels2[i])
                        pk.append(len(labels)-1)
    #return calculate_entropy(pk), pk
    return np.mean(pk)

    
def get_topx_entropy(path1, path2, topx=100):
    '''
    calculates the mean for the files in the selected paths and sub paths
    param: path1 (first path to be used for the entropy calculation)
    param: path2 (second path to be used for the entropy calculation)
    param: path3 (third path to be used for the entropy calculation)
    param: topx=1 (set to 3 gives us the top three files,)
    returns a list (the top x) of filenames with the highest entropy
    '''
    file_mean = {} 
    file_paths = Path(path1).glob('**/test_predictions.txt')
    total_pk = [] #list which will contain the differences over all the files
    for file_path in file_paths:
        file_path1 = str(file_path)
        file_path2 = file_path1.replace(str(Path(path1)), str(Path(path2)))
        #file_path3 = file_path1.replace(str(Path(path1)), str(Path(path3)))

        calculated_mean, pk = calculate_mean_for_files(file_path1, file_path2)
        total_pk = total_pk + pk # appends the difference per file to the total differences
        if calculated_mean > 0:
            parts = file_path1.replace('\\', '/').split('/')
            conll_filename = parts[len(parts) - 2].replace("json", "conll")
            file_mean[conll_filename] = calculated_mean

    sorted_file_mean = sorted(file_mean.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_file_mean)
    top_x_ent = []
    for i in range(0, min(topx, len(sorted_file_mean))):
        top_x_ent.insert(0, sorted_file_mean[i][0])
        
    print(f"Total mean: {calculate_mean(total_pk)}") #prints the total mean over all the differences 
    return top_x_ent 

def copy_topx_mean(path1, path2, data_path, topx_ent_path, topx=100):
    '''
    copy the highest entropy files to the given output path
    param: path1 (first path to be used for the entropy calculation)
    param: path2 (second path to be used for the entropy calculation)
    param: path3 (third path to be used for the entropy calculation)
    param: topx_ent_path (output directory)
    param: topx=3 (top x number of files to select for entropy)
    
    '''
    top_x_ent = get_topx_mean(path1, path2, topx)
    if not os.path.exists(topx_ent_path):
        os.makedirs(topx_ent_path)
    for file_name in top_x_ent:
        shutil.copy(os.path.join(data_path, file_name), os.path.join(topx_ent_path, file_name))
        
def main():
    # See: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Script for entropy calculation and output (transformer predictions files).')
    parser.add_argument('--path1', dest='path1', required=True, help="first path to be used for the mean calculation")
    parser.add_argument('--path2', dest='path2', required=True, help="second path to be used for the mean calculation")
    parser.add_argument('--datapath', dest='data_path', required=True, help="Directory containing (original) dataset")
    parser.add_argument('--entpath', dest='topx_ent_path', required=True, help="Output directory of the top x mean files")
    parser.add_argument('--topx', dest='topx', type=int, default="100", help="Top x number of files to select for mean")
    
    args = parser.parse_args()
    copy_topx_mean(args.path1, args.path2, args.data_path,args.topx_ent_path, args.topx)        
    print("Done mean evaluation.")
    
if __name__ == "__main__":
    main()
