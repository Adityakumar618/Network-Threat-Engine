import socket
import time

print("⚠️ Initiating Simulated Malware Beaconing...")

# We are going to attack Google's DNS server, but on highly suspicious ports
# used by malware (like Metasploit and Trojans).
target_ip = "8.8.8.8"
malicious_ports = [4444, 1337, 31337, 666]

for port in malicious_ports:
    try:
        print(f"--> Sending anomalous connection attempt to {target_ip} on Port {port}...")
        # This forces Windows to send a TCP SYN packet
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        s.connect((target_ip, port))
        s.close()
    except Exception:
        # We expect it to fail (Google blocks these ports), 
        # but the packet will still leave your computer!
        pass
    time.sleep(1)

print("✅ Attack simulation complete.")