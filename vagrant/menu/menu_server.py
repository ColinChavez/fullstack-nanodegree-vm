#!/usr/bin/env python2.7.12
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi #commongatewayinterface, deciphers the message that was sent from the server

#import CRUD Operations from Lesson 1
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Handler code indicates what code to execute based on the type of HTTP requests that is sent to the server.
class webServerHandler(BaseHTTPRequestHandler): #Defines the webserverHandler class that I called in my HTTPServer in main method and have it extend from a class called BaseHTTPRequestHandler.

    def do_GET(self): #Handles all get requests that our web server receives.
        try: #In order to figure out which resource we are trying to access, we will use a simple pattern matching plan that only looks for the ending of our URL path 
            # Objective 3 Step 2 - Create /restaurants/new page
            if self.path.endswith("/restaurants/new"):#The BaseHTTPRequestHandler provides us a variable called path that contains the URL sent by the client to the server as a string. I will make an if statement that looks for the URL that ends with /hello.
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
                output += "<input name='newRestaurantName' type='text' placeholder = 'New Restaurant Name'>"
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id = restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output += "<html><body>"
                    output += "</h1>"
                    output += myRestaurantQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                    output += "<input name='newRestaurantName' type='text' placeholder = '%s' >" % myRestaurantQuery.name
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]

                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id = restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output += ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)



            if self.path.endswith("/restaurants"):#The BaseHTTPRequestHandler provides us a variable called path that contains the URL sent by the client to the server as a string. I will make an if statement that looks for the URL that ends with /hello.
                restaurants = session.query(Restaurant).all()#I learned to place query above headers
                output = "" #I left this out in my solution.
                #Objective 3 Step 1 - Create a Link to create a new menu item
                output += "<a href = '/restaurants/new'> Make a New Restaurant Here </a></br></br>"

                self.send_response(200)#Tell the server to send a successful GET request
                self.send_header('Content-type', 'text/html')#Use the send_header function to indicate that I'm replying with text in the form of HTML to my client. 
                self.end_headers()#The end_headers command which just sends a blank line indicating the end of our HTTP headers in the response.
                output += "<html><body>"#I left this out of my solution
                for restaurant in restaurants:#My for loop was correct! ;) 
                    output += restaurant.name #My solution was output = restaurant.name
                    output += "</br>"#Add all of the restaurant menu items to my output stream and separate with break lines
                    # Objective 2 -- Add Edit and Delete Links
                    # Objective 4 -- Replace Edit href
                    output += "<a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "</br>"
                    output += "<a href='/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output += "</br></br></brl>"

                output += "</body></html>"
                self.wfile.write(output)#this functions sends a message back to the client
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        # Objective 3 Step 3- Make POST Method
        def do_POST(self):#Created method do_POST, which overrides the method in the base http request handler superclass, just like doGET.
            try:
                if self.path.endswith('/delete'):
                    restaurantIDPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id = restaurantIDPath).one()
                    if myRestaurantQuery:
                        session.delete(myRestaurantQuery)
                        session.commit()
                        session.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

                if self.path.endswith("/edit"):
                    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))#cgi.parse_header function parses an HTML form header, such as content type,into a main value and dictionary of parameters
    
                    if ctype == 'multipart/form-data':#After that, we check to see if this is form data being received
                        fields = cgi.parse_multipart(self.rfile, pdict)#Made a variable called fields, which we use the cgi.parse_multipart to collect all of the fields in a form.
                        messagecontent = fields.get('newRestaurantName')#Made a variable called message content to get out the value of a specific field or set of fields and store them in an array, I will call this field message here, and when I create my HTML form
                        restaurantIDPath = self.path.split("/")[2]

                        myRestaurantQuery = session.query(Restaurant).filter_by(
                            id = restaurantIDPath).one()
                        if myRestaurantQuery != []:
                            myRestaurantQuery.name = messagecontent[0]
                            session.add(myRestaurantQuery)
                            session.commit()
                            self.send_response(301)
                            self.send_header('Content-type', 'text/html')
                            self.send_header('Location', '/restaurants')
                            self.end_headers()

                if self.path.endswith("/restaurants/new"):
                    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))#cgi.parse_header function parses an HTML form header, such as content type,into a main value and dictionary of parameters
    
                    if ctype == 'multipart/form-data':#After that, we check to see if this is form data being received
                        fields = cgi.parse_multipart(self.rfile, pdict)#Made a variable called fields, which we use the cgi.parse_multipart to collect all of the fields in a form.
                        messagecontent = fields.get('newRestaurantName')#Made a variable called message content to get out the value of a specific field or set of fields and store them in an array, I will call this field message here, and when I create my HTML form

                        # Create new Restaurant Object
                        newRestaurant = Restaurant(name = messagecontent[0])
                        session.add(newRestaurant)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            except:
                pass


#Main Method instantiates our server and specifies what port it will listen on
def main():
    try:#Python interpreter will try to attempt the code inside the try block.
        server = HTTPServer(('', 8080), webServerHandler) #creates an instance of the HTTP server class
        print 'Web Server running... open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt: #if a defined event occurs we can exit out of the code with an exception.
        print " ^C entered, stopping web server...."
        server.socket.close()
#Runs the main method when the Python interpreter executes my script
if __name__ == '__main__':
    main()