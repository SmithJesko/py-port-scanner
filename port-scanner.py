#!/usr/bin/python3

import argparse
import socket

parser = argparse.ArgumentParser(description='Simple port scanner utility written in Python 3.')
parser.add_argument('-ip', '--IP', default='192.168.1.1', type=str, metavar= '', help='IP address to scan')
scanGroup = parser.add_mutually_exclusive_group()
scanGroup.add_argument('-f', '--full', action='store_true', help='Scan all ports')
scanGroup.add_argument('-ftp', '--FTP', action='store_true', help='Scan FTP (port 21)')
scanGroup.add_argument('-ssh', '--SSH', action='store_true', help='Scan SSH (port 22)')
scanGroup.add_argument('-http', '--HTTP', action='store_true', help='Scan HTTP (port 80)')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)

host = args.IP
ports = {
  'FTP': 21,
  'SSH': 22,
  'HTTP': 80
}

def singlePortScanner(scan, port):
  if s.connect_ex((host, port)):
    print('{} {} - Closed'.format(scan, port))
  else:
    print('{} {} - Open'.format(scan, port))

def portScanner():
  if args.FTP:
    print('FTP scan on server {}'.format(host))
    singlePortScanner('FTP', ports['FTP'])
  elif args.SSH:
    print('SSH scan on server {}'.format(host))
    singlePortScanner('SSH', ports['SSH'])
  elif args.HTTP:
    print('HTTP scan on server {}'.format(host))
    singlePortScanner('HTTP', ports['HTTP'])
  else:
    print('Full scan on server {}'.format(host))
    for scan, port in ports.items():
      if s.connect_ex((host, port)):
        print('{} {} - Closed'.format(scan, port))
      else:
        print('{} {} - Open'.format(scan, port))

if __name__ == "__main__":
  portScanner()