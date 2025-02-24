#!/usr/bin/python3
"""Python3"""


import http.server
import socketserver
import json

PORT = 8000

class Pepito(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API")
        elif self.path == "/data":
            self.send_response(200)
            sample_data = {"name": "John","age": 30,"city": "New York"}
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(sample_data))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Ok")
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            
with socketserver.TCPServer(("", PORT), Pepito) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()