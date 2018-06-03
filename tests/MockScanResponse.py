from nfcproviders import NFCProviderUtil as Util

_default_atqa = "00  00"
_default_sak = "00"
_default_ats = "00  00  00  00"

_atqa_placeholder = "{ATQA}"
_uid_placeholder = "{UID}"
_sak_placeholder = "{SAK}"
_ats_placeholder = "{ATS}"


_replaceable_scan_response = """ISO/IEC 14443A (000 kbps) target:
                             ATQA (SENS_RES): %s
                                UID (NFCID1): %s
                               SAK (SEL_RES): %s
                                         ATS: %s 
                          """ % (_atqa_placeholder, _uid_placeholder, _sak_placeholder, _ats_placeholder)


class MockScanResponse:

    def __init__(self, uid="", atqa=_default_atqa, sak=_default_sak, ats=_default_ats) -> None:
        self.atqa = atqa
        self.uid = uid
        self.sak = sak
        self.ats = ats

    def update_response(self, uid="", atqa="", sak="", ats=""):
        self._update_uid(uid)
        self._update_atqa(atqa)
        self._update_sak(sak)
        self._update_ats(ats)

    def clear(self):
        self.update_response()

    def _update_uid(self, uid):
        self.uid = Util.make_card_id_safe(uid) if Util.is_card_id_valid(uid) else ""

    def _update_atqa(self, atqa):
        self.atqa = Util.make_general_id_safe(atqa) if Util.is_general_id_valid(atqa) else ""

    def _update_sak(self, sak):
        self.sak = Util.make_general_id_safe(sak) if Util.is_general_id_valid(sak) else ""

    def _update_ats(self, ats):
        self.ats = Util.make_general_id_safe(ats) if Util.is_general_id_valid(ats) else ""
        
    def _generate_scan_response(self):
        response = _replaceable_scan_response.replace(_atqa_placeholder, Util.insert_spaces_every_n_chars(self.atqa))
        response = response.replace(_uid_placeholder, Util.insert_spaces_every_n_chars(self.uid))
        response = response.replace(_sak_placeholder, Util.insert_spaces_every_n_chars(self.sak))
        return response.replace(_ats_placeholder, Util.insert_spaces_every_n_chars(self.ats))

    def __str__(self) -> str:
        return self._generate_scan_response()

