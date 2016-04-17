"""
Port scanner tool testing
16 April 2016
"""

import optparse
from socket import *
import socket
import sys


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('Test\n')
        results = connSkt.recv(1024)
        print "{0} tcp open".format(tgtPort)
        print "Results: {0}".format(str(results))
        connSkt.close()
    except Exception as e:
        print "{0} tcp closed".format(tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "Can't get host by name."
    try:
        tgtName = gethostbyaddr(tgtIP)
        print "Scan results for: {0}".format(tgtName[0])
    except:
        print "Scan results for: {0}".format(tgtIP)
    setdefaulttimeout(10)

    for tgtPort in tgtPorts:
        connScan(tgtHost, int(tgtPort))

def main():
    parser = optparse.OptionParser()
    parser.add_option('--host',dest='tgtHost', help='Host to target')
    parser.add_option('-p', dest='tgtPort', help='Specify ports seperated by comma')

    (options, args) = parser.parse_args()
    if not options.tgtHost:
        parser.print_help()
        sys.exit(1)
    elif not options.tgtPort:
        parser.print_help()
        sys.exit(1)


    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    portScan(tgtHost,tgtPorts)

if __name__ == "__main__":
    main()
