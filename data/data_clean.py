import pandas as pd


def clean_data(filepath: str) -> pd.DataFrame:
    """
    Load and clean the US Superstore dataset.

    - Drops 'Row ID' column.
    - Converts 'Order Date' and 'Ship Date' to datetime.
    - Reports number of duplicate rows.

    Returns:
        Cleaned pandas DataFrame.
    """
    df = pd.read_excel(filepath, engine="xlrd")

    # Drop 'Row ID'
    if "Row ID" in df.columns:
        df.drop(columns=["Row ID"], inplace=True)

    # Convert date columns to datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Check for duplicates
    duplicate_count = df.duplicated().sum()
    print(f"Duplicate rows: {duplicate_count}")

    return df


if __name__ == "__main__":
    df_clean = clean_data("US Superstore data.xls")
    df_clean.to_csv("US_Superstore_cleaned.csv", index=False)
