#!/usr/bin/env python
# Basic HTTP program to read URL request and respond accordingly
# Author: Alok Umesh Rajput
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from urlparse import urlparse, parse_qsl
from mypackage import get_greetings

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Assuming request made is http://localhost:8080/getAccountDetails?accountno=nnnnn
        # Use self.path to get the request context or node /getAccountDetails?accountno=nnnnn
        url=self.path
        if(url != "/favicon.ico"):
            print "Path {}".format(url)
            page, query = self.path.split('?')
            print "Page {}".format(page)
            print "Query {}".format(query)
            # Use below dictionary generator to parse all the url query parameter
            query_dict = dict(pair.split('=') for pair in query.split('&'))
            print "Query Dictionary {}".format(query_dict)
            q1 = query_dict["q1"]
            # Get these parameters from request and create a defintion here to incorprate your response and call it passing parameter
            self.wfile.write(get_greetings(q1))
    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
    
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
