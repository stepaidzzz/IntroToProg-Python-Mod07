# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate pickling and structure error handling
# ChangeLog (Who,When,What):
# SYong,08.30.2022,Created started script for Assignment 07
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
# Declare variables and constants
lstData = []
strName = ()
strJobTitle = ()

# Presentation (Input/Output)  ----------------------------------------------- #
print('Enter the word "Exit" twice to end.')


# Main Body of Script  ------------------------------------------------------- #
while (True):
    strName = input('Please input your name: ')
    strJobTitle = input('Please input your job title: ')
    if strName == 'Exit' or strJobTitle == 'Exit':
        break
    else:
        lstData += [strName + " " + strJobTitle]
        try:
            if strName.isalpha() == False or strJobTitle.isalpha() == False:
                raise Exception('Please restrict your input to alphabets only!')
        except Exception as e:
            print(e)

import pickle  # import pickle to use it. Importing a library.
with open('myData.pickle', 'wb') as f1:
    pickle.dump(lstData, f1)

with open('myData.pickle', 'rb') as f2:
    a = pickle.load(f2)

print(a)    


