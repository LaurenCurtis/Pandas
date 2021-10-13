from os import access
import pandas as pd 

#keys become columns and values become rows
grades_dict = {'Wally': [87,96,70], 
                'Eva':  [100,87,90],
                'Sam':  [94,77,90],
                'Katie':[100,81,82],
                'Bob':  [83,65,85]}

grades = pd.DataFrame(grades_dict)
grades.index = ['Test 1','Test 2', 'Test 3']
print(grades)
"""
#each column is a series (1 dimensional)
print(grades['Eva'])
print(grades.Sam)
print(grades.loc['Test 2'])
print(grades.iloc[1])

#consecutive
print(grades.loc['Test 1':'Test 3'])
print(grades.iloc[0:3])

#nonconsecutive 
print(grades.loc[['Test 1','Test 3']])
print(grades.iloc[[0,2]])

#view only eva and katy for test 1 and 2 
print(grades.loc['Test 1':'Test 2',['Eva','Katie']])

#view only dame thru bobs grades for test1 and test2 
print(grades.loc[['Test 1', 'Test 3'],'Sam':'Bob'])

grades_A = grades[grades >= 90]
print(grades_A)

grades_B = [(grades>=80) & (grades <90)]
print(grades_B)

gradesA_B = [(grades>= 90) | (grades>=80)]
print(gradesA_B)
"""

pd.set_option('precision',2)
print(grades.describe())

print(grades.sort_index(ascending=False))

print(grades.sort_index(axis = 1, ascending = False))

print(grades.sort_values(by='Test 1', axis = 1, ascending = False))

print(grades.T.sort_values(by='Test 1', ascending=False))