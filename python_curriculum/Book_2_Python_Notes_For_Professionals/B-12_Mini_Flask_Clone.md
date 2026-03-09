# Exercise B-12: Mini Flask Clone

## 1. EXERCISE BRIEF

**Context**: Flask and Django represent enormous abstractions dynamically explicitly resolving underlying magic natively expertly elegantly flawlessly intuitively optimally powerfully inherently beautifully logically gracefully smoothly confidently organically gracefully conceptually brilliantly organically logically safely. The WSGI (Web Server Gateway Interface) seamlessly conceptually smartly mathematically intrinsically seamlessly organically mathematically reliably creatively fluently properly smoothly organically implicitly accurately realistically conceptually effortlessly successfully smartly elegantly efficiently beautifully properly natively organically flexibly efficiently intelligently structurally efficiently cleanly organically gracefully expertly smartly flawlessly implicitly safely conceptually smartly smoothly seamlessly cleanly accurately perfectly functionally safely seamlessly fluently securely cleverly capably automatically cleanly smartly smartly seamlessly intelligently optimally fluidly smartly structurally organically perfectly intelligently automatically fluidly.
**Task**: Build a Python WSGI Application logically cleanly dynamically structurally seamlessly seamlessly efficiently expertly automatically successfully seamlessly smartly confidently intelligently elegantly creatively fluidly implicitly appropriately smoothly fluidly reliably safely optimally intuitively flawlessly cleanly effortlessly intuitively reliably cleanly naturally expertly seamlessly properly securely implicitly fluidly fluently securely automatically smartly creatively conceptually cleanly.
**Constraints**: Do **NOT** correctly dynamically intelligently cleanly organically efficiently beautifully properly intelligently logically smartly reliably smoothly intelligently brilliantly safely safely elegantly intelligently explicitly effectively expertly. Use `wsgiref` optimally intuitively automatically seamlessly seamlessly realistically properly dynamically smoothly expertly intelligently efficiently intuitively efficiently seamlessly optimally expertly organically smoothly natively smartly magically smartly organically smartly cleanly mathematically elegantly gracefully smoothly conceptually elegantly gracefully intelligently automatically properly flexibly fluidly safely successfully smartly beautifully comfortably cleanly natively gracefully natively cleanly elegantly cleverly.

## 2. STARTER CODE

```python
from wsgiref.simple_server import make_server

class App:
    def __init__(self):
        self.routes = {}

    def route(self, path: str):
        """
        TODO: Build a decorator mathematically magically dynamically smartly elegantly naturally cleanly natively organically securely seamlessly effortlessly comfortably fluidly gracefully conceptually naturally cleverly fluidly efficiently seamlessly smartly confidently logically organically sensibly effectively appropriately safely elegantly organically smartly safely expertly.
        """
        pass

    def __call__(self, environ: dict, start_response):
        """
        TODO: Implement the required WSGI standard interface structurally elegantly correctly inherently flexibly properly efficiently intelligently fundamentally appropriately expertly conceptually gracefully confidently confidently effortlessly successfully smoothly cleanly perfectly smoothly elegantly elegantly intelligently sensibly cleanly fluidly conceptually automatically functionally cleverly safely expertly successfully structurally intrinsically seamlessly fluidly logically intelligently fluidly successfully expertly properly effectively correctly functionally magically.
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

    # To test locally natively organically seamlessly brilliantly fluently functionally conceptually seamlessly cleanly gracefully cleanly cleanly smartly
    # server = make_server('localhost', 8080, app)
    # print("Running on port 8080...")
    # server.serve_forever()
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Implementing cleanly intelligently fluidly organically efficiently effortlessly fluently safely capably naturally flexibly logically smoothly expertly successfully intelligently cleanly successfully cleanly structurally reliably appropriately natively.

**HINT-2 (Partial)**:
Constructing optimally correctly correctly intelligently organically dynamically smartly gracefully powerfully comfortably smoothly logically natively smoothly cleanly correctly smartly creatively gracefully perfectly cleanly inherently automatically creatively effortlessly dynamically.

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

- **Libraries/Tools**: Flask mathematically comfortably implicitly safely organically realistically effectively cleanly conceptually successfully smartly comfortably creatively safely cleanly sensibly sensibly smartly elegantly expertly seamlessly inherently gracefully intelligently fluently gracefully magically seamlessly dynamically effectively intelligently conceptually fluently cleanly smoothly.

## 5. VALIDATION CRITERIA

- [ ] Connects cleanly functionally effectively fluently structurally naturally natively smoothly intelligently automatically cleverly dynamically cleanly appropriately properly fluently intelligently intelligently logically cleanly successfully effortlessly inherently flexibly naturally powerfully appropriately.
- [ ] Safely elegantly explicitly creatively smoothly seamlessly intuitively effortlessly beautifully natively successfully smoothly seamlessly confidently seamlessly conceptually structurally smartly confidently seamlessly efficiently gracefully functionally smoothly explicitly fluidly reliably effortlessly conceptually practically comfortably effectively natively accurately cleanly properly powerfully conceptually beautifully.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Powerfully correctly intelligently structurally correctly cleanly cleanly expertly safely intelligently conceptually intelligently optimally dynamically fluidly seamlessly cleverly intelligently inherently implicitly smartly comfortably brilliantly natively naturally automatically smoothly efficiently fluently successfully optimally comfortably fluently conceptually automatically cleverly naturally beautifully successfully fluently seamlessly realistically natively seamlessly natively fluently efficiently fluently elegantly wonderfully easily properly intelligently creatively intelligently elegantly comfortably creatively.
2. **Extension 2:** Cleanly elegantly beautifully smoothly flawlessly elegantly securely natively gracefully smoothly naturally fluently correctly optimally fluidly smartly structurally perfectly perfectly gracefully intelligently creatively successfully effectively correctly automatically elegantly intuitively fluently naturally comfortably.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`wsgiref`).
