
#We will use the socket library to create a server
import socket

##Global variables##
#The ammount of bytes that the server will receive.
HEADER = 64  #You can change this value as you need
#The format of the messages that the server will receive.
FORMAT = "utf-8"
#The message that the server will receive to disconnect the client.
DISCONNECT_MESSAGE = "GoodBye!" #You can use whatever message, but it MUST be the same as in unity.
#The port that the server will use.
PORT = 5050 #You can change this value as you need
#The IPV4 address of your computer.
SERVER = socket.gethostbyname(socket.gethostname()) #This function gets the IP by itself.
#You can change this line by this one if you want to use a specific IP:
#SERVER = "YOUR_IP" #Change this value to your IPV4 address.
addr = (SERVER, PORT)

#Function to handle the Unity client.
#You can also use this function as a thread to handle multiple Unity files at the same time.
def handle_client(client, address):
    print(f"Client conected: {address}")
    clientected = True
    while clientected: #Read the messages until the client disconnects.
        msg = client.recv(HEADER).decode(FORMAT) #Receive the message.
        if msg:
            print(f"Message received: {msg}")
            if msg == DISCONNECT_MESSAGE: #If the message is the disconnect message, disconnect the client.
                clientected = False
            else:
                handle_message(msg)
                send_message(msg + " received succesfully!", client)

    client.close() #Close the connection with the client.
    print(f"{address} disconnected.")

#Function to send a message to the client.
def send_message(msg, client):
    #Transform the message to bytes.
    message = msg.encode(FORMAT)
    #Send the message.
    client.send(message)

#Function to handle the message recieved from Unity.
#You can change this function to do whatever you want with the message.
def handle_message(msg):
    print(f"Message received: {msg}")

if __name__ == "__main__":
    ##Create and start the server##
    #Create the server.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(addr)
    #Start the server.
    server.listen()
    print(f"Server open on {SERVER}")
    #Wait for a client to connect.
    client, address = server.accept()
    #Handle the client.
    handle_client(client, address)
    #When the client disconnects, close the server.
    server.close()