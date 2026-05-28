import pandas as pd

def clean_data():
    df = pd.read_csv("data/job_market_data.csv")

    print("=== RAW DATA INFO ===")
    print(f"Shape: {df.shape}")
    print(f"Null values:\n{df.isnull().sum()}")
    print(f"Duplicates: {df.duplicated().sum()}")

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Fill any nulls
    df.fillna("Unknown", inplace=True)

    # Standardize text columns
    for col in ["Job Title", "Company", "City", "Experience Level", "Industry", "Remote"]:
        df[col] = df[col].str.strip().str.title()

    # Salary as float
    df["Salary (LPA)"] = pd.to_numeric(df["Salary (LPA)"], errors="coerce")
    df.dropna(subset=["Salary (LPA)"], inplace=True)

    df.to_csv("data/cleaned_job_data.csv", index=False)
    print(f"\n=== CLEANED DATA ===")
    print(f"Shape after cleaning: {df.shape}")
    print("Saved to data/cleaned_job_data.csv")
    return df

if __name__ == "__main__":
    clean_data()
