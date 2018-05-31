from nfcproviders.NFCProvider import NFCProvider
from NFCDevice import NFCDevice
import nfc


class PN532Provider(NFCProvider):
    def __init__(self) -> None:
        self.context = nfc.init()
        self.scanner = nfc.list_devices(self.context, 2)[0]

        self.listener = nfc.open(self.context, self.scanner)
        self.modulation = nfc.modulation()
        self.modulation.nmt = nfc.NMT_ISO14443A
        self.modulation.nbr = nfc.NBR_106

    def scan_for_device(self) -> (bool, NFCDevice):
        """
        :return: A tuple (boolean, NFCDevice)
        boolean -> whether or not a device was found
        NFCDevice -> the device that was found, otherwise None
        """
        number_devices_found, devices = nfc.initiator_list_passive_targets(self.listener, self.modulation, 1)
        if number_devices_found <= 0:
            return False, None
        return True, NFCDevice(devices[0])

    def close(self):
        nfc.close(self.listener)
        nfc.exit(self.context)