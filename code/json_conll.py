import json
import glob
import os 
import argparse
import csv

def get_paths(input_folder):
    """
    Stores all .txt files in a list
    Returns a list of strings of filepaths from the Text (volumes) folder
    :param inputfolder: inputfolder used in main
    """
    list_files = []
    conll_folder = glob.glob(input_folder + '/*.json')
    
    for filename in conll_folder:
        list_files.append(filename)

    return list_files

def process_and_write(loaded_dicts, input_folder, output_folder, text):
    """
    Process each CONLL and write to file
    :param paths: content of json file
    :param input_folder: folder with json files
    :param text: pathname of json file
    """
    
    #check if dir exists, if not make one
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    #get basename of path and change extension to '.conll'
    base = os.path.basename(text)[:-5]
    conll_str = '.conll'
    basename = base + conll_str
    
    #add directory with files to the input folder
    complete_name = os.path.join(output_folder, basename)
    
    #open write file
    f = csv.writer(open(complete_name, 'w'), delimiter=(' '))
    
    #for every value in the json dict, add values to list and write list
    for json_dict in loaded_dicts:
        values_list = []
        for key, value in json_dict.items():
            values_list.append(value)
                
        f.writerow(values_list)
        
def main():
    
    parser = argparse.ArgumentParser(description='Script for converting files from JSON to CoNLL format.')
    parser.add_argument('--inputfolder', dest='input_folder', required=True, help="Directory with JSON files to process")
    parser.add_argument('--outputfolder', dest='output_folder', required=True, help="Name the directory for converted CoNLL files")
    
    args = parser.parse_args()
    
    txt_path = get_paths(args.input_folder)
    for text in txt_path:
        loaded_dicts = load_text(text)
        process_and_write(loaded_dicts, args.input_folder, args.output_folder, text)

if __name__ == "__main__":
    main()
