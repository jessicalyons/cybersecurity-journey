# Linux Commands (Beginner Notes)

## ✍️ Why I’m Learning Linux

Almost everything in cybersecurity touches Linux at some point — whether it’s hacking labs, servers, or running tools in Kali. At first it was intimidating, but now I see it as one of the most powerful tools I can learn. I’m keeping track of the commands I use so I don’t forget and can build muscle memory.

---

## 🖥️ Basic Navigation Commands

| Command            | What It Does                            |
|--------------------|------------------------------------------|
| `pwd`              | Shows current directory (where I am)     |
| `ls`               | Lists files in a folder                  |
| `cd foldername`    | Changes into a folder                    |
| `cd ..`            | Goes up one level                        |
| `clear`            | Clears the screen                        |
| `mkdir newfolder`  | Creates a new folder                     |
| `touch file.txt`   | Creates an empty file                    |

---

## 📁 File Viewing & Editing

| Command                 | What It Does                            |
|--------------------------|------------------------------------------|
| `cat file.txt`           | Displays the file’s contents             |
| `less file.txt`          | Scroll through a file (q to quit)        |
| `nano file.txt`          | Opens a simple text editor               |
| `rm file.txt`            | Deletes a file                           |
| `rmdir foldername`       | Deletes an empty folder                  |
| `rm -r foldername`       | Deletes a folder and everything inside   |

---

## 🔐 Permissions & Ownership

| Command                 | What It Does                            |
|--------------------------|------------------------------------------|
| `ls -l`                  | Lists files with permissions             |
| `chmod 755 file.sh`      | Changes file permissions                 |
| `chown user:user file`   | Changes who owns the file                |

I’m still learning what the numbers mean in `chmod`, but 755 is common for scripts.

---

## ⚙️ System Info & Networking

| Command               | What It Does                            |
|------------------------|------------------------------------------|
| `ifconfig` or `ip a`   | Shows network interfaces & IPs           |
| `ping google.com`      | Tests connection                         |
| `netstat -tuln`        | Shows open ports                         |
| `whoami`               | Shows current user                       |
| `uname -a`             | Shows system info                        |
| `df -h`                | Shows disk space                         |
| `top` or `htop`        | Real-time system usage                   |

---

## 🛠️ Useful for Cyber Work

- `nmap`, `tcpdump`, `nc` → tools I’ll learn next
- `chmod +x script.sh` → makes a script executable
- `./script.sh` → runs the script in current directory

---

## 💭 What Still Confuses Me

- File permission breakdown (what 777 or 644 mean exactly)
- How to use `grep` with `cat` or logs
- When to use `sudo` and when not to

---

## ✅ Things I Can Do Now

- Navigate the file system without using a GUI
- Create and delete files/folders
- Use `nano` to edit a config or text file
- Check my IP address and see what ports are open

---

## 📌 Next Steps

- Learn `grep`, `find`, and `awk` for log searching
- Practice creating users and managing permissions
- Use TryHackMe Linux rooms to apply these commands in a real lab

---

