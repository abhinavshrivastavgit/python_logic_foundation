# 1. String: Used for names and categories
project_name = "Foundation Recovery"

# 2. Integer: Used for whole numbers (counts)
days_active = 1 

# 3. Float: Used for percentages and decimals
growth_score = 0.55  # This is 55%

# 4. Boolean: Used for True/False logic
is_zero_day = False 

# --- LOGIC TEST ---
print(f"Project: {project_name}")
print(f"Is today a zero day? {is_zero_day}")

# This check uses your Technical Logic
if days_active >= 1:
    print("Streak started! Foundation is becoming rigid.")