# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Caller_Places_Call (Number = Reception)
            self.Caller_Hears_Dialtone ()
            self.Step (Message = "FreeSWITCH         ->  FreeSWITCH        [Checks dial-plan.  Result: Queue call.]")
            self.Step (Message = "FreeSWITCH         ->> Call-Flow-Control [event: call-offer; destination: Reception]")
            self.Step (Message = "FreeSWITCH: pauses dial-plan processing for # seconds")
            Call_ID, Reception_ID = self.Call_Announced ()
            self.Step (Message = "Call-Flow-Control  ->  Call-Flow-Control [wait 0.200 s]", Delay_In_Seconds = 0.200)
            self.Step (Message = "Call-Flow-Control  ->  Call-Flow-Control [no responses\nto call-offer]")
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [force-end-pause: <call_ID>]")
            self.Step (Message = "FreeSWITCH         ->> Call-Flow-Control [queued-unavailable: <call_ID>]")
            self.Step (Message = "FreeSWITCH         ->> Opkalder          [dagssvar]")
            self.Receptionist.Wait_For_Call_Locked (Call_ID = Call_ID)
            self.Step (Message = "Klient-N           ->> Receptionist-N    [Queue: <reception name> (optaget)]")
