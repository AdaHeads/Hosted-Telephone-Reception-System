# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception
from time           import sleep

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step ("Receptionist-N     ->> Klient-N          [genvejstast-ring-til-primaert-nummer]")
            self.Receptionist_Places_Call (Number = self.Callee.Number)
            self.Step ("Call-Flow-Control  ->> FreeSWITCH        [ring-op: telefon-N, nummer]")
            self.Callee.Wait_For_Call ()
            self.Step ("FreeSWITCH         ->> FreeSWITCH        [forbind opkald\nog telefon-N]")
