# Broken Brute-Force Protection, IP Block - Lab Solver

## 📜 Description
This repository contains a Python script that automates the solution for the PortSwigger Web Security Academy lab: **"Broken brute-force protection, IP block"**.  
The lab is vulnerable due to a logic flaw in its password brute-force protection mechanism. The script bypasses IP-based blocking by alternating login attempts between valid credentials and brute-force attempts. It ultimately brute-forces the victim's password, logs in as the victim, and accesses their account page.

---

## 🚀 Features
- Automates brute-forcing the victim's password while bypassing IP blocking.
- Alternates login attempts with valid credentials to avoid triggering blocks.
- Provides a simple and efficient way to complete the lab.

---

## 🛠️ Requirements
- Python 3.7+
- `requests` library: Install it using `pip install requests`.

---

## 📝 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Broken-Brute-Force-Solver.git
   cd Broken-Brute-Force-Solver
   Enter the login URL (endpoint): https://0a5e004a0302d3a186314fbb009000e3.web-security-academy.net/login
   Enter the username field name in the request (e.g., 'username'): username                                                
   Enter the password field name in the request (e.g., 'password'): password
   Choose content-type (1: application/x-www-form-urlencoded, 2: application/json): 1
   Enter the valid username: wiener
   Enter the valid password: peter
   Choose brute-force mode (1: Username, 2: Password): 2
   Enter the username to brute-force: carlos
   Enter the path to the wordlist file: Path\to\wordlist.txt


