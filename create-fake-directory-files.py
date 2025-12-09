# This script creates 1000 fake text files in a specified directory and was used to test fuctionality of Python-DVUploader
import os

# Define the directory where text files will be created
output_directory = "/large-test-directory"

# Create 1000 csv files
for i in range(1000):
    # Creates a sequential unique filename for each file
    filename = f"file_{i:03d}.csv"
    file_path = os.path.join(output_directory, filename)

    # Open the file in write mode and add some content, here we just added some sample text - modify this by adding information between the quotes
    with open(file_path, "w") as f:
        f.write(f"This is the content of {filename}.\n")
        f.write(f"This is line 2 of file number {i}.\n")

# Prints a message indicating completion
print(f"Successfully created 1000 text files in '{output_directory}'")



