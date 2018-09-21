#copyright 2017-18 by aleok

############
# SETTINGS #
############
channel = "#channel"
server = "irc.freenode.net"
nickname = "nick"
passwordFileName = "pass.txt"

############
### CODE ###
############
import socket, sys, time

# Don't use unless you know what you're doing!
debug = False

pFile = open(passwordFileName, "r")
password = pFile.read()
pFile.close()

#Create socket
s = socket.socket()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def send(chan, msg):
    s.send(bytes("PRIVMSG " + chan + " :" + msg + "\r\n", "UTF-8"))
    
def connect(srvr, ch, botnick, passw):
    print("Connecting to: "+server)
    s.connect((srvr, 6667)) #Connect to the server
    s.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot\r\n", "UTF-8")) #User authentication
    s.send(bytes("NICK " + botnick + "\r\n", "UTF-8"))
    if passw:
        s.send(bytes('PRIVMSG NickServ :identify {}\r\n'.format(passw), 'UTF-8')) #Use password
    s.send(bytes("JOIN " + ch + "\r\n", "UTF-8")) #Join the channel specified


connect(server, channel, nickname, password)
while 1:
    msg = s.recv(2040)
    if debug:
        print(msg)
    if "JOIN" in str(msg):
        print("Joined channel.")
    if "You are now identified" in str(msg):
        print("Identified.")
        if len(sys.argv) == 1: #If no arguments given...
            print("Using default message.")
            send(channel, "Server shutting down in 10 minutes for backup.")
        else:
            print("Using sys.argv message.")
            send(channel, " ".join(sys.argv[1:]))
        s.send(bytes("QUIT\r\n", "UTF-8")) #Quit
        break
