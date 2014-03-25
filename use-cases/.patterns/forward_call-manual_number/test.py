# -*- coding: utf-8 -*-
# ${WIKI_URL}

from forward_call import Test_Case
from config       import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: viderestil-til-nummer]")
            self.Step (Message = "Klient-N           ->> Receptionist-N    [indtastningsfelt: telefonnummer]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [indtaster/indkopierer nummer]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: ring-op]")
            Outgoing_Call_ID = self.Receptionist_Places_Call (Number = self.Callee.sip_uri ())
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [samtale: telefon-N, <nummer>]")
            self.Step (Message = "FreeSWITCH         ->> Telefon-N         [SIP: opkald]")
            self.Step (Message = "FreeSWITCH         ->> Medarbejder       [SIP: opkald]")
            self.Step (Message = "FreeSWITCH         ->> FreeSWITCH        [Brokobler opkald.]")
            self.Receptionist_Receives_Call ()
