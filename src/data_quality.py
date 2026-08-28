import pandas as pd

file_path = "data/raw/postings.csv"
chunksize = 20000

# Initialize Counters
total_rows = 0
null_counts = None
seen_job_ids = set()
duplicate_job_ids = 0
remote_counts = None
experience_counts = None
work_type_counts = None
pay_period_counts = None
currency_counts = None

# Process Data in Chunks
for chunk in pd.read_csv(file_path, chunksize=chunksize):
    total_rows += len(chunk)

    # Missing Values
    chunk_nulls = chunk.isna().sum()

    if null_counts is None:
            null_counts = chunk_nulls
    else:
         null_counts = null_counts.add(
            chunk_nulls,
             fill_value=0
        )

    # Remote Status    
    chunk_remote_counts = (
        chunk["remote_allowed"]
        .astype("object")
        .fillna("Missing")
        .value_counts()
    )
        
    if remote_counts is None:
        remote_counts = chunk_remote_counts
    else:
        remote_counts = remote_counts.add(
            chunk_remote_counts,
            fill_value=0
        )

    # Experience Level
    chunk_experience_counts = (
         chunk["formatted_experience_level"]
         .fillna("Missing")
         .value_counts()
     )

    if experience_counts is None:
        experience_counts = chunk_experience_counts
    else:
        experience_counts = experience_counts.add(
            chunk_experience_counts,
            fill_value=0
        )

    # Work Type
    chunk_work_type_counts = (
         chunk["formatted_work_type"]
         .fillna("Missing")
         .value_counts()
    )    

    if work_type_counts is None:
        work_type_counts = chunk_work_type_counts
    else:
        work_type_counts = work_type_counts.add(
            chunk_work_type_counts,
            fill_value=0
        )

    # Pay Period
    chunk_pay_period_counts = (
         chunk["pay_period"]
         .fillna("Missing")
         .value_counts()
    )    

    if pay_period_counts is None:
        pay_period_counts = chunk_pay_period_counts
    else:
        pay_period_counts = pay_period_counts.add(
            chunk_pay_period_counts,
            fill_value=0
        )
    # Currency
    chunk_currency_counts = (
         chunk["currency"]
         .fillna("Missing")
         .value_counts()
    )    

    if currency_counts is None:
        currency_counts = chunk_currency_counts
    else:
        currency_counts = currency_counts.add(
            chunk_currency_counts,
            fill_value=0
        )
        
# Duplicate Job IDs
    for job_id in chunk["job_id"].dropna():
        if job_id in seen_job_ids:
            duplicate_job_ids += 1
        else:
            seen_job_ids.add(job_id)

# Building the missing values summary
missing_percent = (null_counts / total_rows * 100).round(2)

missing_summary = pd.DataFrame({
    "missing_count": null_counts,
    "missing_percent": missing_percent
})

missing_summary = missing_summary.sort_values(
    "missing_percent",
    ascending=False
)

# Display Data Quality Results
print("Total rows:")
print(total_rows)

print("\nMissing values:")
print(missing_summary)

print("\nRemote allowed values:")
print(remote_counts.sort_values(ascending=False))

print("\nExperience level values:")
print(experience_counts.sort_values(ascending=False))

print("\nWork type values:")
print(work_type_counts.sort_values(ascending=False))

print("\nPay period values:")
print(pay_period_counts.sort_values(ascending=False))

print("\nCurrency values:")
print(currency_counts.sort_values(ascending=False))

print("\nDuplicate jobs IDs:")
print(duplicate_job_ids)