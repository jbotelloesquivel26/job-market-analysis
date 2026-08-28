import pandas as pd

# File Paths
input_path = "data/raw/postings.csv"
output_path = "data/processed/postings_cleaned.csv"

chunk_size = 20000

# Columns Needed for Analysis
columns_to_keep = [
    "job_id",
    "company_name",
    "title",
    "min_salary",
    "med_salary",
    "max_salary",
    "pay_period",
    "location",
    "company_id",
    "views",
    "remote_allowed",
    "formatted_work_type",
    "formatted_experience_level",
    "original_listed_time",
    "listed_time",
    "expiry",
    "sponsored",
    "currency",
    "compensation_type",
    "normalized_salary"
]

date_columns = [
    "original_listed_time",
    "listed_time",
    "expiry"
]

first_chunk = True
total_rows_written = 0

# Process and Clean Data in Chunks
for chunk in pd.read_csv(
    input_path,
    usecols=columns_to_keep,
    chunksize=chunk_size
):
    
    # Clean Text Fields
    chunk["company_name"] = (
        chunk["company_name"]
        .fillna("Not Specified")
        .str.strip()
    )

    chunk["title"] = chunk["title"].str.strip()
    chunk["location"] = chunk["location"].str.strip()

    # Clean Experience Level
    chunk["formatted_experience_level"] = (
        chunk["formatted_experience_level"]
        .fillna("Not Specified")
    )

    # Create an Accurate Remote-Status Field
    chunk["remote_status"] = (
        chunk["remote_allowed"]
        .map({1.0: "Remote explicitly allowed"})
        .fillna("Not explicitly flagged remote")
    )

    chunk = chunk.drop(columns=["remote_allowed"])

    # Convert Timestamp to Readable Dates
    for column in date_columns:
        chunk[column] = pd.to_datetime(
            chunk[column],
            unit="ms",
            errors="coerce"
        )

    # Rename Fields for Easier Analysis
    chunk = chunk.rename(columns={
        "formatted_work_type": "work_type",
        "formatted_experience_level": "experience_level"
    })

    # Save Cleaned Chunks
    chunk.to_csv(
        output_path,
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    first_chunk = False
    total_rows_written += len(chunk)

print("Cleaning complete.")
print(f"Rows written: {total_rows_written}")
print(f"Saved to: {output_path}")

