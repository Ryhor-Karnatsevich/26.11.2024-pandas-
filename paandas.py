import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
table = pd.read_csv('data.csv',index_col = 0)
#duple = table.drop_duplicates(subset=['Name','Department']) deletes all the duplicates of subset collumns
#print(table['Is_Remote'].value_counts(sort=True,normalize=True)) #gives us the count of all repeated values in the collumn,normalize gives us a proportion of total

#print(table[table['Department'] == 'HR']['Salary'].mean()) gives as mean of all HR salaries
#print(table.groupby('Department')['Salary'].mean()) #better version of previous code
print(table.groupby(['Department','Position']).agg(max,min))
print(table)
