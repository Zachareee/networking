from sys import argv, executable
from yaml import load, Loader

from networking.node import Node
from networking.wire import Wire

with open("config.yaml") as f:
    data = load(f.read(), Loader)

if len(argv) < 3:
    print(f"usage: {executable} {argv[0]} node|wire|router NAME")
    exit(1)

if argv[1] == "node":
    Node(data["nodes"][argv[2]]).send_MAC_frame(
        "N2", input("Enter your message: "))


if argv[1] == "wire":
    Wire(data["wires"][int(argv[2])], data["nodes"]).forward()
