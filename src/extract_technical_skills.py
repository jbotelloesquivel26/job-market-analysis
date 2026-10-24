# Import Libraries
import pandas as pd
import re

# Load Analyst Job IDs
analyst_postings = pd.read_csv(
    "data/processed/analyst_postings.csv"
)

# Load Raw Job Descriptions
raw_postings = pd.read_csv(
    "data/raw/postings.csv",
    usecols=[
        "job_id",
        "title",
        "description"
    ]
)

# Validate Job Descriptions
print("\nRaw Postings Shape:")
print(raw_postings.shape)

print("\nRaw Postings Columns:")
print(raw_postings.columns)

# Filter Analyst Job Descriptions
analyst_descriptions_mask = raw_postings["job_id"].isin(analyst_postings["job_id"])
analyst_descriptions = raw_postings[analyst_descriptions_mask]

print("\nAnalyst descriptions shape:")
print(analyst_descriptions.shape)

print("\nUnique analyst job IDs:")
print(analyst_descriptions["job_id"].nunique())

# Posting Without Description Text
print("\nPostings without descriptions:")
print(analyst_descriptions["description"].isna().sum())

# Define Technical Skill Patterns
skill_patterns = {
    "SQL": r"\bsql\b",
    "Python": r"\bpython\b",
    "Excel": r"\bmicrosoft excel\b|\bms excel\b|\bexcel\b",
    "Power BI": r"\bpower\s*bi\b",
    "Tableau": r"\btableau\b",
    "Pandas": r"\bpandas\b",
    "NumPy": r"\bnumpy\b",
    "R": r"\br programming\b|\br language\b|\brstudio\b|\busing r\b|\bexperience with r\b|\bknowledge of r\b",
    "SAS": r"\bsas\b",
    "SPSS": r"\bspss\b",
    "Alteryx": r"\balteryx\b",
    "Looker": r"\blooker\b",
    "Snowflake": r"\bsnowflake\b",
    "BigQuery": r"\bbigquery\b",
    "AWS": r"\baws\b|\bamazon web services\b",
    "Azure": r"\bazure\b",
    "GCP": r"\bgcp\b|\bgoogle cloud\b",
    "Git": r"\bgit\b|\bgithub\b",
    "PostgreSQL": r"\bpostgresql\b|\bpostgres\b",
    "MySQL": r"\bmysql\b",
    "SQL Server": r"\bsql\s*server\b|\bmssql\b",
    "Databricks": r"\bdatabricks\b",
    "Spark": r"\bapache\s+spark\b|\bpyspark\b",
    "Power Query": r"\bpower\s*query\b",
    "DAX": r"\bdax\b",
    "VBA": r"\bvba\b|\bvisual basic for applications\b",
}

# Create Technical Skills Result List
technical_skill_records = []

# Loop Through Analyst Job Descriptions
for _, row in analyst_descriptions.iterrows():
    job_id = row["job_id"]
    description = row["description"]
    
    for skill_name, pattern in skill_patterns.items():
        if re.search(pattern, description, flags=re.IGNORECASE):
            technical_skill_records.append(
                {
                    "job_id": job_id,
                    "technical_skill": skill_name
                }
            )

# Create Technical Skills DataFrame
technical_skills = pd.DataFrame(technical_skill_records)

print("\nTechnical skills shape:")
print(technical_skills.shape)

print("\nUnique jobs with technical skills:")
print(technical_skills["job_id"].nunique())

print("\nTop technical skills:")
print(technical_skills["technical_skill"].value_counts())

# Save Technical Skills Data
technical_skills.to_csv(
    "data/processed/analyst_technical_skills.csv",
    index=False
)

print("\nDuplicate job-skill relationships:")
print(
    technical_skills.duplicated(
        subset=["job_id", "technical_skill"]
    ).sum()
)