from NFCDevice import NFCDevice


class NFCProvider:

    def scan_for_device(self) -> (bool, NFCDevice):
        raise RuntimeError("Device scanning has not be implemented.")

    def close(self):
        # Closes an NFCProvider
        raise RuntimeError("Closing has not been implemented.")