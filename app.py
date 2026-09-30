import os
from http.server import SimpleHTTPRequestHandler
import http.server

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or not os.path.exists(self.translate_path(self.path)):
            self.path = '/index.html'
        return super().do_GET()

app = CustomHandler

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server = http.server.HTTPServer(('0.0.0.0', port), CustomHandler)
    print(f"Serving on port {port}")
    server.serve_forever()
