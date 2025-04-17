# Networking Basics (Beginner Notes)

## 🧠 Why I'm Learning This

Networking is the foundation of everything in cybersecurity. I realized if I don’t understand how computers talk to each other, I won’t understand how attackers break in — or how to stop them. So I’m starting with the basics and keeping it simple while I build from here.

---

## 🌐 What Is a Network?

A network is just a group of devices (like computers, phones, routers) that can communicate with each other. They do this using specific rules called **protocols**.

---

## 📦 IP Addresses & Subnets

- **IP Address**: Every device has an IP address, like a digital home address. Example: `192.168.1.10`
- **Private IPs**: Used inside your home or office network (usually start with 192.168 or 10.x.x.x)
- **Public IPs**: The one the internet sees
- **Subnet**: Breaks a network into smaller pieces. Common one: `255.255.255.0` means the first 3 numbers are the “neighborhood” and the last number is the house.

---

## 📡 Common Protocols

- **TCP**: Connection-based, reliable (used for things like websites and emails)
- **UDP**: Faster, no guarantee the data arrives (used for games, video calls)
- **ICMP**: Used for testing connections (like the `ping` command)

---

## 🔢 Ports (Think of Them Like Doors)

Ports help identify what type of communication is happening on a device.

| Port | Protocol | What it’s For         |
|------|----------|------------------------|
| 80   | HTTP     | Websites (non-secure)  |
| 443  | HTTPS    | Secure websites        |
| 22   | SSH      | Remote access to systems |
| 53   | DNS      | Translates names to IPs |
| 25   | SMTP     | Sending email          |

---

## 🛠️ Tools I’m Learning

- **ping**: Tests if another device is up
- **ipconfig/ifconfig**: Shows my IP info
- **nmap**: Scans devices to see what’s open or available
- **tracert/traceroute**: Shows the path data takes to reach a site

---

## 🧩 Terms I Keep Seeing

- **LAN**: Local Area Network (like your home WiFi)
- **WAN**: Wide Area Network (like the internet)
- **MAC Address**: A physical ID for your network device (not the same as IP)
- **DNS**: Domain Name System — like the internet’s phonebook

---

## 💭 What I’m Still Figuring Out

- How subnetting math actually works (CIDR notation still confuses me)
- The difference between routing and switching
- How firewalls inspect traffic and decide what to block or allow

---

## ✅ What I’ve Learned So Far

- I can identify devices on my network using `ipconfig` or `nmap`
- I understand that ports are like doors to services
- I’m starting to think like a network — how things move from point A to B

---

## 📌 Next Step

Keep practicing:
- Use `nmap` to scan my home network
- Build a visual of how my home devices connect
- Start a TryHackMe room focused on networking (like “Intro to Networking”)

---

