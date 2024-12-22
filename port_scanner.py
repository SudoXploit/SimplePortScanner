import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} for open ports from {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    open_ports.append(port)
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    if open_ports:
        print("\nOpen Ports:")
        for port in open_ports:
            print(f"  - Port {port}")
    else:
        print("\nNo open ports found.")
    print("\nScan complete.")

if __name__ == "__main__":
    target = input("Enter target IP address or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target, start_port, end_port)

