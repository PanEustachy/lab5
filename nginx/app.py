import socket
import os

version = os.getenv("VERSION", "dev")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

html = f"""<!DOCTYPE html>
<html>
<head><title>App Info</title></head>
<body>
    <h1>Informacje o aplikacji</h1>
    <p><strong>IP serwera:</strong> {ip}</p>
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>Wersja aplikacji:</strong> {version}</p>
</body>
</html>
"""

# Zapisz do pliku
with open("index.html", "w") as f:
    f.write(html)