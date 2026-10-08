import pandas as pd

job_skills = pd.read_csv("data/raw/jobs/job_skills.csv")
skills = pd.read_csv("data/raw/mappings/skills.csv")

print("Job skills shape:")
print(job_skills.shape)

print("\nSkills shape:")
print(skills.shape)

print("\nMissing values in job_skills:")
print(job_skills.isna().sum())

print("\nMissing values in skills:")
print(skills.isna().sum())

print("\nDuplicate rows in job_skills:")
print(job_skills.duplicated().sum())

print("\nDuplicate rows in skills:")
print(skills.duplicated().sum())

print("\nUnique skill abbreviations in job_skills:")
print(job_skills["skill_abr"].nunique())

print("\nUnique skill abbreviations in skills:")
print(skills["skill_abr"].nunique())

print("\nUnique job IDs in job_skills:")
print(job_skills["job_id"].nunique())