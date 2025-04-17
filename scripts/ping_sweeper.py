import os

def ping_sweep(subnet):
    print(f"Scanning {subnet}.0/24...\n")
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"[+] {ip} is up")
        else:
            print(f"[-] {ip} is down")

if __name__ == "__main__":
    subnet_input = input("Enter the subnet (e.g., 192.168.1): ")
    ping_sweep(subnet_input)
