import http.server
import socketserver
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Если зашли на главную страницу (путь /)
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # HTML код страницы
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body, html { margin: 0; padding: 0; height: 100%; overflow: hidden; background: #000; }
                    .fullscreen-bg {
                        background-image: url('/image.png');
                        height: 100vh;
                        background-position: center;
                        background-repeat: no-repeat;
                        background-size: cover;
                    }
                </style>
            </head>
            <body>
                <div class="fullscreen-bg"></div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            # Если запрашивают файл (например, /image.png), используем стандартный метод
            return super().do_GET()

# Позволяет повторно использовать порт сразу после закрытия
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Сервер работает на порту {PORT}")
    httpd.serve_forever()
