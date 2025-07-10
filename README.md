read the following steps

# 🔐 Python Keylogger with Email Reporting (Educational Use Only)

This is a simple **Python keylogger** that captures keyboard input and sends it to your email every 30 seconds. It is intended **only for educational and ethical use**, such as college projects or personal experimentation with Python, threading, and email automation.

---

## ⚠️ DISCLAIMER

> ❗ This project is for **learning purposes only**.  
> ❗ **Do NOT use** this on other people's computers or networks without clear permission.  
> ❗ Unauthorized use of keyloggers is **illegal and unethical**.

---

## 🧠 Features

- ✅ Captures keystrokes exactly as typed
- ✅ Ignores backspace, ESC, and special keys
- ✅ Sends logs to your email every 30 seconds
- ✅ Clean text (sentences) as user types
- ✅ Uses Gmail SMTP for email delivery

---

## 📦 Requirements

- Python 3.x  
- `pynput` library

Install it using:

```bash
pip install pynput

📤 Gmail Setup
Enable 2-Step Verification on your Gmail account.

Generate an App Password:
Google App Password Setup

Replace the email and password in the code:

python
Copy
Edit
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "your-app-password"
How to Run
Save the script as keylogger_email.py

Open terminal in the same folder

Run the script:

bash
Copy
Edit
python keylogger_email.py
The keylogger will start capturing and emailing keystrokes every 30 seconds.

