import socket
import requests
#comment all Ctrl + /
#basic server for 1:1 communication not multithred

#SERVER IP -> To Access it from Internet specify Public IP of the server
def get_public_ip():
    try:
        # Using external service such as httpbin to get public ip
        response = requests.get('https://httpbin.org/ip')
        public_ip = response.json().get('origin')
        return public_ip
    except Exception as e:
        print(f"Error getting public ip: {e}")
        return None

get_public_ip_address = get_public_ip()

if get_public_ip_address:
    print(f"Public ip: {get_public_ip_address}")
else:
    print("can't get public ip address")


# SERVER IP -> On LAN
HOST = socket.gethostbyname(socket.gethostname())
print(f"The local server Ip is : {HOST}")

PORT = 9999

print(HOST)

# Define socket and it's type and it is just for accepting new communication only not the actual communication
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind this host ip with port to enable access to the server
server.bind((HOST, PORT))

# Try max 5 times to initiate connection
server.listen(5)

while True:
    # the socket here is for the actual communication
    # the server.accept() returns 2 values and we set those to corresponding vars com..socket & addr..
    # communication_socket is pipe for each new communication
    # address is the ip address of the incoming connection
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    # recieve buffer size of 1024 then decode it
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank You!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!".encode('utf-8'))
