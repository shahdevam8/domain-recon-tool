import socket
import requests

def get_ip_and_location(domain):
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        return {
            'ip': ip,
            'country': response.get('country'),
            'region': response.get('regionName'),
            'city': response.get('city'),
            'isp': response.get('isp'),
            'asn': response.get('as'),
            'org': response.get('org')
        }
    except Exception as e:
        return {'error': str(e)}
