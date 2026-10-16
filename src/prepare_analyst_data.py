# Import Libraries
import pandas as pd

# Load Data
postings = pd.read_csv("data/processed/postings_cleaned.csv")
postings_with_skills = pd.read_csv("data/processed/postings_with_skills.csv")

# Filter Core Analyst Roles
data_analyst_mask = postings["title"].str.contains(
    "Data Analyst",
    case=False,
    na=False
)

business_analyst_mask = postings["title"].str.contains(
    "Business Analyst",
    case=False,
    na=False
)

bi_analyst_mask = (
    postings["title"].str.contains(
        "BI Analyst",
        case=False,
        na=False
    )
    |
    postings["title"].str.contains(
        "Business Intelligence Analyst",
        case=False,
        na=False
    )
)

reporting_analyst_mask = postings["title"].str.contains(
    "Reporting Analyst",
    case=False,
    na=False
)

analyst_mask = (
    data_analyst_mask
    | business_analyst_mask
    | bi_analyst_mask
    | reporting_analyst_mask
)

analyst_postings = postings[analyst_mask]

print("\nAnalyst postings shape:")
print(analyst_postings.shape)

# Create Excel Reference
analyst_postings.to_csv(
    "excel_references/analyst_postings.csv",
    index=False
)

# Filter Analyst Postings with Skills
analyst_skills_mask = postings_with_skills["job_id"].isin(analyst_postings["job_id"])
analyst_postings_with_skills = postings_with_skills[analyst_skills_mask]

print("\nAnalyst postings with skills shape:")
print(analyst_postings_with_skills.shape)

print("\nUnique analyst job IDs with skills:")
print(analyst_postings_with_skills["job_id"].nunique())

# Convert Whole Number Columns
analyst_postings["company_id"] = analyst_postings["company_id"].astype("Int64")
analyst_postings["views"] = analyst_postings["views"].astype("Int64")

analyst_postings_with_skills["company_id"] = (
    analyst_postings_with_skills["company_id"].astype("Int64")
)

analyst_postings_with_skills["views"] = (
    analyst_postings_with_skills["views"].astype("Int64")
)

# Create Analyst Job Skills Table
analyst_job_skills = analyst_postings_with_skills[
    ["job_id", "skill_abr", "skill_name"]
].dropna(subset=["skill_abr", "skill_name"])

print("\nAnalyst job skills shape:")
print(analyst_job_skills.shape)

# Save Processed Analyst Data
analyst_postings.to_csv(
    "data/processed/analyst_postings.csv",
    index=False
)

analyst_postings_with_skills.to_csv(
    "data/processed/analyst_postings_with_skills.csv",
    index=False
)

analyst_job_skills.to_csv(
    "data/processed/analyst_job_skills.csv",
    index=False
)

# Validate Saved Files
saved_analyst_postings = pd.read_csv(
    "data/processed/analyst_postings.csv"
)

saved_analyst_skills = pd.read_csv(
    "data/processed/analyst_postings_with_skills.csv"
)

print("\nSaved analyst postings shape:")
print(saved_analyst_postings.shape)

print("\nSaved analyst skills shape:")
print(saved_analyst_skills.shape)

saved_analyst_job_skills = pd.read_csv(
    "data/processed/analyst_job_skills.csv"
)

print("\nSaved analyst job skills shape:")
print(saved_analyst_job_skills.shape)