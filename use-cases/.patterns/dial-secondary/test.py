# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-liste-med-sekundaere-numre]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [pil op/ned", note = "nogle\ngange]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-ring-markeret-nummer-op]")
            self.Receptionist_Places_Call (Number = self.Callee)
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [ring-op: nummer, telefon-N]")
            self.Callee.Accept_Call
            self.Step (Message = "FreeSWITCH         ->  FreeSWITCH        [forbind opkald\nmed telefon-N]")
