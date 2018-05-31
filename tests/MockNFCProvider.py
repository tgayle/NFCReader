from NFCDevice import NFCDevice
from nfcproviders.NFCProvider import NFCProvider


_mock_scan_response = """ISO/IEC 14443A (000 kbps) target:
                             ATQA (SENS_RES): 00  00
                                UID (NFCID1): 00  00  00  00
                               SAK (SEL_RES): 00
                                         ATS: 00  00  00  00 
                          """


class MockNFCProvider(NFCProvider):
    def __init__(self) -> None:
        self.current_scan_response = None

    def scan_for_device(self) -> (bool, NFCDevice):
        return True, NFCDevice(self.current_scan_response)

    def close(self):
        return super().close()