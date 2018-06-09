import socket
import select

class Server:

    def __init__(self):
        self.players = {} #the name of the clients
        self.ledder = {1 : 36, 4 : 14, 9 : 31, 21 : 42, 28 : 84, 51 : 67, 71 : 91, 80 : 100}
        self.snakes = {17 : 7, 54 : 34, 62 : 19, 64 : 60, 87 : 24, 93 : 73, 95 : 75, 98 : 79}
        self.counter = 0
        self.colors = ['red', 'yellow', 'green', 'blue']
        self.CONNECTION_LIST = [] # list of socket clients
        self.RECV_BUFFER = 4096 
        self.PORT = 5018
        self.server_socket = None

    def closeConnection(self):
        self.server_socket.close()

    def Get_Name(self, sock):
        index = self.CONNECTION_LIST.index(sock) - 1
        for name in self.players:
            if index == 0:
                return name
            index = index - 1



    
    def create(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", self.PORT))
        self.server_socket.listen(10)
        
        # Add server socket to the list of readable connections
        self.CONNECTION_LIST.append(self.server_socket)

    
    def broadcast(self,message):
        for socket in self.CONNECTION_LIST:
            # send the message only to peer
            if socket != self.server_socket:
                try :
                    socket.send(message)
                except :
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in self.CONNECTION_LIST:
                        name = self.Get_Name(socket)
                        del players[name]
                        self.CONNECTION_LIST.remove(socket)

                                               
    def login(self):
        game_wait=True
        while game_wait:
            # Get the list sockets which are ready to be read through select
            read_sockets,write_sockets,error_sockets = select.select(self.CONNECTION_LIST,[],[]) 
            for sock in read_sockets:
                #New connection
                if sock == self.server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    sockfd, addr = self.server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)               
                #Some incoming message from a client
                else:
                    # Data recieved from client, process it
                    try:
                        #In Windows, sometimes when a TCP program closes abruptly,
                        # a "Connection reset by peer" exception will be thrown
                        data = sock.recv(self.RECV_BUFFER)
                        # echo back the client message
                        if data:
                            if "disconnecttt"==data:
                                name = self.Get_Name(sock)
                                print "Client " + str(name) + " is offline"
                                del self.players[name]
                                sock.close()
                                self.CONNECTION_LIST.remove(sock)
                                if len(self.CONNECTION_LIST)==1:
                                    game_wait=False

                            elif "nameeeeeeeeee" in data:
                                data2 = data.split(' ')
                                self.players[str(data2[1])] = self.colors[self.counter]
                                self.counter = self.counter + 1
                                print "Client " + str(data2[1]) + " is online"

                            elif 'move' in data:
                                data2 = data.split(' ')
                                final = int(data[2]) + int(data[3])
                                if final in ledder:
                                    final = ledder[final]
                                elif final in snakes:
                                    final = snakes[final]
                                message = 'move' + ' ' + str(players[data2[1]]) + ' ' + str(final) + ' ' + str(data2[3])
                                broadcast(message)

                    except:
                        name = self.Get_Name(sock)
                        print "Client " + str(self.players[name]) + " is offline"
                        del self.players[name]
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        if len(self.CONNECTION_LIST)==1:
                            game_wait=False
                        continue

def main():
    server = Server()
    server.create()
    server.login()
    server.closeConnection()
    print "bye bye"


   
if __name__ == "__main__":
    main()
