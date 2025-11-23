import ssl
import socket
from datetime import datetime, timezone

def get_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        # Extract certificate details
        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject = dict(x[0] for x in cert.get("subject", []))

        # Convert dates (cryptography now uses UTC)
        valid_from = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y GMT").replace(tzinfo=timezone.utc)
        valid_to = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y GMT").replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)
        days_left = (valid_to - now).days

        ssl_data = {
            "domain": domain,
            "issuer": {
                "commonName": issuer.get("commonName"),
                "organizationName": issuer.get("organizationName"),
                "countryName": issuer.get("countryName")
            },
            "subject": {
                "commonName": subject.get("commonName"),
                "organizationName": subject.get("organizationName")
            },
            "valid_from": valid_from.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "valid_to": valid_to.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "days_left": days_left,
            "serial_number": cert.get("serialNumber"),
            "version": cert.get("version"),
            "signature_algorithm": cert.get("signatureAlgorithm"),
        }

        return ssl_data

    except Exception as e:
        return {"error": str(e)}
