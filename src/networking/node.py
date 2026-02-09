from namedpipe import NPopen


class Node:
    pipe: NPopen

    def __init__(self, MAC: str, IP: str):
        self.pipe = NPopen(name=MAC)
        print(self.pipe)

    def __del__(self):
        self.pipe.close()
