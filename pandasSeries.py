import pandas as pd 
"""
grades = pd.Series([87,100,94])
print(grades[0])
print(grades.describe())

grades2 = pd.Series(98.6, range(3))
#print(grades2)

grades3 = pd.Series([87,100,94], index = ['Wally','Eva','Sam'])
print(grades3)

#using a dictionary keys become index and value are the value
grades4 = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})
print(grades4['Eva'])
print(grades4.Wally)
print(grades4.dtype)
print(type(grades4.values))
"""

hardware = pd.Series(['hammer', 'Saw', 'Wrench'])
print(hardware.str.contains('a'))
print(hardware.str.upper())
