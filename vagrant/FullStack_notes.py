#FullStack Notes

#Client - computer that wants information
#Server - computer that has the information that can be shared with the clients

#Client has to initiate communication to request information
#Server constantly stays listening for any clients to communicate with it and responds with the data that the client requested.

#Protocols - are like grammatical rules that we use to make sure all machines on the internet are communicating in the same way.

#TCP Transmission Control Protocol (TCP)
#Enables information to be broken into small packets and sent between clients and servers
#If a packet is lost somewhere along the way the send and receiver have a way of figuring out which of the packets is missing and request that they be resent.

#UDP - counterpart to TCP (User Datagram Protocol)
#Used for streaming content like music or video

#IP Internet Protocol (IP) - Similar to Postal addresses, IP addresses allow messages to properly routed to all participants on the internet.
# Statically or Dynamically assigned by the internet service provider (ISP)
#When I type google.com into my browser my computer first figures out the IP address of google by looking it up in a Domain Name Server or (DNS)

#DNS - Domain Name Server 
#Think of DNS as a big online phonebook that finds the IP address of web URLs.
#Once the DNS gives my computer the IP address, it uses that address to initiate communication with the server for Google.

#Ports - Since multiple applications using the internet can run on one machine,
#Operating systems use ports to designat channels of communications on the same IP address.
#Placing a colon after an IP address with another number indicates that we want to communicate on a specific port on the device using that IP address.
#Ports can rant from 0 - 65,536
#0-10,000 are often times reserved by the operating system for a specific use.
#Port 80 is the most common port for web servers.
#8080 is also a common port for web communication

#localhost - when client and server applications are on the same machine we indicate this with the term localhost
#local host has a special ip address of 127.0.0.1
#Whenever we type the local host ip address into a browser or web app, the operations system knows to look for this resource locally and not go out to the internet.

#Hypertext Transfer Protocol (HTTP)
#The main concept of HTTP is that clients tell servers what they want by using an HTTP verb, also known as an HTTP method.
# There are 9 HTTP verbs in the current HTTP specification.
# The two most commonly used methods for webites are GET and POST.

#GET request can be though of as the client telling a server, "get me some information that you have."
#GETs are sometimes called safe methods since they are only used to retrieve existing data from the database.
#POST can be though of as the client saying, "I want to modify some information that you have."
#POSTs call for data to be added, removed, or changed on the server.

#STATUS CODES - The server's reply to a client as to what happened after a specific request.
#in addition to a status code a server can also supply any requested resources the client requested 
#such as HTML, CSS, JAVASCRIPT, and media files such as images and audio.

#200: Successful GET
#200,201,303: Successful POST 
#301: Permanent REDIRECT - used to send a browser to a different URL
#404: File Not Found


