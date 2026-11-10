import socket
import time

targets = [
    ("google.com", 443),
    ("github.com", 443),
    ("localhost", 9999),
    ("badhostname.invalid", 443)
]

def check_connection(host, port):
    ##start timer
    start = time.perf_counter()

    ip = None
    status = "UNKOWN"

    ##attempt TCP connection with remote host and port and handle exceptions
    try:
        ip = socket.gethostbyname(host)
    
        with socket.create_connection((ip,port), timeout=2):
            print("OPEN")
    except socket.timeout:
        print("Connection timed out")
    except ConnectionRefusedError:
        print("Connection refused")
    except socket.gaierror:
        print("DNS resolution failed")
    except OSError as error:
        print(f"Other network error: {error}")
    ##stop timer
    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000,2)
    return{
        "host": host,
        "port": port,
        "ip": ip,
        "status": status,
        "elapsed_ms": elapsed_ms
    }
    

def main():
    print("=" * 40)
    print("Network Connection Check")
    print("=" * 40)

    for host, port in targets:
        result = check_connection(host, port)
        print(f"\nHost: {result['host']}")
        print(f"Port: {result['port']}")
        print(f"IP: {result['ip'] or 'N/A'}")
        print(f"Status: {result['status']}")
        print(f"Elapsed Time: {result['elapsed_ms']:.2f} ms")
        print("-" * 40)

if __name__ == "__main__":
    main()