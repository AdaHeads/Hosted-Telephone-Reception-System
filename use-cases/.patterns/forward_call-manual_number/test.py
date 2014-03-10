# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-viderestil-til-nummer]")
            self.Step (Message = "Klient-N           ->> Receptionist-N    [indtastningsfelt: telefonnummer]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [indtaster/indkopierer nummer]")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-ring-op]")
