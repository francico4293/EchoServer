# Author: Colin Francis
# Description: An echo server used to broadcast messages to connected clients

from socket import *
import os
from sys import *


class EchoServer(object):
    """Constructor for EchoServer class object"""
    def __init__(self, serverAddr: str, serverPort: int) -> None:
        self._serverAddr = serverAddr
        self._serverPort = serverPort
        self._backlog = 10
        self._clientPool = []

    def _handleSIGCLD(self) -> None:
        pass

    """"""
    def _createListenSocket(self) -> socket:
        # create TCP socket
        listenSocket = socket(AF_INET, SOCK_STREAM)
        # bind socket to specified address at specified port
        listenSocket.bind((self._serverAddr, self._serverPort))
        # mark socket as a listening socket with specified backlog
        listenSocket.listen(self._backlog)
        # display "server running" message to user
        print("[+] Server running on port {}".format(self._serverPort))
        # return listen socket back to calling function
        return listenSocket
    
    """Starts the server such that it begins listening for client connections"""
    def start(self) -> None:
        listenSocket = self._createListenSocket()
        

if __name__ == "__main__":
    s = EchoServer("127.0.0.1", 59028)
    s.start()
