import pandas as pd


def show_unique_counts(filepath: str) -> None:
    """
    Load a cleaned dataset, parse date columns, display data types,
    and show the number of unique values per column.
    """
    df = pd.read_csv(filepath, parse_dates=["Order Date", "Ship Date"])

    print("\nColumn data types:\n")
    print(df.dtypes)

    unique_counts = df.nunique()
    print("\nUnique value counts per column:\n")
    print(unique_counts)


if __name__ == "__main__":
    show_unique_counts("US_Superstore_cleaned.csv")
