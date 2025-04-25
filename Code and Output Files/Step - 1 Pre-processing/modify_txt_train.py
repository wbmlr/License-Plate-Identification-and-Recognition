import csv
import os

def modify_csv_and_append_to_txt(csv_file_path, txt_file_path):
    # Read the CSV file and store the modified rows
    modified_rows = []
    
    # Read and sort the CSV file
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        sorted_rows = sorted(reader)

        # Modify the first 890 specified rows
        for i, row in enumerate(sorted_rows):
            if i >= 890:  # Stop processing after 890 rows
                break
            
            # Modify the filename if it ends with .jpg
            if row[0].endswith('.jpg'):
                numeric_part = int(row[0].split('.')[0])  # Get the numeric part
                new_filename = f"{numeric_part + 2700:06d}.jpg"  # Add 2700 and format
                modified_row = [new_filename, row[1]]  # Create modified row
                modified_rows.append(modified_row)

    # Delete lines from the text file
    if os.path.exists(txt_file_path):
        with open(txt_file_path, 'r') as txt_file:
            lines = txt_file.readlines()
        
        total_lines = len(lines)
        lines_to_delete = total_lines - 2700  # Calculate how many lines to delete

        # Keep only the first 2700 lines
        if lines_to_delete > 0:
            lines = lines[:2700]  # Keep only the first 2700 lines

        # Write back the remaining lines
        with open(txt_file_path, 'w') as txt_file:
            txt_file.writelines(lines)

    # Append modified rows to the text file
    with open(txt_file_path, 'a') as txt_file:
        for modified_row in modified_rows:
            txt_file.write('\t'.join(modified_row) + '\n')  # Use tab for spacing

# Example usage
csv_file_path = os.path.join(os.getcwd(), "/home/roadrashfifa21/ML/Assignment/scut_data/scut_data_modified/scut_data/Licplatesrecognition_train.csv")
txt_file_path = os.path.join(os.getcwd(), "/home/roadrashfifa21/ML/Assignment/scut_data/scut_data_modified/scut_data/scut_train.txt")

modify_csv_and_append_to_txt(csv_file_path, txt_file_path)