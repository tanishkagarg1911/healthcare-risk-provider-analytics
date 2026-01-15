USE healthcare_analytics;

-- TOTAL PATIENTS
select count(distinct patient_id) as total_patients
from patients;

-- AVG LENGTH OF STAY
select avg(length_of_stay) from encounters;

-- 30-DAY READMISSION RATE
SELECT
    ROUND(AVG(readmitted_30_days) * 100, 2) AS readmission_rate_percent
FROM readmissions;

-- DEPARTMENT-WISE READMISSIONS

select p.department,
ROUND(AVG(r.readmitted_30_days) * 100, 2) AS readmission_rate
from readmissions r
inner join encounters e on e.encounter_id=r.encounter_id
inner join providers p on p.provider_id=e.provider_id
group by p.department
order by readmission_rate DESC;

-- TOP OVERLOADED PROVIDERS

SELECT
    e.provider_id,
    COUNT(*) AS total_encounters
FROM encounters e
GROUP BY e.provider_id
ORDER BY total_encounters DESC
LIMIT 5;

-- COST PER PATIENT

select e.patient_id,sum(t.treatment_cost) as patient_cost
from treatments t
inner join encounters e on t.encounter_id=e.encounter_id
group by e.patient_id
order by patient_cost desc
limit 5;

