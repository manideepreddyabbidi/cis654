# -*- coding: utf-8 -*-
"""Server.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gd3bF_JwHJ5glCEsHpVXA6ATAPY3K2Jt
"""

import socket

def isPalindrome(s):
    return s == s[::-1]

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 7501)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Server is listening on port 7501 ...")

    while True:
        client_socket, client_address = server_socket.accept()

        try:
            print("Client address", client_address)
            data = client_socket.recv(1024)
            if data:
                string = data.decode()
                if isPalindrome(string):
                    response = "It is a palindrome"
                else:
                    response = "It is not a palindrome"

                client_socket.sendall(response.encode())

        finally:
            client_socket.close()

if __name__ == "__main__":
    main()