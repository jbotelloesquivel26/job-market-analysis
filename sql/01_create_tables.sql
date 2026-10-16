-- Create Analyst Postings Table
CREATE TABLE IF NOT EXISTS analyst_postings (
    job_id BIGINT PRIMARY KEY,
    company_name TEXT,
    title TEXT,
    max_salary NUMERIC,
    pay_period TEXT,
    location TEXT,
    company_id BIGINT,
    views BIGINT,
    med_salary NUMERIC,
    min_salary NUMERIC,
    work_type TEXT,
    original_listed_time TIMESTAMP,
    expiry TIMESTAMP,
    experience_level TEXT,
    listed_time TIMESTAMP,
    sponsored BOOLEAN,
    currency TEXT,
    compensation_type TEXT,
    normalized_salary NUMERIC,
    remote_status TEXT
);

-- Create Analyst Job Skills Table
CREATE TABLE IF NOT EXISTS analyst_job_skills (
    job_id BIGINT NOT NULL,
    skill_abr TEXT NOT NULL,
    skill_name TEXT NOT NULL,
    PRIMARY KEY (job_id, skill_abr),
    FOREIGN KEY (job_id) REFERENCES analyst_postings(job_id)

);