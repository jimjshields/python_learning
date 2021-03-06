import asyncore
import socket

CLIENTS = []

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        print "GOT", data,
        if data:
            bad_clients = []

            # for each connected client
            for i, sock in enumerate(CLIENTS):
                try:
                    # send them the response
                    sock.send(data)
                except:
                    print "Socket bad", sock
                    bad_clients.append(i)

            print "Removing clients", bad_clients
            for i in bad_clients:
                del CLIENTS[i]

        # self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        print "pair", pair
        if pair is not None:
            sock, addr = pair
            # save their socket in the clients list
            CLIENTS.append(sock)
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)
asyncore.loop()