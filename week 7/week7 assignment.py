
#  Assignment: Data Analysis & Visualization with Pandas and Matplotlib


# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


                                # Task 1: Load and Explore Dataset

try:
    # Option 1: Load from CSV file
    # df = pd.read_csv("your_dataset.csv")

    # Option 2: Use built-in sklearn Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame  # convert to pandas DataFrame

    print(" Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: Dataset file not found. Please check the file path.")

# Display first few rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Explore structure
print("\nDataset Info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# Clean missing values (if any)
df = df.dropna()


                            # Task 2: Basic Data Analysis

print("\n Statistical Summary:")
print(df.describe())

# Group by species and compute average of numerical columns
grouped = df.groupby("target").mean()
print("\nAverage measurements by species:")
print(grouped)

# Interesting pattern example:
# Observation: Some species have clearly distinct petal length/width values.


                          # Task 3: Data Visualizations

# 1. Line Chart (Example: Sepal Length trends)
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal length (cm)'], label="Sepal Length", color="blue")
plt.title("Line Chart - Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (Average petal length by species)
plt.figure(figsize=(7,5))
grouped['petal length (cm)'].plot(kind="bar", color="orange")
plt.title("Bar Chart - Avg Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram (Distribution of sepal width)
plt.figure(figsize=(7,5))
plt.hist(df['sepal width (cm)'], bins=20, color="green", edgecolor="black")
plt.title("Histogram - Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Sepal length vs Petal length)
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="target", palette="Set1")
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()


# Findings / Observations

# - Petal length is the strongest feature separating species.
# - Sepal width has a fairly normal distribution.
# - Species 0 generally has smaller petal length compared to species 1 and 2.
# - Clear clustering is visible between species in scatter plot (useful for classification).
