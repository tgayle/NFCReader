from urllib3.exceptions import MaxRetryError

from NFCDevice import NFCDevice
from nfcproviders.NFCProvider import NFCProvider
from tests.MockScanResponse import MockScanResponse
from nfcproviders import NFCProviderUtil as Util

import requests as net


_mock_scan_response = """ISO/IEC 14443A (000 kbps) target:
                             ATQA (SENS_RES): 00  00
                                UID (NFCID1): 00  00  00  00
                               SAK (SEL_RES): 00
                                         ATS: 00  00  00  00 
                          """


class MockNFCProvider(NFCProvider):
    def __init__(self) -> None:
        self.current_scan_response = MockScanResponse()

    def scan_for_device(self) -> (bool, NFCDevice):
        try:
            web_response = net.get("http://localhost:3000/id").json()
            if Util.is_card_id_valid(web_response['uid']):
                return True, NFCDevice(str(web_response['uid']))
        except (Exception):
            pass
        return False, None

    def close(self):
        return "Close called."

    def clear_scan_response(self):
        self.current_scan_response.clear()

    def update_scan_response(self, new_id) -> None:
        self.current_scan_response.update_response(uid=new_id)
