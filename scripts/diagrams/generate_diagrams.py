import requests
import base64

def generate_svg(mermaid_code, filename):
    """Generates an SVG file from Mermaid code using Mermaid.ink."""
    # Encode the code to base64
    encoded_code = base64.b64encode(mermaid_code.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/svg/{encoded_code}"
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{filename}.svg", "wb") as f:
            f.write(response.content)
        print(f"Successfully generated: {filename}.svg")
    else:
        print(f"Failed to generate {filename}.svg")

# Example Usage
domain_structure = """
mindmap
  root((Cyber Security))
    Security and Risk Management
    Asset Security
    Security Architecture and Engineering
    Communication and Network Security
    Identity and Access Management
    Security Assessment and Testing
    Security Operations
    Software Development Security
"""

generate_svg(domain_structure, "domain_structure")
