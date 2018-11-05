

import textwrap

 # select the file   
filepath = ("texto.txt") 

# open de file
with open(filepath) as t:
    file_data = t.read()

#wrap the text
texto = textwrap.wrap(file_data, width=40)

#print each line
for element in texto:
    print(element)
    


