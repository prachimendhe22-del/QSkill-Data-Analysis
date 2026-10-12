import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\Desktop\New folder\Qsikl_task1\student_marks.csv")

print("STUDENT MARKS DATA ANALYSIS")
print("-" * 35)

# Step 2: Display the dataset
print("\nStudent Marks Dataset:")
print(df)

# Step 3: Basic data analysis
print("\nDataset Information:")
df.info()

print("\nAverage Marks:")
print(df[["Python", "Java", "Maths"]].mean())

print("\nHighest Marks:")
print(df[["Python", "Java", "Maths"]].max())

print("\nLowest Marks:")
print(df[["Python", "Java", "Maths"]].min())

# Step 4: Bar chart
average_marks = df[["Python", "Java", "Maths"]].mean()

average_marks.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Step 5: Scatter plot
plt.scatter(df["Python"], df["Java"])
plt.title("Python Marks vs Java Marks")
plt.xlabel("Python Marks")
plt.ylabel("Java Marks")
plt.tight_layout()
plt.show()

# Step 6: Heatmap
correlation = df[["Python", "Java", "Maths"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Between Subjects")
plt.tight_layout()
plt.show()

print("\nDATA ANALYSIS COMPLETED SUCCESSFULLY!")