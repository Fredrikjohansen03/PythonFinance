# 8pandas.ipynb

### Part2 - applications

# 13 Pandas
# reference: https://www.w3schools.com/python/pandas/default.asp
# reference: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf


#import packages
import pandas as pd

import matplotlib.pyplot as plt

# 8.1 import the csb file Credit.csv into a pandas dataframe Credit using the read_csv() function in the pandas package
# TODO: Write your code below
Credit = pd.read_csv('Credit.csv')

# 8.2 print the top 10 rows in Credit using the head() function of pandas
# TODO: Write your code below
print(Credit.head(10))

# 8.3 print information about Credit using the info() function of pandas.
# TODO: Write your code below
print(Credit.info())

# 8.4 using the shape attribute of pandas, print the number of rows and columns in Credit
# HINT: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# TODO: Write your code below
print("Number of rows and columns:", Credit.shape)

# 8.5 if any, drop rows with missing values from the Credit dataframe
# TODO: Write your code below
Credit_cleaned = Credit.dropna()

# 8.6 Calculate correlation coefficients between the numeric columns in Credit using the corr() function in pandas
# TODO: Write your code below
correlation_matrix = Credit.corr()
print(correlation_matrix)

# 8.7 Grouped by student, calculate the sum of Balance and average of Balance
# HINT: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# TODO: Write your code below
balance_sum = Credit.groupby('Student')['Balance'].sum()
balance_avg = Credit.groupby('Student')['Balance'].mean()

print("Sum of Balance grouped by Student:\n", balance_sum)
print("Average of Balance grouped by Student:\n", balance_avg)

# 8.8 Using the plot() function in pandas, plot a histogram of Balance
# HINT: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# TODO: Write your code below
Credit['Balance'].plot(kind='hist', title='Balance Histogram')
plt.xlabel('Balance')
plt.show()

# 8.9 Using the plot() function in pandas, draw a scatterplot of Income vs. Balance
# HINT: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# TODO: Write your code below
Credit.plot(kind='scatter', x='Income', y='Balance', title='Income vs. Balance')
plt.show()
