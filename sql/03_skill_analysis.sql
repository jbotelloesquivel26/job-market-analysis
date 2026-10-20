-- Most Common Skills Categories for Analyst Jobs
SELECT
    skill_name,
    COUNT(*) AS job_count
FROM analyst_job_skills
GROUP BY skill_name
ORDER BY job_count DESC;