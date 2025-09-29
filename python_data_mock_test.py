# Jupyter Notebook: Python & Data Analysis Mock Test

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------
# Part 0: Load Dataset
# ------------------------
df = pd.read_csv("/mnt/data/students_scores.csv")
print("First 5 rows of the dataset:")
df.head()

# ------------------------
# Part 1: Python & Data Wrangling
# ------------------------

# 1. Create a new column 'Average'
df['Average'] = df[['Electronics', 'GEAS', 'Math', 'Communication']].mean(axis=1)
df[['Name', 'Electronics', 'GEAS', 'Math', 'Communication', 'Average']].head()

# 2. Filter female students from Mindanao with Average >= 55
filtered_students = df.loc[(df['Gender'] == 'Female') &
                           (df['Hometown'] == 'Mindanao') &
                           (df['Average'] >= 55),
                           ['Name', 'Track', 'Average']]
filtered_students

# 3. Replace missing scores with mean of that subject
for col in ['Electronics', 'GEAS', 'Math', 'Communication']:
    df[col].fillna(df[col].mean(), inplace=True)
df.head()

# ------------------------
# Part 2: NumPy Analysis
# ------------------------

# 1. Convert subject scores to NumPy array
scores_array = df[['Electronics', 'GEAS', 'Math', 'Communication']].to_numpy()
scores_array[:5]

# 2. Compute overall average score per subject
subject_averages = np.mean(scores_array, axis=0)
subject_averages_dict = {
    'Electronics': subject_averages[0],
    'GEAS': subject_averages[1],
    'Math': subject_averages[2],
    'Communication': subject_averages[3]
}
subject_averages_dict

# 3. Student with highest average
highest_avg_index = np.argmax(df['Average'].to_numpy())
top_student = df.iloc[highest_avg_index][['Name', 'Average']]
top_student

# ------------------------
# Part 3: Visualization
# ------------------------

# 1. Bar chart: average score per track
avg_per_track = df.groupby('Track')['Average'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='Track', y='Average', data=avg_per_track, palette='viridis')
plt.title('Average Score per Track')
plt.ylabel('Average Score')
plt.xlabel('Track')
plt.ylim(0, 100)
plt.savefig('/mnt/data/average_per_track.png')
plt.show()

# 2. Histogram of student average scores
plt.figure(figsize=(8,5))
sns.histplot(df['Average'], bins=10, kde=True, color='skyblue')
plt.title('Histogram of Student Average Scores')
plt.xlabel('Average Score')
plt.ylabel('Count')
plt.xlim(0, 100)
plt.savefig('/mnt/data/average_score_hist.png')
plt.show()

# ------------------------
# Bonus Challenge
# ------------------------

# 1. Students scoring below 50 in any subject
below_50 = df[['Name', 'Electronics', 'GEAS', 'Math', 'Communication']].copy()
for col in ['Electronics', 'GEAS', 'Math', 'Communication']:
    below_50[col] = below_50[col] < 50
students_below_50 = below_50[below_50[['Electronics','GEAS','Math','Communication']].any(axis=1)]
students_below_50

# 2. Heatmap of scores
plt.figure(figsize=(10,6))
sns.heatmap(df[['Electronics', 'GEAS', 'Math', 'Communication']], annot=True, cmap='coolwarm', fmt=".1f")
plt.title("Heatmap of Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Student Index")
plt.show()