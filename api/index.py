from http.server import BaseHTTPRequestHandler
import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"¡Hola desde Vercel Serverless! Hora actual: {current_time}"
        
        self.wfile.write(message.encode('utf-8'))
        return