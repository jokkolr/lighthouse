import pandas as pd
from rules import check_missing_values, check_negative_prices, check_duplicates
from cleaner import fill_missing_values, remove_duplicates, correct_negative_prices

def validate_and_clean(data_path: str, output_path: str):
    """
    Validate the dataset and automatically fix detected issues.
    """
    print(f"🔍 Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)

    print("\n--- VALIDATION REPORT ---")
    missing = check_missing_values(df)
    negatives = check_negative_prices(df)
    duplicates = check_duplicates(df)

    if missing:
        print(f"⚠️ Missing values found: {missing}")
    if negatives:
        print(f"⚠️ Negative prices found in rows: {negatives}")
    if duplicates:
        print(f"⚠️ Duplicate rows detected: {duplicates}")
    if not (missing or negatives or duplicates):
        print("✅ No major issues found!")

    print("\n--- CLEANING PROCESS ---")
    if missing:
        df = fill_missing_values(df)
        print("🧹 Filled missing values using mean strategy.")
    if negatives:
        df = correct_negative_prices(df)
        print("🧽 Corrected negative or zero prices.")
    if duplicates:
        df = remove_duplicates(df)
        print("♻️ Removed duplicate rows.")

    print("\n💾 Saving cleaned dataset...")
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

    return df

# Example usage:
# validate_and_clean("data/sample.csv", "data/cleaned_sample.csv")
