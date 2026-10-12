# Import Libraries
import pandas as pd

# Load Data
postings_cleaned = pd.read_csv("data/processed/postings_cleaned.csv")
job_skills = pd.read_csv("data/raw/jobs/job_skills.csv")
skills = pd.read_csv("data/raw/mappings/skills.csv")

# Merge Skills Names
job_skills_named = job_skills.merge(
    skills[["skill_abr", "skill_name"]],
    on="skill_abr",
    how="left"
)

# Merge Postings with Skills
postings_with_skills = postings_cleaned.merge(
    job_skills_named,
    on="job_id",
    how="left"
)

# Save Processed Data
postings_with_skills.to_csv(
    "data/processed/postings_with_skills.csv",
    index=False
)

# Validate Output
print("\nProcessed postings with skills shape:")
print(postings_with_skills.shape)