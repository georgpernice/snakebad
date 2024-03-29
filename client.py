# echo-client.py
import socket
from agent import Agent

HOST = "192.168.0.131"  # The server's hostname or IP address
PORT = 4000  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    agent = Agent(s)
    while True:
        data = s.recv(1024)
        if data:
            # parsing event and args
            idx = data.decode().find("\n")
            msg = data.decode()[:idx]
            args = msg.split("|") if "|" in msg else msg
            if isinstance(args,list):
                event = args[0] 
                args = args [1:]
            else:
                event = "tick" 
                args = None
            # pass event and args to agent
            agent.act(event, args)
            # log the server input
            print(msg)
