# https://github.com/AdaHeads/Hosted-Telephone-Reception-System/wiki/Use-case%3A-Indg%C3%A5ende-opkald#wiki-variant-FIXME

from incoming_calls          import Test_Case
from sip_profiles            import agent110# as Caller
from sip_profiles            import agent110# as Receptionist
from config                  import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Caller       = Caller,
                                Receptionist = Receptionist,
                                Reception    = Reception)

