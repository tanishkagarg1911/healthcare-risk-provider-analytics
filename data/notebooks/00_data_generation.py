import os

os.makedirs("../raw", exist_ok=True)
os.makedirs("../processed", exist_ok=True)
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

# ---------------- PATIENTS ----------------
n_patients = 1000
patients = pd.DataFrame({
    "patient_id": range(1, n_patients + 1),
    "age": np.random.randint(18, 90, n_patients),
    "gender": np.random.choice(["Male", "Female"], n_patients),
    "chronic_condition": np.random.choice(
        ["Diabetes", "Hypertension", "Heart Disease", "None"],
        n_patients,
        p=[0.25, 0.25, 0.2, 0.3]
    ),
    "region": np.random.choice(["North", "South", "East", "West"], n_patients)
})

patients.to_csv("data/raw/patients.csv", index=False)

# ---------------- PROVIDERS ----------------
n_providers = 50
providers = pd.DataFrame({
    "provider_id": range(1, n_providers + 1),
    "department": np.random.choice(
        ["Cardiology", "Orthopedics", "Neurology", "General Medicine"],
        n_providers
    ),
    "experience_years": np.random.randint(1, 30, n_providers)
})

providers.to_csv("data/raw/providers.csv", index=False)

# ---------------- ENCOUNTERS ----------------
n_encounters = 3000
encounters = pd.DataFrame({
    "encounter_id": range(1, n_encounters + 1),
    "patient_id": np.random.choice(patients["patient_id"], n_encounters),
    "provider_id": np.random.choice(providers["provider_id"], n_encounters),
    "admit_date": pd.to_datetime("2023-01-01") +
                  pd.to_timedelta(np.random.randint(0, 365, n_encounters), unit="D")
})

encounters["length_of_stay"] = np.random.randint(1, 15, n_encounters)
encounters["discharge_date"] = encounters["admit_date"] + \
                               pd.to_timedelta(encounters["length_of_stay"], unit="D")

encounters.to_csv("data/raw/encounters.csv", index=False)

# ---------------- TREATMENTS ----------------
treatments = pd.DataFrame({
    "encounter_id": encounters["encounter_id"],
    "treatment_cost": np.random.randint(5000, 200000, n_encounters)
})

treatments.to_csv("data/raw/treatments.csv", index=False)

# ---------------- READMISSIONS ----------------
enc_pat = encounters.merge(patients, on="patient_id", how="left")

def readmission_risk(row):
    risk = 0.1
    if row["age"] > 60:
        risk += 0.2
    if row["chronic_condition"] != "None":
        risk += 0.3
    return np.random.rand() < risk

readmissions = enc_pat[["encounter_id"]].copy()
readmissions["readmitted_30_days"] = enc_pat.apply(
    readmission_risk, axis=1
).astype(int)

readmissions.to_csv("data/raw/readmissions.csv", index=False)

print("✅ Synthetic healthcare data generated successfully.")
