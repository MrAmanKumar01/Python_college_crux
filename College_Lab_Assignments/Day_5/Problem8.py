'''
8. Create a script that removes all of the comments from a Python source file and save the 
modified file with a new name.
'''

source=input("Enter name of the python file to remove comments: ")
dest=input("Enter name of the new file to save the modified code: ")

with open(source,"r") as r:
    text=r.readlines()

modified=[]
for i in text:
    line=i.strip()
    if (line.startswith("#") or line.startswith("'''") or line.startswith('"""')):
        continue
    else:
        modified.append(i)

with open(dest,"w") as w:
    w.writelines(modified)