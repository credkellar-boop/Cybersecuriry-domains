import socket

def scan_port(ip, port):
    """Attempts to connect to a specific port on a target IP."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"Port {port} is OPEN")
        s.close()
        return True
    except:
        return False

# Usage
# target_ip = "127.0.0.1"
# for port in range(20, 1025):
#     scan_port(target_ip, port)
