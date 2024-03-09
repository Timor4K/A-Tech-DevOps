client server comm on the same Local Area Network ? I have IP address accessible only locally

Port Number is like a door for a room (could be more than one door to the room)

On the internet i have a different Public IP address:
The Router-
The Internet-

Requests to the server on my local machine -
use my public ip address to get access to my local server
which has it's own private ip address on the local network
you have to implement a bind between the private ip of the server and the public ip

SOCKETS
is just a communication end point
os -> os
IR, IP, BT ,
+Internet Sockets... AF_INET
 - SOCK_STREAM (TCP)
 - SOCK_DGRAM (UDP)

