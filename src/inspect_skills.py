import pandas as pd

# Load Data
job_skills = pd.read_csv("data/raw/jobs/job_skills.csv")
skills = pd.read_csv("data/raw/mappings/skills.csv")
postings = pd.read_csv("data/processed/postings_cleaned.csv")

# Table Shapes
print("Job skills shape:")
print(job_skills.shape)

print("\nSkills shape:")
print(skills.shape)

print("\nPostings shape:")
print(postings.shape)

# Missing Values
print("\nMissing values in job_skills:")
print(job_skills.isna().sum())

print("\nMissing values in skills:")
print(skills.isna().sum())

# Duplicate Rows
print("\nDuplicate rows in job_skills:")
print(job_skills.duplicated().sum())

print("\nDuplicate rows in skills:")
print(skills.duplicated().sum())

# Unique Values
print("\nUnique skill abbreviations in job_skills:")
print(job_skills["skill_abr"].nunique())

print("\nUnique skill abbreviations in skills:")
print(skills["skill_abr"].nunique())

print("\nUnique job IDs in job_skills:")
print(job_skills["job_id"].nunique())

print("\nUnique job IDs in postings:")
print(postings["job_id"].nunique())

# Job ID Membership Test
print("\nFirst 10 job ID membership checks:")
print(job_skills["job_id"].isin(postings["job_id"]).head(10))

print("\nJob skill rows with no matching posting:")
print((~job_skills["job_id"].isin(postings["job_id"])).sum())

# Create Table of Unmatched Job Skills Row
unmatched_job_skills = job_skills[
    ~job_skills["job_id"].isin(postings["job_id"])
]

print("\nUnmatched job skills shape:")
print(unmatched_job_skills.shape)

print("\nUnique unmatched job IDs:")
print(unmatched_job_skills["job_id"].nunique())

# Posting IDs Without Matching Job Skills
print("\nPosting IDs without matching job skills:")
print((~postings["job_id"].isin(job_skills["job_id"])).sum())

# Skill Abbreviation Validation
print("\nSkill abbreviation without a matching lookup:")
print((~job_skills["skill_abr"].isin(skills["skill_abr"])).sum())

# Merge Skill Names
job_skills_named = job_skills.merge(
    skills, 
    on="skill_abr",
    how="left"
)

print("\nFirst 10 rows of merged job skills:")
print(job_skills_named.head(10))

print("\nMerged job skills shape:")
print(job_skills_named.shape)

print("\nMissing skill names after merge:")
print(job_skills_named["skill_name"].isna().sum())

# Merge Postings with Named Job Skills
postings_with_skills = postings.merge(
    job_skills_named,
    on="job_id",
    how="left"
)

print("\nFirst 10 rows of postings with skills:")
print(postings_with_skills.head(10))

print("\nMerged postings with skills shape:")
print(postings_with_skills.shape)