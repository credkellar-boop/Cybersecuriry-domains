def calculate_risk(threat_likelihood, impact_severity):
    """
    Calculates a risk score (1-25) based on a 5x5 matrix.
    Likelihood: 1 (Rare) to 5 (Almost Certain)
    Impact: 1 (Insignificant) to 5 (Catastrophic)
    """
    score = threat_likelihood * impact_severity
    
    if score >= 15:
        rating = "High"
    elif score >= 8:
        rating = "Medium"
    else:
        rating = "Low"
        
    return f"Risk Score: {score} ({rating})"

# Usage
# print(calculate_risk(4, 5)) # High risk (20)
