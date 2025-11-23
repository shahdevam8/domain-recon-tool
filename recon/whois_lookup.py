import whois

def get_whois_info(domain):
    try:
        data = whois.whois(domain)
        return {key: str(value) for key, value in data.items()}
    except Exception as e:
        return {'error': str(e)}
