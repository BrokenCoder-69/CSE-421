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

                hours = int(message)
                salary = 0


                if hours <= 40:
                    salary = 200 * hours


                else:
                    salary = 8000 + (hours - 40) * 300
                    
                response = f"The salary for {hours} hours of work is: Tk {salary}"
                print(response)
                conn.send(response.encode(format))

                conn.send("The server has received the message".encode(format))
                print("\n")

    conn.close()  # Close the connection after handling the client

            
# 4. Create a basic client-server program where the server takes the number of hours a person worked from the client and calculates the person’s salary.
# If the hours worked is less than or equal to 40, then the person receives Tk 200 per hour.
# If the hours worked is greater than 40, then the person receives Tk 8000 plus Tk 300 for each hour worked over 40 hours.
# The client will provide how many hours the person worked to the server and the server will calculate the salary and send it to the client.
