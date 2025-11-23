🕵️‍♂️ Domain Recon & WHOIS Intelligence Tool
Lightweight · Fast · Accurate · Privacy-Focused

A Python-powered domain intelligence toolkit with a clean Flask dashboard.
Built for security researchers, bug bounty hunters, penetration testers, and developers.

It performs complete domain reconnaissance including:

WHOIS lookup

DNS record extraction

Subdomain brute-forcing

IP + Geo-location lookup

ASN & hosting provider info

SSL Certificate details (issuer, expiry, days left, etc.)

Flask web interface

🚀 Features
✅ 1. WHOIS Lookup
Registrar

Registration / Expiry dates

Ownership metadata

Domain age

✅ 2. DNS Record Scanner
A

MX

TXT

NS
(using dnspython)

✅ 3. Subdomain Enumeration
Wordlist-based brute forcing

Customizable dictionary

✅ 4. IP & Hosting Intelligence
Domain → IP resolution

Geo-location (country, region, ISP)

ASN

Hosting provider

✅ 5. SSL Certificate Scanner
Issuer

Subject

Valid from / Valid to

Days left until expiry

Serial number

Signature algorithm

Version

✅ 6. Clean Flask Dashboard
Intuitive UI

Fast response

Great for demos & recon reports

📌 Why Use This Tool?
This tool is perfect for:

Cybersecurity learners

Bug bounty hunters

Penetration testers

Investigators

Network admins

Developers verifying DNS/SSL setups

Use it to:

Validate DNS changes

Check SSL certificate expiration

Enumerate subdomains for attack surface mapping

Identify hosting/ASN

Perform pre-engagement recon

Inspect domains before production deployment

No external SaaS, no limits — everything is processed locally.

📁 Project Structure
domain-recon-tool/
│ app.py
│ requirements.txt
│ README.md
│
├── recon/
│   ├── whois_lookup.py
│   ├── dns_lookup.py
│   ├── subdomain_enum.py
│   ├── ip_geo.py
│   ├── ssl_info.py
│   └── subdomains.txt
│
└── templates/
    └── index.html
▶️ Usage Guide (How to Run)
Step 1: Clone the Repository
git clone https://github.com/yourusername/domain-recon-tool.git
cd domain-recon-tool
Step 2: Install Dependencies
Create a virtual environment (recommended):

Windows

python -m venv venv
venv\Scripts\activate
Linux/Mac

python3 -m venv venv
source venv/bin/activate
Install packages:

pip install -r requirements.txt
Step 3: Start the Flask Server
python app.py
Step 4: Open Dashboard
Go to:

http://127.0.0.1:5000
Enter any domain:

google.com

amazon.in

example.org

You'll instantly get:

WHOIS

DNS

Subdomains

SSL info

IP + Geo

Hosting

All in one place.

🔄 How to Duplicate / Fork This Repo
If users want to create their own version:

Option 1 — Fork
Click Fork on GitHub → Full editable copy in their account.

Option 2 — Download ZIP
Click Code → Download ZIP.

Option 3 — Clone
git clone https://github.com/yourusername/domain-recon-tool.git
Option 4 — Template Mode (Optional)
If you want to allow “Duplicate Repo” style, you can turn your repo into a Template:

Go to Settings → Template Repository → Enable

Users will see the option "Use this Template"

🧩 Customization Options
You can easily upgrade this tool by adding:

Port scanning module (nmap/pure python)

Directory brute-forcing (like dirsearch)

Tech stack detection (Wappalyzer APIs)

Shodan / VirusTotal enrichment

Website screenshot capture

Export report to PDF/JSON

Add dark mode UI