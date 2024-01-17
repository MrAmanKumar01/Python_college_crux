"""
6. Write a Python script that reads lines from a file, adds line numbers to them, and then
stores the numbered lines into a new file. The name of the input file and also the new file
will be read from the user. Each line in the output file should begin with the line number,
followed by a colon and a space, followed by the line from the input file.
"""
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

with open(input_file, 'r') as r_input_file:
  input_file_contents = r_input_file.read()

with open(output_file, 'w') as w_output_file:
    linenum = 0
    for line in input_file_contents.splitlines():
        linenum += 1
        line = str(linenum) + ': ' + line.strip() + '\n'
        w_output_file.write(line)