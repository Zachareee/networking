from dataclasses import dataclass
from typing import override
import socket

from networking.log_format import create_logger
from networking.frames import MAC_frame
from networking.protocol import MACaddr

logger = create_logger(__name__)


@dataclass
class Node:
    MAC: MACaddr
    IP: int
    __socket: socket.SocketType

    def rcv_MAC_frame(self) -> MAC_frame:
        frame = MAC_frame(self.MAC, "bo", "hello")
        logger.info(f"rcving {frame.data} from {
                    frame.destination} to {frame.source}")
        return frame

    def send_MAC_frame(self, dst: MACaddr, data: str):
        logger.info(f"sending {data} from {self.MAC} to {dst}")
        MAC_frame(self.MAC, dst, data)

    def resolve_MAC(self, dst: MACaddr):
        pass

    @override
    def __init__(self, node_config: dict):
        self.MAC = node_config["MAC"]
        self.IP = node_config["IP"]
        self.__socket = socket.create_server(
            ("127.0.0.1", node_config["port"]))

    def __del__(self):
        self.__socket.close()
        logger.info("closing node")
