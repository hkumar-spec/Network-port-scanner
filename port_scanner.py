import socket
import sys
from datetime import datetime

# Target host and critical ports to inspect
TARGET = "127.0.0.1"  # Localhost for safe testing
PORTS = [21, 22, 80, 443, 8080, 3306]

print("=" * 50)
print(f"Scanning Target: {TARGET}")
print(f"Time Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

try:
    for port in PORTS:
        # Create standard TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)  # 1 second timeout

        result = s.connect_ex((TARGET, port))
        if result == 0:
            print(f"[+] Port {port:5d} : OPEN")
        else:
            print(f"[-] Port {port:5d} : CLOSED")
        s.close()

except KeyboardInterrupt:
    print("\nScan interrupted by user.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCould not connect to target server.")
    sys.exit()

print("=" * 50)
print("Scan Complete.")
