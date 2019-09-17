#!/usr/bin/python3

import argparse
import socket

parser = argparse.ArgumentParser(description='Simple port scanner utility written in Python 3.')
parser.add_argument('-ip', '--IP', default='192.168.1.1', type=str, metavar= '', help='IP address to scan')
# parser.add_argument('-p', '--port', default=22, type=int, metavar='', help='Port to scan')
scanGroup = parser.add_mutually_exclusive_group()
scanGroup.add_argument('-f', '--full', action='store_true')
scanGroup.add_argument('-ftp', '--FTP', action='store_true')
scanGroup.add_argument('-ssh', '--SSH', action='store_true')
scanGroup.add_argument('-http', '--HTTP', action='store_true')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(5)

host = args.IP
ports = {
  'FTP': 21,
  'SSH': 22,
  'HTTP': 80
}

def portScanner():
  for scan, port in ports.items():
    if s.connect_ex((host, port)):
      print('{} {} - Closed'.format(scan, port))
    else:
      print('{} {} - Open'.format(scan, port))

if __name__ == "__main__":
  portScanner()