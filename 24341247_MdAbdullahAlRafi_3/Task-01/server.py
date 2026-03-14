import socket

# Server configuration
server_port = 8080            
format ="utf-8"
buffer_for_message_length = 16



#Create the  Servers address
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

#Create a socket address
addr = (host_ip, server_port)


#Creating the socket for the client Ipv4, TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)


# Listen for incoming connections
server.listen()  
print(f"Server is listening")



#to keep the listening server running
while True:
    conn, add = server.accept()  # Accept a connection Object, Address
    print(f"Connected to {add}")

    connected = True
    while connected:
        message_length = conn.recv(buffer_for_message_length).decode(format)
        print(f"Upcoming message length: {message_length}")


        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(format)

            if message == "Disconnect":
                connected = False
                print(f"Terminating connection with {add}")
                conn.send("The session is terminated".encode(format))
                print("\n")

            else:
                print(message)
                conn.send("The server has received the message".encode(format))
                print("\n")


    conn.close()  # Close the connection after handling the client




               
