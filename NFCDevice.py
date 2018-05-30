import nfc


class NFCDevice:
    def __init__(self, device) -> None:
        self.pretty_id = pretty_id_from_device(device)
        self.id = self.pretty_id.replace(" ", "")


def pretty_id_from_device(device: NFCDevice) -> str:
    _, string = nfc.str_nfc_target(device, False)
    str_list = string.split("\n")
    uid = str_list[2].strip().replace("  ", " ")
    return uid[uid.index(": ") + 2:]