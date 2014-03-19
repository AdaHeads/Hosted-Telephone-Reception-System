# -*- coding: utf-8 -*-
# ${WIKI_URL}

from forward_call import Test_Case
from config       import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: liste-med-sekundaere-numre]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [pil op/ned - nogle gange]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: ring-markeret-nummer-op]")
            self.Receptionist_Places_Call (Number = self.Callee.sip_uri ())
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [ring-op: nummer, telefon-N]")
            self.Callee_Receives_Call ()
            self.Step (Message = "FreeSWITCH         ->  FreeSWITCH        [forbind opkald med telefon-N]")
