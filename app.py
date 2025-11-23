from flask import Flask, render_template, request
from recon.whois_lookup import get_whois_info
from recon.dns_lookup import get_dns_records
from recon.subdomain_enum import brute_force_subdomains
from recon.ip_info import get_ip_and_location
from recon.ssl_info import get_ssl_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        domain = request.form['domain'].strip()
        try:
            whois_info = get_whois_info(domain)
            dns_info = get_dns_records(domain)
            subdomains = brute_force_subdomains(domain)
            ip_info = get_ip_and_location(domain)
            ssl_details = get_ssl_info(domain)

            result = {
                'domain': domain,
                'whois': whois_info,
                'dns': dns_info,
                'subdomains': subdomains,
                'ip_info': ip_info,
                'ssl': ssl_details
            }
        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
