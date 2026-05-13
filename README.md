# ⚡ GOOGLE DORKER ⚡

---

# 📌 About

Google Dorker is a simple Python tool that helps automate Google dork searching directly from your terminal.

It contains multiple predefined dork queries targeting different country domains such as:

* 🇵🇭 Philippines
* 🇺🇸 United States
* 🇬🇧 United Kingdom
* 🇨🇦 Canada
* 🇦🇺 Australia
* 🇮🇳 India
* 🇿🇦 South Africa

The tool automatically opens selected searches in your default browser.

---

# ✨ Features

✅ Large built-in dork list
✅ Country-based dorks
✅ Browser auto-open
✅ Hacker-style terminal output
✅ Lightweight and fast
✅ Beginner friendly

---

# 🛠 Requirements

* Python 3.x

No external libraries needed.

Built-in Python modules used:

```python
import os
import time
import random
import webbrowser
```

---

# 📥 Installation

## Linux / Termux

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/JKA-C0D35/google-dorker.git
cd google-dorker
python dorker.py
```

---

## Windows

Install Python first:

https://www.python.org/downloads/

Then run:

```bash
git clone https://github.com/JKA-C0D35/google-dorker.git
cd google-dorker
python dorker.py
```

---

# 🚀 Usage

Run the script:

```bash
python dorker.py
```

Example output:

```bash
[1] inurl: php?id=1 site:.ph
[2] inurl:php?id= site:edu.ph
[3] inurl:?page_id= site:.ph
```

Select a dork number:

```bash
root@dorker:~# 1
```

The selected Google dork will automatically open in your browser.

---

# 📂 Project Structure

```bash
google-dorker/
│
├── dorker.py
└── README.md
```

---

# ⚠ Disclaimer

This tool is intended for:

* Educational purposes
* Cybersecurity learning
* Bug bounty reconnaissance
* Security research

Do NOT use this tool for illegal activities.

You are responsible for your own actions.

---

# ❤️ Author

Made with Python & caffeine ☕

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
🚀 Contribute improvements
