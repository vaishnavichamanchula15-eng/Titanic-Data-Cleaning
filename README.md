# Titanic Dataset – Data Cleaning Project

## Objective
Identify and correct common data-quality problems in a public dataset, including missing values, duplicate rows, data types, and inconsistent categorical values.

## Dataset
- **Name:** Titanic passenger dataset (Seaborn example dataset)
- **Source CSV:** https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
- **Source repository:** https://github.com/mwaskom/seaborn-data
- **Expected original size:** 891 rows and 15 columns

## Tools
Python, pandas

## Issues checked and cleaning decisions
1. **Missing values:** The source contains missing `age`, `deck`, and a small number of `embarked` / `embark_town` values. Missing `age` values are filled with the median; missing embarkation values are filled with the most frequent value; missing `deck` values are labeled `unknown` because the cabin deck is not recoverable from the other columns.
2. **Duplicate records:** Exact duplicate rows are detected with `duplicated()` and removed with `drop_duplicates()`. The script prints the number removed; it does not assume that two passengers are duplicates merely because some fields match.
3. **Data types:** Numeric fields (`survived`, `pclass`, `sibsp`, `parch`, `age`, `fare`) and Boolean fields (`adult_male`, `alone`) are explicitly converted to suitable types. Invalid numeric text, if any, is coerced to missing and then handled by the missing-value rules where applicable.
4. **Inconsistent values:** Text is stripped of leading/trailing spaces and category labels are normalized to lowercase. The `alive` label is reconciled with `survived`, and `class` is reconciled with `pclass` so the paired columns agree.

## Run the project
```bash
pip install -r requirements.txt
python clean_data.py
```

The script downloads the public CSV and creates:
- `titanic_cleaned.csv` – cleaned dataset
- `data_quality_report.csv` – missing-value counts before and after cleaning
- `cleaning_summary.txt` – row counts, duplicate count, missing-value summary, and final data types

## Notes
The cleaned CSV and reports are generated when the script is run, so the repository remains reproducible from the cited public source. Keep the original source data unchanged and submit the generated cleaned CSV along with this README and script.

 

## Final Data Analytics Project

### 1. Problem Statement
The objective of this project is to analyze Titanic passenger data and identify the factors that influenced passenger survival.

### 2. Dataset Information
- Dataset: Titanic Dataset
- Format: CSV
- Data includes passenger details, age, gender, ticket class, fare and survival status.

### 3. Data Cleaning Process
- Checked missing values.
- Handled duplicate records.
- Corrected data formats.
- Prepared clean data for analysis.
- Exported the cleaned dataset.

### 4. Data Analysis
Analyzed passenger information to understand survival patterns based on:
- Gender
- Age
- Passenger class
- Fare
- Survival status

### 5. Power BI Dashboard
Created an interactive Power BI dashboard to present Titanic passenger survival analysis using charts, graphs and visualizations.

**Dashboard File:** Titanic_Survival_Analysis.pbix

### 6. Key Business Insights
- Female passengers had higher survival rates than male passengers.
- First-class passengers had better survival chances than lower-class passengers.
- Passenger age and ticket class were important factors in survival patterns.

### 7. Tools and Technologies
- Python
- Pandas
- Power BI
- GitHub

### 8. Conclusion
This project helped in understanding the complete data analytics process, including data cleaning, analysis, visualization and extracting meaningful insights from data.


