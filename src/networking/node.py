from namedpipe import NPopen
from networking.log_format import CustomFormatter, create_logger

logger = create_logger(__name__)


class Node:
    MAC: str
    IP: str
    __MACpipe: NPopen
    __IPpipe: NPopen

    def __init__(self, MAC: str, IP: str):
        self.MAC = MAC
        self.IP = IP
        self.__MACpipe = NPopen(name=MAC)
        self.__IPpipe = NPopen(name=IP)
        logger.info(self.__MACpipe)
        logger.info(self.__IPpipe)

    def __del__(self):
        logger.info("closing pipes")
        self.__MACpipe.close()
        self.__IPpipe.close()
