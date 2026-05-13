# 🔍 ADMIN FINDER

---

## 📌 About

Admin Finder is a multithreaded Python tool that scans websites for common admin panel paths using fast HTTP requests and randomized User-Agent headers.

The tool is designed for:

 Security learning
 
 Web reconnaissance practice
 
 Educational penetration testing

---

## ✨ Features

 Multi-threaded scanning
 Random User-Agent rotation
 Fast admin path detection
 Handles connection errors
 Beginner-friendly Python code
 Easy to modify and extend

---

## 🛠 Requirements
Python 3.x

No external libraries needed.

Built-in Python modules used:
```python

import requests

import threading

import random

import time


---

## 📥 Installation

Linux / Termux


pkg update && pkg upgrade

pkg install python git

git clone https://github.com/JKA-C0D35/admin_finder.git

cd admin_finder

pip install requests

---
Windows

Install Python first:

https://www.python.org/downloads/

Then run:


git clone https://github.com/JKA-C0D35/admin_finder.git

cd admin_finder

pip install requests


---

## 🚀 Usage

Run the script:


python admin_finder.py


Enter target URL:


Target URL: https://example.com


Example output:


Scanning: https://example.com

Status: 200 | URL: https://example.com/admin

Status: 404 | URL: https://example.com/admin/login

[ERROR]: Connection timeout


---

## 📂 Project Structure

---
admin-finder/
 │
 ├── admin_finder.py
 ├── README.md
 ├── LICENSE
 ├── requirements.txt

---

## 🧠 What I Learned

 Python threading
 HTTP requests handling
 Web directory scanning
 Automation scripting
 Error handling and exceptions

## ⚠ Disclaimer

 This tool is intended for:
 Educational purposes
 Cybersecurity learning
 Bug bounty reconnaissance
 Authorized security testing
 Do NOT use this tool against any website without permission.
 You are responsible for your actions.

## 👤 Author
 🧑 Developer: JKA-C0D35
 📦 Project: admin-finder
 🌐 GitHub: https://github.com/JKA-C0D35

## ⭐ Support

If you like this project, you can support it by:

⭐ Starring the repository  
🍴 Forking the project  
🐛 Reporting bugs  
🚀 Contributing improvements  
