from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class LoginHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())

    def do_POST(self):

        length = int(self.headers["Content-Length"])

        data = self.rfile.read(length).decode()

        form = urllib.parse.parse_qs(data)

        username = form.get("username", [""])[0]
        password = form.get("password", [""])[0]

        print("\n========== LOGIN RECEIVED ==========")
        print("Username:", username)
        print("Password:", password)
        print("====================================\n")

        self.send_response(200)
        self.end_headers()

        self.wfile.write(b"Login received.")

server = HTTPServer(("0.0.0.0",8000),LoginHandler)

print("HTTP Login Server Running...")
print("http://localhost:8000")

server.serve_forever()