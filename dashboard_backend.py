import os
import glob

def get_security_summary():
    """Aggregates data from all domain log files."""
    summary = {}
    log_files = glob.glob("**/logs/*.md", recursive=True)
    
    for file in log_files:
        domain = file.split(os.sep)[0]
        with open(file, 'r') as f:
            content = f.read()
            # Logic to count "Critical" entries or recent logs
            summary[domain] = content.count("Critical") 
    return summary

# This backend will feed data to our frontend display
print(f"Current Security Posture: {get_security_summary()}")
