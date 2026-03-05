import numpy as np
import pandas as pd

df = pd.read_csv("../data/data.csv")

df.columns = df.columns.str.strip()          # remove spaces
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("(", "")
df.columns = df.columns.str.replace(")", "")


df = df.drop_duplicates()                    # remove duplicate rows
df = df.fillna(df.mean(numeric_only=True))   # fill numeric missing values


df["Year"] = df["Year"].astype(int)

numeric_cols = df.select_dtypes(include=["float64","int64"]).columns
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

df.to_csv("../data/cleaned_data.csv", index=False)

print("Dataset cleaned successfully")