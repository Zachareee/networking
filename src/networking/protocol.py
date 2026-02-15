from typing import TypeIs

MACaddr = str


def _valid_MAC(MAC: str) -> TypeIs[MACaddr]:
    return isinstance(MAC, str) and len(MAC) == 2
