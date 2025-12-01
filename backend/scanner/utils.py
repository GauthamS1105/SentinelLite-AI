import requests
import socket

def check_https(url):
    return url.startswith("https")

def get_headers(url):
    try:
        r = requests.get(url, timeout=5)
        return r.headers
    except:
        return {}

def scan_ports(domain):
    common_ports = [80, 443, 21, 22, 25]
    open_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((domain, port))
            open_ports.append(port)
        except:
            pass
        finally:
            sock.close()

    return open_ports
