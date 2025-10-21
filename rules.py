import pandas as pd

def check_missing_values(df: pd.DataFrame):
    """Check for missing (NaN) values in the dataset."""
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    return missing.to_dict()

def check_negative_prices(df: pd.DataFrame):
    """Find any records with negative or zero prices."""
    invalid = df[df["price"] <= 0]
    return invalid.to_dict(orient="records")

def check_duplicates(df: pd.DataFrame):
    """Check for duplicate rows in the dataset."""
    duplicates = df[df.duplicated()]
    return duplicates.to_dict(orient="records")
