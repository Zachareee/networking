type MACaddr = str


def _valid_MAC(MAC: MACaddr):
    assert len(MAC) == 2, "invalid MAC string"
