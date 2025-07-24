import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("accident_prediction_india.csv")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Column names
print("\nColumns:")
print(df.columns)

# Optional: Plot accidents by state (if there's a 'State/UT' column)
if 'State Name' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='State Name', order=df['State Name'].value_counts().index)
    plt.xticks(rotation=90)
    plt.title("Number of Accidents by State/UT")
    plt.tight_layout()
    plt.show()
