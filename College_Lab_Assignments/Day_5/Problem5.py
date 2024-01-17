"""
5. The sample file student.txt contains one line for each student. The student’s name is the first
entry on each line, followed by some exam scores. The number of scores might be different
for each student. Using the text file student.txt, write a Python script that prints out the
names of students those have a total score more than 500.
"""

with open("student.txt","r") as r:
    text=r.read()
    lines=text.split("\n")
    print("Students who scored more than 500 are: ")
    for i in lines:
        text=i.split()
        marks=text[1:]
        sum=0
        for i in marks:
            sum+=int(i)
        # print(sum)
        if(sum>500):
            print(text[0]," = ",sum,end=", ")