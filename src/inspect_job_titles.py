# Import Libraries
import pandas as pd

# Load Data
postings = pd.read_csv("data/processed/postings_cleaned.csv")

# Job Title Counts
print("\nJob title counts:")
print(postings["title"].value_counts())

title_counts = postings["title"].value_counts().reset_index()

# Create Excel Reference
title_counts.to_csv(
    "excel_references/job_title_counts.csv",
    index=False
)

# Inspect Core Analyst Titles
data_analyst_mask = postings["title"].str.contains(
    "Data Analyst",
    case=False,
    na=False
)

print("\nData Analyst mask:")
print(data_analyst_mask.head(10))

data_analyst_postings = postings[data_analyst_mask]

print("\nData Analyst postings shape:")
print(data_analyst_postings.shape)

data_analyst_title_counts = (
    data_analyst_postings["title"]
    .value_counts()
    .reset_index()
)

# Create Data Analyst Excel Reference
data_analyst_title_counts.to_csv(
    "excel_references/data_analyst_title_counts.csv",
    index=False
)

# Inspect Business Analyst Titles
business_analyst_mask = postings["title"].str.contains(
    "Business Analyst",
    case=False,
    na=False
)

print("\nBusiness Analyst mask:")
print(business_analyst_mask.head(10))

business_analyst_postings = postings[business_analyst_mask]

print("\nBusiness Analyst postings shape:")
print(business_analyst_postings.shape)

business_analyst_title_counts = (
    business_analyst_postings["title"]
    .value_counts()
    .reset_index()
)

# Create Business Analyst Excel Reference
business_analyst_title_counts.to_csv(
    "excel_references/business_analyst_title_counts.csv",
    index=False
)

# Inspect BI Analyst Titles
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

bi_analyst_postings = postings[bi_analyst_mask]

print("\nBI Analyst postings shape:")
print(bi_analyst_postings.shape)

bi_analyst_title_counts = (
    bi_analyst_postings["title"]
    .value_counts()
    .reset_index()
)