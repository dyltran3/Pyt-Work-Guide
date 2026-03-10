# Exercise B-12: Mini Flask Clone

## 1. EXERCISE BRIEF

**Context**: Flask, Django đều bắt nguồn từ chuẩn WSGI (Web Server Gateway Interface) chung cho các WebApp server tại Python.
**Task**: Triển khai micro-framework hỗ trợ Routing căn bản `@app.route('/home')` từ điểm khởi nguồn giao thức WSGI (thực thi được bằng lệnh gunicorn/werkzeug).
**Constraints**: Chỉ dùng chuẩn `def __call__(self, environ, start_response)`. Xử lý regex match trong Router base.
## 2. STARTER CODE

```python
from wsgiref.simple_server import make_server

class App:
    def __init__(self):
        self.routes = {}

    def route(self, path: str):
        """
        TODO: Build a decorator [... logic ...] 
        """
        pass

    def __call__(self, environ: dict, start_response):
        """
        TODO: Implement the required WSGI standard interface [... logic ...] 
        """
        pass

if __name__ == "__main__":
    app = App()

    @app.route("/")
    def home(environ):
        return "Hello World!"

    @app.route("/api")
    def api_res(environ):
        return '{"status": "ok"}'

    # To test [... logic ...] 
    # server = make_server('localhost', 8080, app)
    # print("Running on port 8080...")
    # server.serve_forever()
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
Constructing [... logic ...] 

**HINT-3 (Near-solution)**:

```python
    def route(self, path: str):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        handler = self.routes.get(path)

        if handler:
            response_body = handler(environ)
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [response_body.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
            return [b'Not Found']
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Flask [... logic ...] 

## 5. VALIDATION CRITERIA

- [ ] Connects [... logic ...] 
- [ ] [... logic ...] 

## 6. EXTENSION CHALLENGES

1. **Extension 1:** [... logic ...] 
2. **Extension 2:** [... logic ...] 

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`wsgiref`).
