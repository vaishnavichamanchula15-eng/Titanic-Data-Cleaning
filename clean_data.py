"""Clean the public Seaborn Titanic dataset and create audit outputs."""
from pathlib import Path
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
OUT = Path(__file__).parent

# Load source data
raw = pd.read_csv(DATA_URL)

# Save a pre-cleaning quality report
missing_before = raw.isna().sum()
duplicates_before = int(raw.duplicated().sum())

# Standardize text values (trim whitespace and normalize case)
for col in raw.select_dtypes(include="object").columns:
    raw[col] = raw[col].astype("string").str.strip()

for col in ["sex", "embarked", "class", "who", "deck", "embark_town", "alive"]:
    if col in raw.columns:
        raw[col] = raw[col].str.lower()

# Remove exact duplicate rows
clean = raw.drop_duplicates().copy()

# Correct/enforce data types
integer_cols = ["survived", "pclass", "sibsp", "parch"]
for col in integer_cols:
    clean[col] = pd.to_numeric(clean[col], errors="coerce").astype("Int64")
clean["age"] = pd.to_numeric(clean["age"], errors="coerce")
clean["fare"] = pd.to_numeric(clean["fare"], errors="coerce")
clean["adult_male"] = clean["adult_male"].astype("boolean")
clean["alone"] = clean["alone"].astype("boolean")

# Fill missing values using simple, explainable rules
if "age" in clean:
    clean["age"] = clean["age"].fillna(clean["age"].median())
if "embarked" in clean:
    clean["embarked"] = clean["embarked"].fillna(clean["embarked"].mode().iloc[0])
if "embark_town" in clean:
    clean["embark_town"] = clean["embark_town"].fillna(clean["embark_town"].mode().iloc[0])
if "deck" in clean:
    clean["deck"] = clean["deck"].fillna("unknown")

# Ensure categorical text columns use consistent lowercase strings
for col in clean.select_dtypes(include=["object", "string"]).columns:
    clean[col] = clean[col].astype("string").str.strip().str.lower()

# Reconcile derived labels with their numeric/source fields where possible
if {"survived", "alive"}.issubset(clean.columns):
    clean["alive"] = clean["survived"].map({0: "no", 1: "yes"}).astype("string")
if {"pclass", "class"}.issubset(clean.columns):
    clean["class"] = clean["pclass"].map({1: "first", 2: "second", 3: "third"}).astype("string")

# Output cleaned data and an audit summary
clean.to_csv(OUT / "titanic_cleaned.csv", index=False)
report = pd.DataFrame({
    "missing_values_before": missing_before,
    "missing_values_after": clean.isna().sum().reindex(missing_before.index, fill_value=0),
})
report.to_csv(OUT / "data_quality_report.csv")

summary = [
    f"Rows before cleaning: {len(raw)}",
    f"Rows after cleaning: {len(clean)}",
    f"Exact duplicate rows removed: {duplicates_before}",
    "Missing values before cleaning:",
    missing_before.to_string(),
    "",
    "Missing values after cleaning:",
    clean.isna().sum().to_string(),
    "",
    "Final data types:",
    clean.dtypes.astype(str).to_string(),
]
(OUT / "cleaning_summary.txt").write_text("\n".join(summary), encoding="utf-8")
print("Cleaning complete. Files saved in:", OUT)
print("Rows:", len(raw), "->", len(clean))
print("Exact duplicates removed:", duplicates_before)
