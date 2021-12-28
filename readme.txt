https://en.wikipedia.org/wiki/Network_socket

A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. 
Sockets are created only during the lifetime of a process of an application running in the node.

Because of the standardization of the TCP/IP protocols in the development of the Internet, the term network socket is most commonly used in the context of the Internet protocol suite, and is therefore often also referred to as Internet socket. 
In this context, a socket is externally identified to other hosts by its socket address, which is the triad of transport protocol, IP address, and port number.

The term socket is also used for the software endpoint of node-internal inter-process communication (IPC), which often uses the same API as a network socket.


PORT Range
----------
A port number uses 16 bits: from 0 to 65535 decimal

Port numbers are divided into ranges:
- Port numbers 0-1023: Well known ports: RESERVED
- Ports 1024-49151: Registered Port: SEMI-RESERVER
- Ports 49152-65535: FREE TO USE

Ports are implemented at the transport layer as part of the TCP or UDP header 

(use netstat command to check active ports)


TCP and UDP
-----------
The TCP/IP protocol supports two types of port- TCP Port and UDP Port.
- TCP: connection orientated applications. It has built in error checking and will re transmit missing packets.
- UDP:connection less applications. It has no has built in error checking and will not re transmit missing packets.


SOCKET TYPE
-----------
- Stream sockets: enable processes to communicate using TCP. A stream socket provides a bidirectional, reliable, sequenced, and unduplicated flow of data with no record boundaries
- Datagram sockets: enable processes to use UDP to communicate
- Raw sockets: provide access to ICMP


TCP Sockets
-----------
A connection between two computers uses a socket.
A socket is the combination of IP address plus port
Each end of the connection will have a socket.


REFERENCES
----------

https://realpython.com/python-sockets/

https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be