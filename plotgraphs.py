import os
os.getcwd()
os.makedirs("./data",exist_ok=True)
os.chdir("/content/data")

with open("sample_data.csv", "w") as f:
    f.write("ID,Name,Age,Department,Salary\n")
    f.write("1,Ali,25,IT,50000\n")
    f.write("2,Ayesha,28,HR,55000\n")
    f.write("3,Ahmed,30,Finance,60000\n")
    f.write("4,Sara,26,Marketing,52000\n")
    f.write("5,Hassan,32,IT,65000\n")
import pandas as pd

# read the CSV into a DataFrame
df = pd.read_csv("sample_data.csv")

# display it
print(df)
df.plot(x="Name", y="Salary", kind="bar", title="Salary by Employee")
df.plot(x="Age", y="Salary", kind="line", marker="o", title="Age vs Salary")
df["Department"].value_counts().plot(kind="pie", autopct='%1.1f%%', title="Employees per Department")
import matplotlib.pyplot as plt
plt.show()
