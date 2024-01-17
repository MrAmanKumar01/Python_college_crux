"""
6. Write a Python script that reads lines from a file, adds line numbers to them, and then
stores the numbered lines into a new file. The name of the input file and also the new file
will be read from the user. Each line in the output file should begin with the line number,
followed by a colon and a space, followed by the line from the input file.
"""

with open('text3.txt','w') as w_file:
    w_file.write("I am student of PG.\nI am pursuing MCA.")
with open('text4.txt','w') as w_newFile:
   with open('text3.txt','r') as w_file:
       linenum=0
       for line in w_file:
           linenum+=1
           line=str(linenum)+': '+ line
           w_newFile.write(line)