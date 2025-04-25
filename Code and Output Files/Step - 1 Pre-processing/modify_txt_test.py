import os
import re

def natural_sort_key(s):
    # Split the string into a list of strings and numbers
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def prepend_sorted_last_10_lines(csv_file_path, txt_file_path):
    # Read all lines from the CSV file
    with open(csv_file_path, 'r') as csv_file:
        lines = csv_file.readlines()

    # Sort the lines in natural order
    sorted_lines = sorted(lines, key=natural_sort_key)

    # Get the last 10 lines from the sorted list
    last_10_lines = sorted_lines[-10:]

    # Read the existing content of the text file
    with open(txt_file_path, 'r') as txt_file:
        original_content = txt_file.readlines()

    # Write the last 10 sorted lines followed by the original content back to the text file
    with open(txt_file_path, 'w') as txt_file:
        txt_file.writelines(last_10_lines + original_content)

# Example usage
csv_file_path = os.path.join(os.getcwd(), "/home/roadrashfifa21/ML/Assignment/scut_data/scut_data_modified/scut_data/Licplatesrecognition_train.csv")
txt_file_path = os.path.join(os.getcwd(), "/home/roadrashfifa21/ML/Assignment/scut_data/scut_data_modified/scut_data/scut_test.txt")

prepend_sorted_last_10_lines(csv_file_path, txt_file_path)