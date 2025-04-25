import os
import csv
import re

def process_text_file_and_generate_csv(text_file_path):
    # Extract the directory path
    input_directory = os.path.dirname(text_file_path)
    
    # Read the entire content of the text file
    with open(text_file_path, 'r') as f:
        lines = f.readlines()
    
    # Prepare to store all data for CSV
    csv_data = {}
    
    # Process each line
    for line in lines[1:]:  # Skip the first line (header)
        # Extract number from filename and content
        match = re.match(r'(\d+)_cropped_\d+\.jpg\s*(.+)', line.strip())
        if not match:
            continue
        
        number = match.group(1)
        content = match.group(2)
        
        # Clean the content - remove non-digit characters
        content = re.sub(r'[^\d]', '', content)
        
        # Skip if no digits remain
        if not content:
            continue
        
        # Prepare rows for this image
        rows = []
        for m in range(1, 8):  # m from 1 to 7
            row_id = f"img_{number}_{m}"
            row_data = {str(i): 0 for i in range(10)}  # Initialize all columns to 0
            row_data['id'] = row_id
            
            # Check if mth character exists
            if m <= len(content):
                n = int(content[m-1])
                row_data[str(n)] = 1
            
            rows.append(row_data)
        
        # Store rows for this image
        csv_data[int(number)] = rows
    
    # Sort the data
    sorted_numbers = sorted(csv_data.keys())
    final_csv_data = []
    for number in sorted_numbers:
        final_csv_data.extend(csv_data[number])
    
    # Write to CSV
    output_filename = 'output.csv'
    columns = ['id'] + [str(i) for i in range(10)]
    
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in final_csv_data:
            writer.writerow(row)
    
    print(f"CSV file '{output_filename}' has been created successfully.")
    print(f"Total number of entries: {len(final_csv_data)}")

# Use the function
text_file_path = '/home/roadrashfifa21/ML/Assignment/ocr_results.txt'
process_text_file_and_generate_csv(text_file_path)