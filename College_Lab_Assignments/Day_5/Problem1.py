"""
1. Write a Python script to copy a text file.
"""

# w_file = open('org.txt','w')
# w_file.write("Apple...Ball...\nCat...\nDog...Elephant...")        
# w_file.close() 

# Specify the source and destination file path
source_file_path = "org.txt"
destination_file_path = "copy.txt"

# Read the entire contents of the source file
with open(source_file_path, "r") as source_file:
    source_file_contents = source_file.read()

# Open the destination file in write mode
with open(destination_file_path, "w") as destination_file:
    for line in source_file_contents:
        destination_file.write(line) 

print("File copied successfully!😎\n")
with open(destination_file_path, "r") as destination_file:
    for x in destination_file:
        print(x.rstrip())