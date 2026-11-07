# 🕵️‍♂️ Domain Recon & WHOIS Intelligence Tool
**Lightweight • Fast • Accurate • Privacy-Focused**
A Python-based domain intelligence toolkit with a clean Flask dashboard.
Built for security researchers, bug bounty hunters, penetration testers, and developers who want fast, local, and reliable reconnaissance without depending on third-party services.
---
## 🚀 Features
### ✔ WHOIS Lookup
- Registrar
- Registration & expiry
- Domain age
- Ownership metadata
### ✔ DNS Records
- A
- MX
- TXT
- NS
### ✔ Subdomain Brute-forcing
- Wordlist-based
- Customizable
### ✔ IP + Geo Information
- Domain → IP resolution
- Country
- Region
- ISP
- ASN
- Hosting provider
### ✔ SSL Certificate Details
- Issuer
- Subject
- Serial number
- Signature algorithm
- Valid from / Valid to
- Days left before expiry
- Version
### ✔ Flask Web Dashboard
- Clean, readable UI
- Instant scan results
- Perfect for demos & recon reports
---
## 📌 Why This Tool Is Useful
Perfect for:
- Cybersecurity learners
- Bug bounty hunters
- Penetration testers
- Threat investigators
- Network administrators
- Developers validating DNS/SSL setups
Use it to:
- Identify hosting + IP ownership
- Validate DNS changes
- Find subdomains
- Inspect SSL before deployment
- Perform pre-attack surface mapping
Everything runs **locally** — no tracking, no API rate-limits.
---
## 📁 Project Folder Structure
```bash
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
└── templates/
    └── index.html
```bash
---
## ▶️ How to Use
### 1️⃣ Clone or Download
```bash
git clone https://github.com/shahdevam8/domain-recon-tool.git
cd domain-recon-tool
```
### 2️⃣ Create & Activate Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Flask App
```bash
python app.py
```
### 5️⃣ Open the Dashboard
Open your browser:
```
http://127.0.0.1:5000
```
Enter any domain (example.com, google.com, amazon.in) and view:
- WHOIS details
- DNS records
- Subdomains
- IP + Geo-location
- Hosting provider & ASN
- SSL certificate details
---
## 🧩 Customization
- **Modify Wordlist:** recon/subdomains.txt
- **Modify UI:** templates/index.html
- **Add New Modules:** Port scanner, Directory brute-forcing, Tech detection (Wappalyzer), Shodan / VirusTotal enrichment, PDF / JSON report export, Screenshot capture
---
## 🔄 How to Duplicate This Repo
### ✔ Fork
Click **Fork** on GitHub.
### ✔ Template Repository
Enable **"Template Repository"** in settings. Users can click **Use this template**.
### ✔ Clone
```bash
git clone https://github.com/shahdevam8/domain-recon-tool.git
```
### ✔ Download ZIP
GitHub → Code → Download ZIP
---
## 🤝 Contributing
Pull requests are welcome! You can contribute: UI / Frontend, Performance improvements, New modules, Wordlists, Bug fixes
---
## ⚠ Legal Disclaimer
This tool is for:
- Educational purposes
- Pentesting with permission
- Recon on domains you own
Unauthorized scanning of external domains may be illegal.
---
## 🎉 You're All Set!
