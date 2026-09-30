import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html_path = os.path.join(os.path.dirname(__file__), 'index.html')
        if not os.path.exists(html_path):
            html_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')
        if os.path.exists(html_path):
            with open(html_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.wfile.write(b"<h1>VPNGuard Dashboard Loaded</h1>")
