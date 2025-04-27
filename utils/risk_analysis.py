def calculate_risk(row):
    score = 0
    if row["Sleep Duration"] <= 5:
        score += 1
    if row["Stress Level"] >= 7:
        score += 1
    if row["Heart Rate"] >= 90:
        score += 1
    if row["Sleep Disorder"] != "None":
        score += 1
    return score

def categorize_risk(score):
    if score == 0:
        return "Low Risk"
    elif score <= 2:
        return "Medium Risk"
    else:
        return "High Risk"