import nfc

class PN532Parser:
    def __init__(self, device) -> None:
        self.id = self.pretty_id_from_device(device)

    def pretty_id_from_device(self, device) -> str:
        """
        Returns the id of an NFC device from a device object from the nfc library.
        :param device: A device from the nfc library
        :return: str
        """
        string = nfc.str_nfc_target(device, False)[1]
        str_list = string.split("\n")
        uid = str_list[2].strip().replace("  ", " ")
        return uid[uid.index(": ") + 2:]

    def __str__(self) -> str:
        return self.id

