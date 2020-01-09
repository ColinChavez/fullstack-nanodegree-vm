#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
from cgi import parse_header, parse_multipart
import urllib
from urllib.parse import parse_qs
import ctypes
import cgitb
cgitb.enable()

class webserverHandler(BaseHTTPRequestHandler):
    form_html = \
        '''
        <form method='POST' enctype='multipart/form-data' action='/hello'>
        <h2>What would you like me to say?</h2><input name='message' type ='text'>
        <input type='submit' value='Submit'></form>
        '''

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html>" \
                          " <body" \
                          "     Hello!<br>" + self.form_html + \
                          " <body>" \
                          "</html>"
                #self.wfile.write(bytes(output, "utf-8"))
                self.wfile.write(output.encode())
                print (output)
                #return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                #output = ""
                output += "<html>" \
                          "     <body>" \
                          "         &#161 Hola! <br>" + self.form_html + \
                          "         <a href = '/hello' >Back to Hello</a>" \
                          "     </body>" \
                          "</html>"
                #self.wfile.write(bytes(output, "utf-8"))
                self.wfile.write(output.encode())
                print(output)
                #return

        except IOError:
            self.send_error(404, "File Not Found {}".format(self.path))

    def do_POST(self):
        try:
            self.send_response(200) 
            self.send_header('Content-type', 'text/html')
            self.end_headers

            #ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
            #content_len = int(self.headers.get('Content-length'))
            #pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            #pdict["CONTENT-LENGTH"] = content_len
            #if ctype == 'multipart/for-data':
            #fields = cgi.parse_multipart(self.rfile, pdict)
            #messagecontent = fields.get('message')

            ctype, pdict = cgi.parse_header(self.headers['content-type'])

            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

            #content_len = int(self.headers.get('Content-length'))
            #pdict["CONTENT-LENGTH"] = content_len

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> {} </h1>".format(messagecontent[0].decode())
            output += self.form_html
            output += "</body></html>"
            self.wfile.write(bytes(output, "utf-8"))
            print (output)
           #return   

        except:
            raise

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print ("Web server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print ("^C entered, stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    main()