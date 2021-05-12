from scipy.stats import entropy
import glob
import os
import operator
import shutil
import argparse

def get_label(line):
    '''
    replace new line with space
    param: line (line in file)
    return label or an empty string
    '''
    line = line.replace("\n", "")
    if line.find(" ") != -1:
        return line.split(" ")[1]
    else:
        return ""

def calculate_entropy(file_name_1, file_name_2, file_name_3):
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
    ''' 
    calculates entropy
    param: file_name_1 (file name of annotator 1)
    param: file_name_2 (file name of annotator 2)
    param: file_name_3 (file name of annotator 3)
    
    return entropy (sequence)
    '''
    pk = []
    with open(file_name_1, "rt") as f_p1:
        with open(file_name_2, "rt") as f_p2:
            with open(file_name_3, "rt") as f_p3:
                for line1 in f_p1:
                    label1 = get_label(line1)
                    try:
                        label2 = get_label(f_p2.readline())
                        label3 = get_label(f_p3.readline())
                    except:
                        print("Getting an label for file 2 or 3 fails, probably the files do not align")
                    labels = set([label1, label2, label3])
                    pk.append(len(labels)-1)

    if len(set(pk)) == 1:
        return 0
    else:
        return entropy(pk)
    
def get_topx_entropy(path1, path2, path3, topx=3):
    '''
    calculates the entropy for the files in the selected paths 
    param: path1 (first path to be used for the entropy calculation)
    param: path2 (second path to be used for the entropy calculation)
    param: path3 (third path to be used for the entropy calculation)
    param: topx=1 (set to 3 gives us the top three files,)
    returns a list (the top x) of filenames with the highest entropy
    '''
    file_entropy = {} 
    file_paths = glob.glob(os.path.join(path1, "*.conll"))
    for file_path in file_paths:
        file_name = os.path.basename(file_path) 
        calculated_entropy = calculate_entropy(os.path.join(path1, file_name), os.path.join(path2, file_name), os.path.join(path3, file_name))
        file_entropy[file_name] = calculated_entropy

    sorted_file_entropy = sorted(file_entropy.items(), key=operator.itemgetter(1), reverse=True)
    top_x_ent = []
    for i in range(0, min(topx, len(sorted_file_entropy))):
        top_x_ent.insert(0, sorted_file_entropy[i][0])
    return top_x_ent

def copy_topx_entropy(path1, path2, path3, data_path, topx_ent_path, topx=3):
    '''
    copy the highest entropy files to the given output path
    param: path1 (first path to be used for the entropy calculation)
    param: path2 (second path to be used for the entropy calculation)
    param: path3 (third path to be used for the entropy calculation)
    param: topx_ent_path (output directory)
    param: topx=3 (top x number of files to select for entropy)
    
    '''
    top_x_ent = get_topx_entropy(path1, path2, path3, topx)
    if not os.path.exists(topx_ent_path):
        os.makedirs(topx_ent_path)
    for file_name in top_x_ent:
        shutil.move(os.path.join(data_path, file_name), os.path.join(topx_ent_path, file_name))
        
def main():
    # See: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Script for entropy calculation and output.')
    parser.add_argument('--path1', dest='path1', required=True, help="first path to be used for the entropy calculation")
    parser.add_argument('--path2', dest='path2', required=True, help="second path to be used for the entropy calculation")
    parser.add_argument('--path3', dest='path3', required=True, help="third path to be used for the entropy calculation")
    parser.add_argument('--datapath', dest='data_path', required=True, help="Directory containing (original) dataset")
    parser.add_argument('--entpath', dest='topx_ent_path', required=True, help="Output directory of the top x entropy files")
    parser.add_argument('--topx', dest='topx', type=int, default="3", help="Top x number of files to select for entropy")
    
    args = parser.parse_args()
    copy_topx_entropy(args.path1, args.path2, args.path3, args.data_path,args.topx_ent_path, args.topx)        
    print("Done entropy evaluation.")
    
if __name__ == "__main__":
    main()
