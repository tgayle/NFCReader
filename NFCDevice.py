# import nfc
from nfcproviders import NFCProviderUtil


class NFCDevice:
    def __init__(self, id) -> None:
        self.card_id = id
        self.pretty_card_id = NFCProviderUtil.insert_spaces_every_n_chars(id, 2, num_of_spaces=1)



