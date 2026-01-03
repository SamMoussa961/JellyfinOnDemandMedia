import subprocess
import ipaddress

def ping_host(ip, timeout=5):

    try:
        ipaddress.IPv4Address(ip)
    except ValueError:
        return False

    command = ['ping', '-c', '1', ip]

    try:
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        return response.returncode == 0
    except subprocess.TimeoutExpired:
        return False

