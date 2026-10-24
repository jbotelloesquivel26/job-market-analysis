# Import Libraries
import pandas as pd


# Load Processed Data
analyst_postings = pd.read_csv(
    "data/processed/analyst_postings.csv"
)

analyst_technical_skills = pd.read_csv(
    "data/processed/analyst_technical_skills.csv"
)

# Export Data to Excel Workbook
output_path = "data/processed/job_market_analysis_powerbi.xlsx"

with pd.ExcelWriter(
    output_path,
    engine="xlsxwriter"
) as writer:
    analyst_postings.to_excel(
        writer,
        sheet_name="analyst_postings",
        index=False
    )

    analyst_technical_skills.to_excel(
        writer,
        sheet_name="technical_skills",
        index=False
    )

    # Create Excel Tables
    workbook = writer.book

    postings_sheet = writer.sheets["analyst_postings"]
    skills_sheet = writer.sheets["technical_skills"]

    postings_rows, postings_cols = analyst_postings.shape
    skills_rows, skills_cols = analyst_technical_skills.shape

    postings_sheet.add_table(
        0,
        0,
        postings_rows,
        postings_cols - 1,
        {
            "name": "AnalystPostings",
            "columns": [
                {"header": column}
                for column in analyst_postings.columns
            ]
        }
    )

    skills_sheet.add_table(
        0,
        0,
        skills_rows,
        skills_cols - 1,
        {
            "name": "AnalystTechnicalSkills",
            "columns": [
                {"header": column}
                for column in analyst_technical_skills.columns
            ]
        }
    )