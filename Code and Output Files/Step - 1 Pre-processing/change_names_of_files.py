import os

# Specify the directory containing the files
directory = '/home/roadrashfifa21/ML/Assignment/scut_data/scut_data_modified/scut_data/scut_train'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') and len(filename[:-4]) == 4:  # Check for exactly 4 characters before '.jpg'
        # Extract the number from the filename
        number = int(filename[:-4])  # Get the number part
        
        # Create the new filename with leading zeros
        new_filename = f"{number:06}.jpg"  # Change to 6 digits
        
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)

print("Files renamed successfully.")