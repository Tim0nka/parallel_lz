import subprocess
def ping(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output = True)
    print(f"{ip} is {'up' if result.returncode == 1 else 'down'}")

ips = ["23.236.62.147", "109.70.26.37.", "216.239.32.21", "23.227.38.32", "74.125.22.132", "1.179.201.18", "1.32.194.195", "1.55.188.25", "41.55.189.76", "2.16.10.106"]
for ip in ips: 
    ping(ip)