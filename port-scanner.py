#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("IP Address: ")
port = int(input("Port: "))


def portScanner(port):
  if s.connect_ex((host, port)):
    print('The port is closed.')
  else:
    print('The port is open.')

if __name__ == "__main__":
  portScanner(port)
