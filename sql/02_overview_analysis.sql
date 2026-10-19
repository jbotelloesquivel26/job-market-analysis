-- Total Analyst Job Postings
SELECT
    COUNT(*) AS total_jobs
FROM analyst_postings;

-- Jobs by Experience Level
SELECT
    experience_level,
    COUNT(*) AS job_count
FROM analyst_postings
GROUP BY experience_level
ORDER BY job_count DESC;

-- Jobs by Remote Status
SELECT
    remote_status,
    COUNT(*) AS job_count
FROM analyst_postings
GROUP BY remote_status
ORDER BY job_count DESC;