import json
import glob
import os
import argparse
import shutil

def get_paths(input_folder):
    """
    Stores all .txt files in a list
    Returns a list of strings of filepaths from the Text (volumes) folder
    :param inputfolder: inputfolder used in main
    """
    list_files = []
    if not os.path.exists(input_folder):
        print("Input folder does not exist!")
    conll_folder = glob.glob(input_folder + '/*.conll')
    
    for filename in conll_folder:
        list_files.append(filename)

    return list_files

def load_text(txt_path):
    """
    Opens the container en reads the elements(strings)
    Returns a string
    :param txt path: list with filepaths
    """
    with open(txt_path, 'rt', encoding="utf8") as infile:
        content = infile.readlines()

    return content

def process_all_lines(paths):
    """
    given a list of txt_paths
    -process each
    :param paths: list of content volume
    :return: dicts of lists
    """
    return_value = ''
    myDict = dict()
    word_list = []
    ner_list = []
    #strip newline, split on space char and make components for the dictionary
    for i, line in enumerate(paths):
        components = line.split()
        if len(components) > 0:
            word = components[0]
            word_list.append(word)
            try:
                ner = components[1]
            except IndexError as e:
                print(f"Word {word} on line {i} has no label (components: {components})")
                raise e
            ner_list.append(ner)
        else:
            myDict['words'] = word_list
            myDict['ner'] = ner_list
            return_value += json.dumps(myDict) + "\n"
            word_list = []
            ner_list = []
            myDict = dict()

    return return_value

def write_file(json, input_folder, output_folder, text):
    """
    write volumes to new directory
    :param json: json string
    :param input_folder: folder with CONLL files
    :param text: pathname of CONLL file
    """
    #get basename of the path and change extension to json
    base = os.path.basename(text)[:-6]
    json_str = '.json'
    basename = base + json_str
    
    #put in the new directory
    completeName = os.path.join(output_folder, basename)
    #write file to json format
    jsonfile = open(completeName, "w", encoding="utf8")
    jsonfile.write(json)
    jsonfile.close()

def copy_write_file(inputfolder, outputfolder):
    #loop over every pathname and call functions for each path separately
    
    #check if directoy exists, if not make it
    if os.path.exists(outputfolder):
        shutil.rmtree(outputfolder)
    os.makedirs(outputfolder)
    
    txt_path = get_paths(inputfolder)
    for text in txt_path:
        print(f"Processing file: {text}")
        lines = load_text(text)
        try:
            json = process_all_lines(lines)
            write_file(json, inputfolder, outputfolder, text)
        except IndexError as e:
            print("Error with file {}".format(text))
            raise e

def main():
    parser = argparse.ArgumentParser(description='Script for converting files from CoNLL to JSON format.')
    parser.add_argument('--inputfolder', dest='input_folder', required=True, help="Directory with CoNLL files to process")
    parser.add_argument('--outputfolder', dest='output_folder', required=True, help="Name the directory for converted JSON files")

    args = parser.parse_args()
    copy_write_file(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()
