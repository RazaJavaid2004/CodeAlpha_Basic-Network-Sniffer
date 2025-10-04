## ✅ README.md — Basic Network Sniffer

# 🕵️‍♂️ Basic Network Sniffer

A modular Python-based packet sniffer built with Scapy, designed for educational and cybersecurity use.
Captures live network traffic, logs summaries with timestamps, and supports clean environment setup via `venv`.

---

## 🚀 Features

- ✅ Real-time packet sniffing using Scapy
- ✅ Timestamped logging to `logs/sniffer_YYYYMMDD_HHMMSS.txt`
- ✅ UTF-8 safe output for cross-platform compatibility
- ✅ Modular structure for easy extension (filters, CLI, logging)
- ✅ Clean virtual environment setup for reproducibility

---

## 🧰 Prerequisites

- Python 3.11+ — [Download from python.org](https://www.python.org)
- Npcap (Windows packet capture driver) — [Download here](https://npcap.com)
- OS: Windows 10/11 (tested)

---

## 🧪 Setup Instructions

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # For CMD
# Or use:
venv\Scripts\Activate.ps1  # For PowerShell

# Install dependencies
pip install -r requirements.txt
```

---

## 📦 Dependencies

```text
scapy==2.6.1
colorama==0.4.6
```

---

## 🧾 Usage

```bash
python sniffer.py
```

This will:

- Sniff packets for 30 seconds  
- Print summaries to terminal  
- Save logs to `logs/sniffer_YYYYMMDD_HHMMSS.txt`

---

## 📁 Sample Log Output

```text
[2025-10-04 16:23:13] Ethernet | 2e:24:76:a3:5d:eb -> 8c:42:6d:15:1a:45 | Ether / IP / TCP 192.168.100.7:59360 > 20.42.72.131:https FA
```

---

## 🧠 Future Enhancements

- [ ] Protocol filters (e.g., TCP, ICMP)
- [ ] Interface selection via CLI
- [ ] Packet count or timeout as command-line arguments
- [ ] Log rotation or archiving
- [ ] GUI wrapper (Tkinter or PyQt)

---

## 🤝 Credits

Built by [Muhammad Raza](https://github.com/RazaJavaid2004) as part of the [CodeAlpha Cybersecurity Internship](https://codealpha.tech/).

---

## 🔐 License

MIT — feel free to fork, modify, and contribute.
```
