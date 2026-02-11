from networking.node import Node
from networking.frames import MAC_frame

print(MAC_frame.from_bytes(bytes(Node("al", 0x5).rcv_MAC_frame())))
