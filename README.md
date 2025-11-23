# 🕵️‍♂️ Domain Recon & WHOIS Intelligence Tool  
Lightweight • Fast • Accurate • Privacy-Focused

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
Clean, readable UI with instant scans.

---

## 📌 Why This Tool Is Useful

Perfect for:

- Cybersecurity learners  
- Bug bounty hunters  
- Pentesters  
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

domain-recon-tool/
│ app.py
│ requirements.txt
│ README.md
│
├── recon/
│ ├── whois_lookup.py
│ ├── dns_lookup.py
│ ├── subdomain_enum.py
│ ├── ip_geo.py
│ ├── ssl_info.py
│ └── subdomains.txt
│
└── templates/
└── index.html


---

## ▶️ How to Use
git clone https://github.com/shahdevam8/domain-recon-tool.git
### 1️⃣ Clone or Download
cd domain-recon-tool

---

### 2️⃣ Create & Activate Virtual Environment

**Windows:**
python -m venv venv
venv\Scripts\activate
**Linux / Mac:**
python3 -m venv venv
source venv/bin/activate

yaml
Copy code

---

### 3️⃣ Install Requirements

pip install -r requirements.txt

yaml
Copy code

---

### 4️⃣ Run the Flask App

python app.py

yaml
Copy code

---

### 5️⃣ Open the Dashboard
AT GIVEN IP
