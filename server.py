from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        data_value = query_params.get('data', [''])[0]

        # response  client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Received data: {data_value}".encode())

   
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        #  'post_data.txt'
        with open('post_data.txt', 'w+') as file:
            file.write(post_data)
        
        #  client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_content = "POST data received and saved to file 'post_data.txt'"
        self.wfile.write(response_content.encode())


port = 9000

httpd = HTTPServer(("", port), MyHandler)

print(f"Serving on port {port}")

httpd.serve_forever()