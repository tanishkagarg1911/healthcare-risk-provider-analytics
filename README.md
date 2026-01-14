# healthcare-risk-provider-analytics
# Healthcare Provider Performance & Patient Readmission Risk Analytics Platform

## 📌 Problem Statement
Hospitals generate large volumes of patient and operational data, but lack integrated analytics systems to proactively identify high-risk patients and evaluate provider performance. This often leads to higher readmission rates, increased operational costs, and suboptimal resource allocation.

This project aims to build an end-to-end healthcare analytics platform that enables hospitals to:
- Identify patients at high risk of 30-day readmission
- Analyze provider and department-level performance
- Monitor key healthcare KPIs for data-driven decision-making

---

## 🎯 Objectives
- Design a healthcare-style relational data model
- Perform SQL-based KPI analysis on patient and provider data
- Build a risk scoring model to predict patient readmissions
- Create executive dashboards for hospital stakeholders
- Translate data insights into actionable business recommendations

---

## 🗂️ Dataset Overview
The project uses **synthetic healthcare data** generated using Python to simulate real-world Electronic Health Records (EHR) while avoiding privacy concerns.

### Tables Included:
- **patients**: demographics and chronic conditions
- **providers**: department and experience details
- **encounters**: hospital admissions and length of stay
- **treatments**: cost incurred per encounter
- **readmissions**: 30-day readmission flag

Domain logic was applied to ensure realistic patterns (e.g., higher readmission risk for elderly and chronic patients).

---

## 🛠️ Tech Stack
- **SQL**: MySQL / PostgreSQL (data modeling & KPI analysis)
- **Python**: pandas, numpy, matplotlib (data processing & ML)
- **Machine Learning**: Logistic Regression (risk prediction)
- **BI Tool**: Power BI (interactive dashboards)
- **Version Control**: Git & GitHub

---

## 📊 Key KPIs & Metrics
- 30-Day Readmission Rate
- Average Length of Stay
- Cost per Patient
- High-Risk Patient Percentage
- Provider Utilization Rate
- Department-wise Outcome Efficiency

---

## 🧠 Methodology
1. Designed normalized healthcare tables and generated synthetic data
2. Loaded datasets into SQL for KPI-driven analysis
3. Performed data cleaning and feature engineering using Python
4. Built an interpretable ML model prioritizing recall for high-risk patients
5. Developed Power BI dashboards for hospital and provider insights
6. Derived business recommendations based on analytical findings

---

## 📈 Key Insights
- Elderly patients and those with chronic conditions show significantly higher readmission risk
- Certain departments exhibit high patient load but lower outcome efficiency
- A small percentage of patients contribute disproportionately to readmission costs

---

## 📊 Dashboard Overview
The Power BI dashboard includes:
- Hospital-level KPI overview
- Department performance comparison
- Provider-level workload and outcome analysis
- High-risk patient segmentation

(Screenshots available in `/dashboards/dashboard_screenshots`)

---

## 💡 Business Recommendations
- Implement early follow-up programs for high-risk patients
- Redistribute provider workload in overburdened departments
- Use risk scores to prioritize post-discharge care and reduce cost leakage

---

## 🔮 Future Enhancements
- Incorporate real-time data ingestion
- Extend risk modeling with time-series features
- Add explainability dashboards for clinical users
- Deploy as a web-based analytics application

---

## 📎 Repository Structure
healthcare-risk-provider-analytics/
├── data/
├── sql/
├── notebooks/
├── dashboards/
├── docs/
└── README.md
