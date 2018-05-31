import nfc


class NFCDevice:
    def __init__(self, device) -> None:
        self.pretty_card_id = pretty_id_from_device(device)
        self.card_id = self.pretty_card_id.replace(" ", "")


def pretty_id_from_device(device) -> str:
    """
    Returns the id of an NFC device with spaces every two characters.
    :param device: A device from the nfc library
    :return: str
    """
    string = nfc.str_nfc_target(device, False)[1]
    str_list = string.split("\n")
    uid = str_list[2].strip().replace("  ", " ")
    return uid[uid.index(": ") + 2:]
