# Jupyter Notebook: Data Wrangling and Visualization with Matplotlib - Detailed Explanations

# ------------------------
# 1. Importing Libraries
# ------------------------
import pandas as pd  # For data manipulation and analysis
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For data visualization

# Enable plots to appear in the notebook
%matplotlib inline

# ------------------------
# 2. Creating a Sample Dataset
# ------------------------

# Create a dictionary of data
data = {
    'Date': pd.date_range(start='2025-01-01', periods=10, freq='D'),  # 10 consecutive dates
    'Sales': [200, 220, 250, 270, 300, 320, 310, 330, 360, 400],    # Sales numbers
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']  # Region names
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)
print("Sample Dataset:")
print(df)

# ------------------------
# 3. Inspecting Data
# ------------------------

print("\nFirst 5 rows of dataset:")
print(df.head())  # Show first 5 rows

print("\nDataset info:")
print(df.info())  # Info about columns, types, non-null counts

print("\nSummary statistics:")
print(df.describe())  # Descriptive statistics for numerical columns

# ------------------------
# 4. Handling Missing Data
# ------------------------

# Introduce a missing value
df.loc[2, 'Sales'] = np.nan  # Set Sales for 3rd row to NaN
print("\nDataset with missing value:")
print(df)

# Fill missing values with the mean
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())  # Fill NaN with column mean
print("\nDataset after filling missing values:")
print(df)

# ------------------------
# 5. Sorting Data
# ------------------------

# Sort by Sales in descending order
df_sorted = df.sort_values(by='Sales', ascending=False)  # Sort Sales descending
print("\nData sorted by Sales descending:")
print(df_sorted)

# ------------------------
# 6. Grouping and Aggregation
# ------------------------

# Group by Region and calculate average Sales per Region
df_grouped = df.groupby('Region')['Sales'].mean()  # Mean Sales per Region
print("\nAverage Sales per Region:")
print(df_grouped)

# ------------------------
# 7. Filtering Data
# ------------------------

# Filter rows where Sales > 300
df_filtered = df[df['Sales'] > 300]  # Keep only rows with Sales > 300
print("\nRows where Sales > 300:")
print(df_filtered)

# ------------------------
# 8. Creating New Columns
# ------------------------

# Add a new column 'Sales_diff' showing difference from previous day
df['Sales_diff'] = df['Sales'].diff()  # Difference between current and previous row
print("\nDataset with Sales_diff column:")
print(df)

# ------------------------
# 9. Data Visualization with Matplotlib
# ------------------------

# 9.1 Line Plot
plt.figure(figsize=(8,5))  # Set figure size
plt.plot(df['Date'], df['Sales'], marker='o', color='blue', linestyle='-')  # Line plot of Sales over Date
plt.title('Sales Over Time')  # Title of plot
plt.xlabel('Date')  # X-axis label
plt.ylabel('Sales')  # Y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot

# 9.2 Bar Plot
plt.figure(figsize=(8,5))
df_grouped.plot(kind='bar', color='green')  # Bar plot of average Sales per Region
plt.title('Average Sales by Region')
plt.xlabel('Region')
plt.ylabel('Average Sales')
plt.grid(axis='y')  # Grid only on y-axis
plt.show()

# 9.3 Histogram
plt.figure(figsize=(8,5))
plt.hist(df['Sales'], bins=5, color='orange', edgecolor='black')  # Histogram of Sales
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# 9.4 Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df['Date'], df['Sales'], color='red')  # Scatter plot of Sales vs Date
plt.title('Sales Scatter Plot')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# 9.5 Multiple Lines
plt.figure(figsize=(8,5))
for region in df['Region'].unique():  # Loop over each unique Region
    plt.plot(df[df['Region']==region]['Date'], df[df['Region']==region]['Sales'], marker='o', label=region)
plt.title('Sales by Region Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()  # Show legend
plt.grid(True)
plt.show()

# ------------------------
# 10. Saving Cleaned and Visualized Data
# ------------------------

# Save cleaned DataFrame to CSV file
# df.to_csv('cleaned_sales_data.csv', index=False)  # Save without index
