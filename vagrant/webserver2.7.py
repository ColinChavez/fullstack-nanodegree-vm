#!/usr/bin/env python2.7.12
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi#commongatewayinterface, deciphers the message that was sent from the server

#Handler code indicates what code to execute based on the type of HTTP requests that is sent to the server.
class webServerHandler(BaseHTTPRequestHandler): #Defines the webserverHandler class that I called in my HTTPServer in main method and have it extend from a class called BaseHTTPRequestHandler.

    def do_GET(self): #Handles all get requests that our web server receives.
        try: #In order to figure out which resource we are trying to access, we will use a simple pattern matching plan that only looks for the ending of our URL path 
            if self.path.endswith("/hello"):#The BaseHTTPRequestHandler provides us a variable called path that contains the URL sent by the client to the server as a string. I will make an if statement that looks for the URL that ends with /hello.
                self.send_response(200)#Tell the server to send a successful GET request
                self.send_header('Content-type', 'text/html')#Use the send_header function to indicate that I'm replying with text in the form of HTML to my client. 
                self.end_headers()#The end_headers command which just sends a blank line indicating the end of our HTTP headers in the response.
                output = ""#Create some content to send back to the client
                output += "<html><body>"#
                output += "<h1>Hello!</h1>"#add HTML message to my output stream
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)#this functions sends a message back to the client
                print output
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):#Created method do_POST, which overrides the method in the base http request handler superclass, just like doGET.
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))#cgi.parse_header function parses an HTML form header, such as content type,into a main value and dictionary of parameters
            if ctype == 'multipart/form-data':#After that, we check to see if this is form data being received
                fields = cgi.parse_multipart(self.rfile, pdict)#Made a variable called fields, which we use the cgi.parse_multipart to collect all of the fields in a form.
                messagecontent = fields.get('message')#Made a variable called message content to get out the value of a specific field or set of fields and store them in an array, I will call this field message here, and when I create my HTML form
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]#Returns the first value of the array that was submitted when I created my form
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)#Send the output out to the server
            print output#print out the output for debugging.
        except:
            pass

#Main Method instantiates our server and specifies what port it will listen on
def main():
    try:#Python interpreter will try to attempt the code inside the try block.
        port = 8080
        server = HTTPServer(('', port), webServerHandler) #creates an instance of the HTTP server class
        print "Web Server running on port %s" % port #Server address is a tuple that contains the host and port number for our server.
        server.serve_forever()
    except KeyboardInterrupt: #if a defined event occurs we can exit out of the code with an exception.
        print " ^C entered, stopping web server...."
        server.socket.close()
#Runs the main method when the Python interpreter executes my script
if __name__ == '__main__':
    main()