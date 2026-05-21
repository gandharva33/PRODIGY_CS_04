⌨️ Python Keylogger  
### *Educational Cybersecurity Project*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Purpose-Educational-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

## ⚠️ Disclaimer

> This project is created strictly for **educational purposes**, cybersecurity learning, and authorized environments only.

🚫 **Do NOT use this software for unauthorized monitoring, spying, or malicious activities.**  
Using keyloggers without permission may violate privacy laws and ethical standards.

---

# ✨ Features

✅ Real-time keyboard tracking  
✅ Saves logs into a text file  
✅ Handles:
- Letters & numbers
- Special keys
- Spacebar
- Enter key
- Backspace key

✅ Session start & end timestamps  
✅ Stops safely using the `ESC` key  
✅ Beginner-friendly Python project

---

# 📸 Preview

```bash
⚠️ Keylogger running. For authorized/educational use only. Press Esc to stop.
```

### Example Log File

```text
--- Session Started: 2026-05-21 20:15:10 ---
hello world
[backspace]
--- Session Ended: 2026-05-21 20:16:42 ---
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Main programming language |
| pynput | Keyboard listener |
| datetime | Timestamp logging |

---

# 📂 Project Structure

```bash
📦 python-keylogger
 ┣ 📜 keylogger.py
 ┣ 📜 keystroke_log.txt
 ┗ 📜 README.md
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/gandharva33/python-keylogger.git
cd python-keylogger
```

---

## 2️⃣ Install Required Library

```bash
pip install pynput
```

---

# ▶️ Run the Program

```bash
python keylogger.py
```

---

# 🧠 How It Works

The program uses:

```python
from pynput import keyboard
```

to listen for keyboard events in real time.

Every key pressed:
- gets detected
- processed
- stored inside:

```bash
keystroke_log.txt
```

The listener automatically stops when:

```text
ESC key is pressed
```

---

# 📖 Learning Concepts

This project helps beginners understand:

🔹 Python event listeners  
🔹 Keyboard input handling  
🔹 File operations  
🔹 Logging systems  
🔹 Basic cybersecurity concepts  
🔹 Real-time event monitoring

---

# ⚡ Future Improvements

🚀 GUI version using Tkinter  
🚀 Encrypted log storage  
🚀 Screenshot capturing  
🚀 Email log reports  
🚀 Cross-platform optimization

---

# 🔒 Ethical Usage

✅ Allowed:
- Educational labs
- Cybersecurity practice
- Personal experiments
- Authorized systems

❌ Not Allowed:
- Password theft
- Unauthorized spying
- Monitoring without consent
- Malicious surveillance

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share it with others

---

# 📄 License

This project is licensed under the **MIT License**.

---

<p align="center">
  Made with ❤️ using Python
</p>
