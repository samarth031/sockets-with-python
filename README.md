# sockets-with-python
My sockets implementation with notes

Networking Basics

IP ADDRESSES:-
IP Address: The way of locating your device through the internet
e.g: when a computer has to communicate with another computer, it needs the IP address of the other computer
Google's definition of IP address: A unique string of numbers separated by full stops that identifies each computer using the Internet Protocol to communicateover a network
IP
1> Static IP - IP adresses never change(eg: Servers and Websites)
2> Dynamic IP - IP adress keeps changing(eg: Your Computer, Mobile Devices)

Find out Static IP b: ifconfig(linux based), ipconfig(windows)
Find out Dynamic IP by: "Type Whats my IP" on google


PORTS:-
Ports are numbers like house numbers for precise identification
Protocol - Port#
HTTP - 80
SSH - 22
HTTPS - 443
FTP - 20
SMTP - 25
POP3 - 110

SOCKETS:-
A Socket is one endpoint of a two way communication link between two programs running on a network
 A socket is bound to a port number so that TCP layer can identify the program that the data is destined to be sent to
 An Endpoint is a combination of IP & Port

 
