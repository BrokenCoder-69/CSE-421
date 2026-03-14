import socket


server_port = 8080            
format ="utf-8"
buffer_for_message_length = 16



#Create the  Servers address
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

#Create a socket address
addr = (host_ip, server_port)


#Creating the socket for the client Ipv4, TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(addr)

def message_to_be_sent(message):        #"Hi"
    # Encode the message to bytes
    msg = message.encode(format)
    #
    # Get the length of the message
    msg_length = str(len(message))           #2
    msg_length = msg_length.encode(format)

    # Pad the message length to a fixed size
    padding = b" " * (buffer_for_message_length - len(msg_length))
    msg_length += padding

    client.send(msg_length)
    client.send(msg)


    print(client.recv(2048).decode(format))






message_to_be_sent(f"48")
message_to_be_sent(f"10")

message_to_be_sent("Disconnect")

# while True:
#     user_input = input("Enter a message to send (or type 'Disconnect' to exit): ")
#     message_to_be_sent(user_input)

#     # If the user types "Disconnect", send the disconnect message and break the loop
#     if user_input.lower() == "disconnect":
#         break
