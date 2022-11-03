//This script connects to the python server
//It includes examples of how to send and receive messages
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;

public class UnityClient : MonoBehaviour
{
    //Insert your IP here. It MUST be the same as the one in the python server
    public string IP = ""; 
    //Insert the port you want to use. It MUST be the same as the one in the python server
    public int port = 5050; 
    Socket client;
    // Start is called before the first frame update
    void Start()
    {
        //Create the client socket
        client = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        //This is the IP address of the computer running Python
        IPAddress ip = IPAddress.Parse(IP);
        //This is the port that Python is listening on
        IPEndPoint localEndPoint = new IPEndPoint(ip, port);
        //Connect the socket to the server
        client.Connect(localEndPoint);
        //Check if the socket is connected
        if (client.Connected)
        {
            Debug.Log("Socket connected to " + client.RemoteEndPoint.ToString());
        }
        else
        {
            Debug.Log("Socket not connected");
        }
    }

    //Function to send a message to python
    void send_message(string message)
    {
        //Convert the string to a byte array
        byte[] msg = System.Text.Encoding.ASCII.GetBytes(message);
        //Send the byte array to Python
        client.Send(msg);
    }

    //Function to receive a message from python
    void receive_message()
    {
        //Create a byte array to store the message.
        byte[] msg = new byte[1024];
        //Receive the message
        int bytesRec = client.Receive(msg);
        //Convert the byte array to a string
        string message = System.Text.Encoding.ASCII.GetString(msg, 0, bytesRec);
        //Print the message
        Debug.Log("Received: " + message);
    }

    // Update is called once per frame
    void Update()
    {   
        Debug.Log("");
        send_message("Hello World");
        receive_message();
    }

    //Function when the application is closed
    void OnApplicationQuit()
    {
        //Close the socket and send the disconnect message to python
        send_message("GoodBye!");
        client.Close();
    }
}