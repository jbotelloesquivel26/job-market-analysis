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

-- Jobs by Work Type
SELECT
    work_type,
    COUNT(*) AS job_count
FROM analyst_postings
GROUP BY work_type
ORDER BY job_count DESC;

-- Jobs with Salary Information
SELECT
    COUNT(*) AS job_postings
FROM analyst_postings
WHERE normalized_salary IS NOT NULL;

-- Average Reported Salary
SELECT
    ROUND(AVG(normalized_salary),2) AS job_postings
FROM analyst_postings
WHERE normalized_salary IS NOT NULL;

-- Median Reported Salary
SELECT
    ROUND(
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY normalized_salary)::NUMERIC,2
    ) AS median_salary
FROM analyst_postings
WHERE normalized_salary IS NOT NULL;

-- Average Salary by Experience Level
SELECT
    experience_level,
    ROUND(AVG(normalized_salary), 2) AS average_salary
FROM analyst_postings
WHERE normalized_salary IS NOT NULL
GROUP BY experience_level
ORDER BY average_salary DESC;

--Salary Observations by Experience Level
SELECT
    experience_level,
    COUNT(*) AS salary_observations
FROM analyst_postings
WHERE normalized_salary IS NOT NULL
GROUP BY experience_level
ORDER BY salary_observations DESC;