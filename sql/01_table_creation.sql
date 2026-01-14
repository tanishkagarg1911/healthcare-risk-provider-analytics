CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    chronic_condition VARCHAR(50),
    region VARCHAR(20)
);
CREATE TABLE providers (
    provider_id INT PRIMARY KEY,
    department VARCHAR(50),
    experience_years INT
);
CREATE TABLE encounters (
    encounter_id INT PRIMARY KEY,
    patient_id INT,
    provider_id INT,
    admit_date DATE,
    discharge_date DATE,
    length_of_stay INT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);
CREATE TABLE treatments (
    encounter_id INT,
    treatment_cost INT,
    FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id)
);
CREATE TABLE readmissions (
    encounter_id INT,
    readmitted_30_days TINYINT,
    FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id)
);
