import dns.resolver

def get_dns_records(domain):
    record_types = ['A', 'MX', 'TXT', 'NS']
    dns_records = {}

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            dns_records[record] = [rdata.to_text() for rdata in answers]
        except Exception:
            dns_records[record] = ['No record found']
    return dns_records
