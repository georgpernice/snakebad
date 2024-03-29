from secret import USER, PWD
class CommandCreator():
    def __init__(self, socket):
        self.sock = socket
    def _send(self, str):
        self.sock.send(bytearray(str.encode("utf-8")))
    def chat(self, msg):
        string = "chat|" + msg + "\n"
        self.sock.send(bytearray(string.encode("utf-8")))
    def join(self):
        return self._send(f"join|{USER}|{PWD}\n")
    def up(self):
        return self._send("move|up\n")
    def left(self):
        return self._send("move|left\n")
    def right(self):
        return self._send("move|right\n")
    def down(self):
        return self._send("move|down\n")