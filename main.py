import websockets
import nfc
import time
from nfcproviders.NFCProvider import NFCProvider
from nfcproviders.PN532Provider import PN532Provider
from tests.MockNFCProvider import MockNFCProvider


def current_milli_time():
    return int(round(time.time() * 1000))


def read_single_card(nfc_provider: NFCProvider):
    was_device_found, device = nfc_provider.scan_for_device()
    # while not was_device_found:
    #     was_device_found, device = nfc_provider.scan_for_device()
    return device


def wait_for_card_remove(nfc_provider: NFCProvider, on_card_first_found=None, on_card_found=None, on_card_removed=None):
    def default_on_first_found(device_id):
        print("Card found: %s" % device_id)

    def default_on_found(device_id):
        print("Found %s" % device_id)

    def default_on_removed():
        print("Card removed.")

    if not on_card_first_found:
        on_card_first_found = default_on_first_found

    if not on_card_found:
        on_card_found = default_on_found

    if not on_card_removed:
        on_card_removed = default_on_removed

    is_device_found = False
    print("Waiting for device...")
    while not is_device_found:
        device_was_found, device = nfc_provider.scan_for_device()
        if device_was_found:
            card_id = device.pretty_card_id
            on_card_first_found(card_id)
            while device_was_found:
                device_was_found, device = nfc_provider.scan_for_device()
                is_device_found = True
                on_card_found(card_id)
            else:
                on_card_removed()


def require_card_for_time(millis):
    starting_time = None
    time_elapsed = 0
    is_time_finished = False

    def on_card_found(device_found):
        nonlocal starting_time, time_elapsed, is_time_finished
        if not starting_time:
            starting_time = current_milli_time()

        time_elapsed = current_milli_time() - starting_time
        if not is_time_finished and millis <= time_elapsed:
            print("%s milliseconds have passed. You may remove the card." % millis)
            is_time_finished = True

    def on_card_removed():
        if not millis <= time_elapsed:
            print("Card removed before %s milliseconds passed." % millis)

    wait_for_card_remove(on_card_found=on_card_found, on_card_removed=on_card_removed)


if __name__ == '__main__':
    try:
        nfc_provider = MockNFCProvider()
        while True:
            device_found = nfc_provider.scan_for_device()[1]
            if device_found is not None:
                print(device_found.pretty_card_id)
            else:
                print("None")

    except KeyboardInterrupt:
        nfc_provider.close()






