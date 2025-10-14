import pandas as pd

#1. extracting
df=pd.read_csv("13-oct-class-1.csv")

#2. transform
df.dropna(inplace=True) #removing rows with missing values
df["Marks"] = df["Marks"].astype(int)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x>=50 else "Fail")

#3. load
df.to_csv("13-oct-class.csv",index=False)

print("Data pipeline completed. cleaned data saved to cleaned_students.csv.")
print("ETL IS DONE")