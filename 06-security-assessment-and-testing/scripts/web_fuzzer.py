import requests

def fuzz_url(base_url, wordlist):
    """Checks for the existence of common files/directories."""
    for path in wordlist:
        url = f"{base_url}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
        except requests.exceptions.RequestException:
            pass

# Usage
# target = "http://example.com"
# paths = ["admin", "config", "backup", "login"]
# fuzz_url(target, paths)
