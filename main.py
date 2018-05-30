import websockets
import nfc
import time


def current_milli_time():
    return int(round(time.time() * 1000))


def parse_device_to_id(device):
    _, string = nfc.str_nfc_target(device, False)
    str_list = string.split("\n")
    uid = str_list[2].strip().replace("  ", " ")
    return uid[uid.index(": ") + 2:]


def wait_for_card_remove(on_card_first_found=None, on_card_found=None, on_card_removed=None):
    def default_on_first_found(id):
        print("Card found: %s" % id)

    def default_on_found(id):
        print("Found %s" % card_id)

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
        number_found, devices = read_nfc()
        if number_found > 0:
            card_id = parse_device_to_id(devices[0])
            on_card_first_found(card_id)
            while number_found > 0:
                number_found, devices = read_nfc()
                is_device_found = True
                on_card_found(card_id)
            else:
                on_card_removed()


def read_nfc():
    return nfc.initiator_list_passive_targets(listener, modulation, 1)


def require_card_for_time(millis):
    starting_time = None
    time_elapsed = 0
    is_time_finished = False

    def on_card_found(id):
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
        context = nfc.init()
        reader = nfc.list_devices(context, 2)[0]

        listener = nfc.open(context, reader)
        modulation = nfc.modulation()
        modulation.nmt = nfc.NMT_ISO14443A
        modulation.nbr = nfc.NBR_106

        number_found, devices = nfc.initiator_list_passive_targets(listener, modulation, 1)
        wait_for_card_remove()
        # require_card_for_time(5000)

    except KeyboardInterrupt:
        nfc.close(listener)
        nfc.exit(context)






