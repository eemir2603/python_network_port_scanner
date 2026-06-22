# 1. ARSENAL: The core module that lets us talk to the operating system's network card.
import socket

print("-" * 50)
print("CYBER SECURITY ORACLE: PORT SCANNER V1.0")
print("-" * 50)

# 2. TARGET LOCK: Getting the IP address or URL from the user.
# For a legal test, you can use 'scanme.nmap.org' or '127.0.0.1' (your own machine).
target_ip = input("Enter Target IP or URL to Scan: ")

# We put the most critical doors (ports) into a list to save time.
# 21: FTP, 22: SSH, 80: HTTP, 443: HTTPS
target_ports = [21, 22, 80, 443]

print(f"\n[+] Scanning target: {target_ip}")
print("Please wait, knocking on doors...\n")

# 3. ENGINEERING (Loop and Socket Logic):
for port in target_ports:
    # Create a new socket (communication tunnel) for each port.
    system_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a 1-second timeout so our computer doesn't wait forever if the door doesn't answer.
    system_socket.settimeout(1)
    
    # 4. THE TEST: Attempting to connect to the specified IP and Port.
    # If the connection is successful, 'result' returns 0.
    result = system_socket.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[OPEN] Port {port} - This door is wide open!")
    else:
        print(f"[CLOSED] Port {port} - Door is locked.")
        
    # Clean up by closing the socket.
    system_socket.close()

print("\n[-] Scan Complete.")