"""
3. Write a Python script to obtain the line number in a file in which a given word is present.
"""

def find_word_line_number(file_path, word):
    line_number = 0

    with open(file_path, "r") as r_file:
        for line in r_file:
            line_number += 1
            if word in line:
                return line_number

    # return None

# Specify the file path and word to search for
file_path = "prob3.txt"
word = input("Enter a word: ")

# Find the line number where the word is present
line_number = find_word_line_number(file_path, word)

if line_number:
    print("Word '{}' found on line: {}".format(word, line_number))
else:
    print("Word '{}' not found in the file".format(word))