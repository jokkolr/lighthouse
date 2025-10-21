import pandas as pd

def fill_missing_values(df: pd.DataFrame, strategy: str = "mean"):
    """
    Fill missing values in numeric columns using the chosen strategy.
    strategy options: "mean", "median", or "zero"
    """
    for col in df.select_dtypes(include="number").columns:
        if df[col].isnull().sum() > 0:
            if strategy == "mean":
                df[col].fillna(df[col].mean(), inplace=True)
            elif strategy == "median":
                df[col].fillna(df[col].median(), inplace=True)
            elif strategy == "zero":
                df[col].fillna(0, inplace=True)
    return df

def remove_duplicates(df: pd.DataFrame):
    """Remove duplicate rows from the dataset."""
    df.drop_duplicates(inplace=True)
    return df

def correct_negative_prices(df: pd.DataFrame):
    """
    Replace negative or zero prices with NaN for review or recalculation.
    """
    if "price" in df.columns:
        df.loc[df["price"] <= 0, "price"] = pd.NA
    return df
