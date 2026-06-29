def analyze_logs(file_path, search_term="FAILED"):
    """Searches for a specific term in a log file."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if search_term in line:
                    print(f"Suspicious activity found: {line.strip()}")
    except FileNotFoundError:
        print("Log file not found.")

# Usage
# analyze_logs("system.log", "FAILED")
