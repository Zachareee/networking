from sys import argv, executable
from yaml import load, Loader

from networking.node import Node
from networking.wire import Wire
# from networking.frames import MAC_frame

# print(MAC_frame.from_bytes(bytes(Node("al", 0x5).rcv_MAC_frame())))

with open("config.yaml") as f:
    data = load(f.read(), Loader)

if len(argv) < 3:
    print(f"usage: {executable} {argv[0]} node|wire|router NAME")
    exit(1)

if argv[1] == "node":
    Node(data["nodes"][argv[2]]).rcv_MAC_frame()

if argv[1] == "wire":
    Wire(data["wires"][int(argv[2])], data["nodes"])
