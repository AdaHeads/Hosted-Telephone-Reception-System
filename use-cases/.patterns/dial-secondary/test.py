# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception
from time           import sleep

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step ("Receptionist-N     ->> Klient-N          [genvejstast-liste-med-sekundaere-numre]")
            self.Step ("Receptionist-N     ->> Klient-N          [pil op/ned", note = "nogle\ngange]")
            self.Step ("Receptionist-N     ->> Klient-N          [genvejstast-ring-markeret-nummer-op]")
            self.Receptionist_Places_Call (Number = self.Callee)
            self.Step ("Call-Flow-Control  ->> FreeSWITCH        [ring-op: nummer, telefon-N]")
            self.Callee.Accept_Call
            self.Step ("FreeSWITCH         ->  FreeSWITCH        [forbind opkald\nmed telefon-N]")
