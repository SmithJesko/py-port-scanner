#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.1"
port = 22

def portScanner(port):
  if s.connect_ex((host, port)):
    print('The port is closed.')
  else:
    print('The port is open.')

if __name__ == "__main__":
  portScanner(port)
