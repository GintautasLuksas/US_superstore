import pandas as pd


def clean_data(filepath: str) -> pd.DataFrame:
    """
    Load and clean the US Superstore dataset.

    - Drops 'Row ID' and 'Country' columns.
    - Converts 'Order Date' and 'Ship Date' to datetime.
    - Reports number of duplicate rows.
    - Displays data types of each column.

    Returns:
        Cleaned pandas DataFrame.
    """
    df = pd.read_excel(filepath, engine="xlrd")

    # Drop unnecessary columns
    for col in ["Row ID", "Country", "Customer Name", "Postal Code"]:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)

    # Convert date columns to datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # Check for duplicates
    duplicate_count = df.duplicated().sum()
    print(f"Duplicate rows: {duplicate_count}")

    # Print column data types
    print("\nColumn data types after cleaning:\n")
    print(df.dtypes)

    return df


if __name__ == "__main__":
    df_clean = clean_data("US Superstore data.xls")
    df_clean.to_csv("US_Superstore_cleaned.csv", index=False)
