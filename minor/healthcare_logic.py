# --- PILLAR: DATA LITERACY + TECHNICAL LOGIC ---
# Case: Congestive Heart Failure (CHF) Readmission

# 1. String (Category)
condition = "Congestive Heart Failure"

# 2. Integer (Threshold from IBM Case)
days_since_rehab = 365 

# 3. Float (Probability/Risk)
readmission_score = 0.82

# 4. Boolean (Decision Point)
is_high_risk = readmission_score > 0.70

# --- THE "ANALYTIC APPROACH" LOGIC ---
if is_high_risk:
    print(f"STAKEHOLDER ALERT: Patient with {condition} is at {readmission_score * 100}% risk.")
    print("Action: Schedule Clinical Workshop.")
else:
    print("Status: Stable.")