#!/usr/bin/python

import network
import sys

walkMsg = "walk;"
stopMsg = "stop;"

conn = network.TextConnection()
address = '127.0.0.1'
port = 9001


def heard(phrase):
    # print "them:" + phrase
    pass


def serverConnect():
    conn.call(address, whenHearCall=heard, port=port)


def chat():
    print "Input a command: < stop or walk >"
    while conn.isConnected():
        phrase = raw_input()
        print "Send:" + phrase
        try:
            conn.say(phrase)
        except:
            conn.hangUp()
            serverConnect()
            conn.say(phrase)


def init(addr='127.0.0.1', p=9001):
    global address
    global port
    global conn
    
    address = addr
    port = p
    conn = network.TextConnection()
    serverConnect()


def walk():
    conn.say(walkMsg)


def stop():
    conn.say(stopMsg)


def main():
    if len(sys.argv) == 2:
        address = sys.argv[1]

    if len(sys.argv) == 3:
        address = sys.argv[1]
        port = sys.argv[2]
        
    print "Remote control program."
    while True:
        conn = network.TextConnection()
        serverConnect()
        chat()
        conn.hangUp()


if __name__ == '__main__':
    main()
