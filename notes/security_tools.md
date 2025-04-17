# Security Tools (Beginner Notes)

## 🎯 Why I'm Learning This

Cybersecurity tools can feel overwhelming when you’re new. There’s so many names being thrown around — Wireshark, Burp, Metasploit — and I didn’t even know what half of them did when I started. These notes are where I’m keeping track of each tool I’ve heard of, tried, or want to practice with. I’m not an expert yet, but this is how I’ll get there.

---

## 🧰 Tools I’ve Used (or Am Learning)

### 🔍 Nmap
- **What it is**: A network scanner
- **Why it matters**: Helps find live hosts, open ports, and services running on a network
- **Commands I tried**:
  - `nmap -sV 192.168.1.1` → scans for open ports and service versions
  - `nmap -sn 192.168.1.0/24` → host discovery only

---

### 🐍 Wireshark
- **What it is**: A packet analyzer
- **Why it matters**: You can see what’s happening on a network in real time
- **Learning curve**: High at first, but super powerful once you understand filters
- **Filters I’ve learned**:
  - `http` → shows HTTP traffic
  - `ip.addr == 192.168.1.10` → filters by IP

---

### 🦷 Burp Suite
- **What it is**: A web vulnerability scanner and proxy
- **Why it matters**: Lets you intercept and manipulate HTTP/HTTPS traffic
- **What I’ve tried**:
  - Intercepted login requests in a TryHackMe lab
  - Used Repeater to test form input behavior

---

### 🛠️ Netcat
- **What it is**: A tool for reading/writing data across networks
- **Why it matters**: It's called the “Swiss Army Knife” of networking
- **Commands I’m practicing**:
  - `nc -lvnp 4444` → listens for a reverse shell
  - `nc 192.168.1.10 80` → connects to a server on port 80

---

### 🧨 Metasploit Framework
- **What it is**: A tool for developing and executing exploits
- **Why it matters**: Common in red teaming and CTFs
- **What I learned**:
  - I can search for known exploits using `search`
  - It automates a lot of post-exploitation work
- Still feels advanced, but I'm getting more comfortable the more I play in labs

---

## 🧪 Tools I Want to Try Next

- **Hydra** → for brute force attacks
- **John the Ripper** → password cracker
- **Nikto** → scans for web server vulnerabilities
- **tcpdump** → command-line packet sniffer
- **Enum4linux** → used in SMB enumeration

---

## 🧠 What I’m Starting to Understand

- Each tool has a purpose — scanning, sniffing, cracking, or exploiting
- I don’t need to learn *everything* at once
- Practicing a few tools at a time helps me go deeper instead of being overwhelmed

---

## ✅ What I Can Do So Far

- Run a basic `nmap` scan to find live devices
- Use `Wireshark` to filter for HTTP traffic and see usernames in plain text
- Intercept simple web forms with `Burp Suite`
- Connect to a service with `netcat` and test response behavior

---

## 📌 Next Steps

- Keep using TryHackMe rooms that focus on one tool at a time
- Build a mini cheat sheet as I go
- Try combining tools in lab scenarios (like scanning with nmap → exploiting with Metasploit)

---

