import socket

# Case 1 : get to the server On LAN, so specify IP of the server
#HOST = '127.0.1.1'
HOST = socket.gethostbyname(socket.gethostname())
# Case 2 : get a static public ip for the running server which is not on your machine
# Try using Ngrok or send the server public IP from the running server to a shared FOLDER
# Try upload the server ip to s3 buket as an object file then read the file to get the ip
PORT = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))