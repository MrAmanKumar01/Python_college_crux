"""
7. Write a script that identifies the longest word(s) in a file and 
output a message that includes the length of the longest word, 
along with all of the words of that length that occurred in the file.
"""

with open('file.txt','w') as fname:
    fname.write("The critic accused the author of excessive sententiousness in his writing")
with open ('file.txt', 'r') as fp:
           content=fp.read().replace('\n',' ')
           l_words=content.split(' ')
fp.close()
l_words.sort(key=lambda x: len(x), reverse=True)
print("Longest word(s) is of length:",len(l_words[0]))
index=0
while(len(l_words[index])==len(l_words[0])):
          print(l_words[index])
          index+=1
