import sys
import socket
import select


Usernames = {}
HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def who(sock):
    for name, socket in Usernames.iteritems():
        if socket == sock:
            return name

def privatemsg(name, data):
    for user in Usernames:
        if user in data:
            sock = Usernames[user]
            data = data.replace('send ' + str(user) + ' ', '')
            sock.send('private from ' + name + ': ' + data)

def users(sock):
    data = ''
    for user in Usernames:
        data += user + ', '
    sock.send(data)

def exit(sock):
    for name, socket in Usernames.iteritems():
        if socket == sock:
            SOCKET_LIST.remove(sock)
            broadcast(server_socket, sock, "Client %s is offline\n" % name) 
            del Usernames[name]
            
def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
    
    while 1:
        # get the list sockets which are ready to be read through select
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                name = sockfd.recv(RECV_BUFFER)
                Usernames[name] = sockfd
                print "Client %s connected" % name
                 
                broadcast(server_socket, sockfd, "%s entered our chatting room\n" % name)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        name = who(sock)
                        if data[:4] == 'send':
                            privatemsg(name, data)
                        elif data[:6] == 'show()':
                            users(sock)
                        elif data[:6] == 'exit()':
                            exit(sock)
                        else:
                            broadcast(server_socket, sock, "\r" + '[' + name + '] ' + data)  
                    else:
                        # remove the socket that's broken    
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        name = who(sock)
                        broadcast(server_socket, sock, "Client %s is offline\n" % name) 
 
                except:
                    name = who(sock)
                    broadcast(server_socket, sock, "Client %s is offline\n" % name) 
                    continue

    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(chat_server())
