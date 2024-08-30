import cgi
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # print("Request headers:", self.headers)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        data = json.loads(self.rfile.read(int(self.headers.get('Content-Length'))))

        if "publicKey" in data.keys():
            if data["publicKey"] == "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDk9RLL24qZcbfmzKUsZo2G8EVVvYZhRc8V7fAcUqD/l+e1wKCpIMZwYyTUC5NXqm1XkO+A8Qh4VSTtUHSgWnAugvrihmKCXLxN84yuCkwMkaMg53R5q0/bQPp6vNG2S0kLd0cBLiS9NXI4+XvgGM6itx+FQncf9Nzd/6/0GmanFg1eRPAj6ucg0DGafQKX1pxlckUez1xYqvtc/UbtVzdRasmriKzLsoTX6MkmHCOqEMsUFPo9B3TjDzdSD3gbHvSqFd+t6jQsHAavp7vRfRxMu/AfkT3wXTpoSJen6hS+uCN4EHQ5b3UJgg+C1JudasWS6dBEn01Xkd5QwId9lFqH":
                self.wfile.write(bytes("{\"success\": true}", "utf-8"))
            else:
                print("not trusted: ", data)
                self.wfile.write(bytes("{\"success\": false}", "utf-8"))
        else:
            print("no publicKey: ", data)
            self.wfile.write(bytes("{\"success\": false}", "utf-8"))

def main():
    print('Listening on 0.0.0.0:8080')
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
