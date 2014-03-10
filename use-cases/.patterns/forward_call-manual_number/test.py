# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception
from time           import sleep

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step ("Receptionist-N     ->> Klient-N          [genvejstast-viderestil-til-nummer]")
            self.Step ("Klient-N           ->> Receptionist-N    [indtastningsfelt: telefonnummer]")
            self.Step ("Receptionist-N     ->> Klient-N          [indtaster/indkopierer nummer]")
            self.Step ("Receptionist-N     ->> Klient-N          [genvejstast-ring-op]")
