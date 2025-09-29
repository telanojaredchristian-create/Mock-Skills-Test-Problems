# Jupyter Notebook: Pandas Basics - Detailed Explanations with Examples and Comments

# ------------------------
# 1. Importing Pandas
# ------------------------
import pandas as pd  # Import pandas library as 'pd' for convenience

# ------------------------
# 2. Creating Series
# ------------------------

# Series from a list
data = [10, 20, 30, 40]
series1 = pd.Series(data)  # Create a pandas Series
print("Series from list:")
print(series1)  # Print the Series with default index 0,1,2...

# Series with custom index
series2 = pd.Series(data, index=['a', 'b', 'c', 'd'])
print("\nSeries with custom index:")
print(series2)

# Series from dictionary
data_dict = {'Alice': 25, 'Bob': 30, 'Cathy': 22}
series3 = pd.Series(data_dict)  # Keys become index, values become data
print("\nSeries from dictionary:")
print(series3)

# Access elements
print("\nAccess element at index 'b':", series2['b'])  # Access element using index label
print("Access first element:", series1[0])  # Access using integer position

# ------------------------
# 3. Creating DataFrames
# ------------------------

# DataFrame from dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Cathy', 'David'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)  # Create DataFrame
print("DataFrame from dictionary of lists:")
print(df)

# DataFrame from list of dictionaries
data_list = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30},
    {'Name': 'Cathy', 'Age': 22}
]
df2 = pd.DataFrame(data_list)
print("\nDataFrame from list of dictionaries:")
print(df2)

# ------------------------
# 4. Viewing Data
# ------------------------

print("\nFirst 2 rows of DataFrame:")
print(df.head(2))  # View first 2 rows

print("\nLast 2 rows of DataFrame:")
print(df.tail(2))  # View last 2 rows

print("\nDataFrame info:")
print(df.info())  # Information about columns, non-null counts, and dtypes

print("\nDataFrame description (numerical columns):")
print(df.describe())  # Statistical summary of numerical columns

# ------------------------
# 5. Selecting Data
# ------------------------

# Select single column
print("\nSelect 'Name' column:")
print(df['Name'])  # Returns a Series

# Select multiple columns
print("\nSelect 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])  # Returns a DataFrame

# Select rows by index position
print("\nSelect first row:")
print(df.iloc[0])  # iloc for integer-location based indexing

# Select rows by label (if index is set)
df_indexed = df.set_index('Name')  # Set 'Name' as index
print("\nSelect row by index label 'Bob':")
print(df_indexed.loc['Bob'])  # loc for label-based indexing

# ------------------------
# 6. Filtering Data
# ------------------------

# Filter rows where Age > 25
print("\nRows where Age > 25:")
print(df[df['Age'] > 25])

# Filter with multiple conditions (Age > 22 and City is 'Chicago')
print("\nRows where Age > 22 and City is 'Chicago':")
print(df[(df['Age'] > 22) & (df['City'] == 'Chicago')])

# ------------------------
# 7. Adding and Modifying Columns
# ------------------------

# Add new column 'Salary'
df['Salary'] = [50000, 60000, 45000, 52000]  # Adding a new column
print("\nDataFrame with 'Salary' column:")
print(df)

# Modify existing column (increase Salary by 10%)
df['Salary'] = df['Salary'] * 1.1  # Update values
print("\nUpdated Salary by 10%:")
print(df)

# ------------------------
# 8. Dropping Columns or Rows
# ------------------------

# Drop column 'City'
df_drop_col = df.drop('City', axis=1)  # axis=1 for columns
print("\nDataFrame after dropping 'City' column:")
print(df_drop_col)

# Drop row by index
df_drop_row = df.drop(0, axis=0)  # axis=0 for rows
print("\nDataFrame after dropping first row:")
print(df_drop_row)

# ------------------------
# 9. Sorting Data
# ------------------------

# Sort by Age ascending
print("\nSort by Age ascending:")
print(df.sort_values(by='Age'))

# Sort by Salary descending
print("\nSort by Salary descending:")
print(df.sort_values(by='Salary', ascending=False))

# ------------------------
# 10. Grouping Data
# ------------------------

# Group by City and get mean Age
print("\nGroup by City and calculate mean Age:")
print(df.groupby('City')['Age'].mean())

# ------------------------
# 11. Handling Missing Data
# ------------------------

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Cathy', None],
    'Age': [25, None, 22, 28],
    'Salary': [50000, 60000, None, 52000]
})
print("\nDataFrame with missing values:")
print(df_missing)

# Drop rows with any missing values
print("\nDrop rows with missing values:")
print(df_missing.dropna())

# Fill missing values
print("\nFill missing Age with 0:")
print(df_missing.fillna({'Age': 0}))

# ------------------------
# 12. Basic Statistical Operations
# ------------------------

print("\nMean Age:", df['Age'].mean())
print("Maximum Salary:", df['Salary'].max())
print("Minimum Salary:", df['Salary'].min())
print("Sum of Salary:", df['Salary'].sum())

# ------------------------
# 13. Reading and Writing CSV Files
# ------------------------

# Reading a CSV file (example path: 'data.csv')
# df_csv = pd.read_csv('data.csv')  # Read CSV into DataFrame

# Writing DataFrame to CSV file
# df.to_csv('output.csv', index=False)  # Save DataFrame to CSV without index
