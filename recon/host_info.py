import socket
import requests
from ipwhois import IPWhois

IP_API_URL = "http://ip-api.com/json/{ip}?fields=status,country,regionName,city,lat,lon,isp,org,query"

def resolve_domain_ips(domain):
    ips = set()
    try:
        for res in socket.getaddrinfo(domain, None):
            if res[0] == socket.AF_INET:
                ips.add(res[4][0])
    except Exception:
        pass
    return list(ips)

def get_geo_for_ip(ip):
    try:
        r = requests.get(IP_API_URL.format(ip=ip), timeout=5)
        data = r.json()
        if data.get("status") == "success":
            return {
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "isp": data.get("isp"),
                "org": data.get("org"),
                "lat": data.get("lat"),
                "lon": data.get("lon")
            }
    except Exception:
        pass
    return {"error": "Geo lookup failed"}

def get_asn_for_ip(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        return {
            "asn": res.get("asn"),
            "asn_cidr": res.get("asn_cidr"),
            "network_name": (res.get("network") or {}).get("name"),
        }
    except Exception:
        return {"error": "ASN lookup failed"}

def get_host_info(domain):
    hosts = []
    for ip in resolve_domain_ips(domain):
        hosts.append({
            "ip": ip,
            "geo": get_geo_for_ip(ip),
            "asn": get_asn_for_ip(ip)
        })
    return hosts
