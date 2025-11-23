import socket

COMMON_SUBDOMAINS = [
    'www', 'mail', 'ftp', 'test', 'dev', 'api', 'blog', 'shop', 'staging'
]

def brute_force_subdomains(domain):
    found = []
    for sub in COMMON_SUBDOMAINS:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            found.append({'subdomain': subdomain, 'ip': ip})
        except socket.gaierror:
            pass
    return found
