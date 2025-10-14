import pandas as pd
from datetime import datetime

def run_pipeline():
    df=pd.read_csv("customers.csv")

    def categorize_age(age):
        if age<30:
            return "Young"
        elif 30<= age <50:
            return "Adult"
        elif age>=58:
            return "Senior"
        else:
            return None

    df["AgeGroup"] = df["Age"].apply(categorize_age)
    df_filtered = df[df["Age"]>=28]
    df_filtered.to_csv("filtered_customers.csv",index=False)
    print(f"Pipeline completed at {datetime.now()}")
    print("Output saved to filtered_customers.csv")


if __name__ == "__main__":
    run_pipeline()