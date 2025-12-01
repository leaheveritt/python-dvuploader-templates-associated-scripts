import os

# Define the directory where text files will be created
output_directory = "C:/Users/LEveritt/Documents/GitHub/dvuploader-test/large-test-directory"

# Create 1000 csv files
for i in range(1000):
    # Create a unique filename with zero-padding for sorting
    filename = f"file_{i:03d}.csv"
    file_path = os.path.join(output_directory, filename)

    # Open the file in write mode and add some content
    with open(file_path, "w") as f:
        f.write(f"This is the content of {filename}.\n")
        f.write(f"This is line 2 of file number {i}.\n")

print(f"Successfully created 1000 text files in '{output_directory}'")



