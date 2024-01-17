""" 
2. Write a Python script to find number of characters, words and lines in a file.
"""

def count_characters_words_lines(file_path):
    # Initialize counters
    character_count = 0
    word_count = 0
    line_count = 0

    # Open the file in read mode
    with open(file_path, "r") as r_file:
        for line in r_file:
            # Count characters
            character_count += len(line.strip())  #used strip() to remove "\n"

            # Count words
            words = line.split()
            word_count += len(words)

            # Count lines
            line_count += 1

    return character_count, word_count, line_count

# Specify the file path
file_path = "prob2.txt"

# Count characters, words, and lines
character_count, word_count, line_count = count_characters_words_lines(file_path)

# Print the results
print("Characters:", character_count)
print("Words:", word_count)
print("Lines:", line_count)