from werkzeug.wrappers import Request, Response


class Middleware():
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        if request.full_path.startswith(('/static', 'favicon')) or 'session' in request.cookies:
            return self.app(environ, start_response)

        response = False
        routes = ['/data', '/user/create', '/auth/login']
        route = request.full_path

        while route[-1] == '/' or route[-1] == '?':
            if route == '/':
                break
            route = route[:-1]

        for i in routes:
            if i == route:
                response = True

        if response:
            return self.app(environ, start_response)

        res = Response(u'Authorization failed',
                       mimetype='text/plain', status=401)
        return res(environ, start_response)
