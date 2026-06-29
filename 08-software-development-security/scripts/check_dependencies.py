def check_requirements(file_path):
    """Checks requirements.txt for known vulnerable package names."""
    vulnerable_packages = ["requests==2.20.0", "flask==0.12.0"] # Example list
    
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            for package in lines:
                if package in vulnerable_packages:
                    print(f"SECURITY ALERT: Found vulnerable package: {package}")
    except FileNotFoundError:
        print("requirements.txt not found.")

# Usage:
# check_requirements("requirements.txt")
