import os, sys, functools, http.server
sys.stderr = open(os.devnull, 'w')
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('0.0.0.0', 8000), functools.partial(QuietHandler, directory=sys.argv[1])).serve_forever()
