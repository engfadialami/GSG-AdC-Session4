import pandas as pd

df_raw = pd.read_csv("data/attacks.csv", encoding="latin1")
print("Raw shape:", df_raw.shape)
print("Columns:", df_raw.columns.tolist())

df_true = df_raw.dropna(how="all")

print("True shape after removing blank rows:", df_true.shape)

df_true.columns = df_true.columns.str.strip()

print("Percentage of null values in 'Age' column:")
print(f"{round(df_true['Age'].isnull().mean() * 100, 2)}% ")
print("Percentage of null values in 'Time' column:")
print(f"{round(df_true['Time'].isnull().mean() * 100, 2)}% ")

print(df_true["Fatal (Y/N)"].unique())

#Let us drop metadata columns that are not useful for analysis
metadata_cols = ["pdf", "href", "href formula", "Case Number.1",
                 "Case Number.2", "original order"]
df_true.drop(columns=metadata_cols, inplace=True)
print(df_true.shape)
