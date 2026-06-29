import subprocess

subprocess.Popen([
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--remote-debugging-port=9222",
    r'--user-data-dir=C:\ChromeAutomation\User Data',
    '--profile-directory=Profile 1'
])

subprocess.Popen([
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--remote-debugging-port=9223",
    r'--user-data-dir=C:\ChromeAutomation\User Data Second',
    '--profile-directory=Profile 1'
])