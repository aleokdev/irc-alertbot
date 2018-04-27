import socket, sys # this is a modified code found by the interwebz. mostly of this isn't written by me, and that's why it didn't work at first :P

irc = socket.socket()
  
def __init__(self):  
    self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
def send(chan, msg):
    irc.send(bytes("PRIVMSG " + chan + " :" + msg + "\r\n", "UTF-8"))
 
def connect(server, channel, botnick):
    #defines the socket
    print("connecting to:"+server)
    irc.connect((server, 6667))                                                         #connects to the server
    irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!\r\n", "UTF-8")) #user authentication
    irc.send(bytes("NICK " + botnick + "\r\n", "UTF-8"))               
    irc.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))        #join the chan
 
def get_text():
    text=irc.recv(2040)  #receive the text
 
    return text

channel = "##TommyTreasureMinetest"
server = "irc.freenode.net"
nickname = "alertbot3000"

connect(server, channel, nickname)
 
while 1:
    text = get_text()
    print(text)
    if "JOIN" in str(text):
        if sys.argv == []:
            send(channel, "Server shutting down in 10 minutes for Backup.")
        else:
            send(channel, " ".join(sys.argv[1:]))
        irc.close()
        break