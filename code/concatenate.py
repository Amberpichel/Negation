import argparse
import glob
import os
import shutil

# Inspired on: https://stackoverflow.com/questions/17749484/python-script-to-concatenate-all-the-files-in-the-directory-into-one-file
def concatenate_files(input_folder, output_filename, file_filter="*.*", header=None, footer=None):
    """
    concatenate files in a specific folder into one file 
    param: input_folder (specific folder of the files that need to be concatenated), 
    param: output_filename (concatenated file), 
    param: file_filter (optional parameter by default all files (*.*) are processed but this can be altered), 
    param: header (optional parameter, if needed: Header to be inserted before every file"), 
    param: footer (optional parameter, if needed: Footer to be inserted after every file")
    writes the concatenated file to the output_filename
    """
    glob_query = os.path.join(input_folder, file_filter)
    with open(output_filename, 'w') as out_file:
        for file_name in glob.glob(glob_query):
            if file_name == output_filename:
                # don't want to copy the output into the output
                continue
            else:
                with open(file_name, 'r') as read_file:
                    if header is not None:
                        out_file.write(header)
                    shutil.copyfileobj(read_file, out_file)
                    if footer is not None:
                        out_file.write(footer)

def main():
    # See: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Script for merging files in a folder to a single file.')
    
    parser.add_argument('--inputfolder', dest='input_folder', required=True, help="Directory to process")
    parser.add_argument('--outputfilename', dest='output_filename', required=True, help="File to output to")
    parser.add_argument('--file_filter', dest='file_filter', default="*.*", help="Filter to select the files (glob)")
    parser.add_argument('--header', dest='header', default=None, help="Header to be inserted before every file")
    parser.add_argument('--footer', dest='footer', default=None, help="Footer to be inserted after every file, use [[newline]] for a newline character")
    
    args = parser.parse_args()
    if args.footer == "[[newline]]":
        args.footer = "\n"
    concatenate_files(args.input_folder, args.output_filename, args.file_filter, args.header, args.footer)    
    print("Done concatenating files.")
    
if __name__ == "__main__":
    main()