from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os

VERSION = os.getenv("VERSION", "dev")

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        hostname = socket.gethostname()
        client_ip = self.client_address[0]
        response = f"IP: {client_ip}\nHostname: {hostname}\nVersion: {VERSION}\n"
        self.wfile.write(response.encode())

if __name__ == "__main__":
    server = HTTPServer(('', 8080), SimpleHandler)
    print(f"Starting server on port 8080...")
    server.serve_forever()