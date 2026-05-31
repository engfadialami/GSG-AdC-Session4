import pandas as pd

def clean_empty_rows(df):
    df = df.copy()
    df = df.dropna(how="all")
    return df
def check_strip(df):
    df = df.copy()
    df.columns = df.columns.str.strip()
    return df
def drop_metadata(df):
    df = df.copy()

    cols_to_drop = [
        "pdf",
        "href",
        "href formula",
        "Case Number.1",
        "Case Number.2",
        "original order"
    ]

    df = df.drop(columns=cols_to_drop)

    return df

# df= pd.read_csv("data/attacks.csv", encoding="latin1")


# df = clean_empty_rows(df)
# df = check_strip(df)
# df = drop_metadata(df)

df = (
    pd.read_csv("data/attacks.csv", encoding="latin1")
    .pipe(clean_empty_rows)
    .pipe(check_strip)
    .pipe(drop_metadata)
)

print(df.shape)
print(df.columns.tolist())




