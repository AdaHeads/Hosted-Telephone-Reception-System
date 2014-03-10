# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception
from time           import sleep

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Caller.Call (Number = Reception)
            self.Caller.Hear_Dialtone ()
            self.Step ("FreeSWITCH         ->  FreeSWITCH        [dial-plan-query:\n+45 21 49 08 04?", note = "queue\ncall]")
            self.Step ("FreeSWITCH         ->> Call-Flow-Control [queued-dialtone: +45 21 49 08 04]")
            self.Step ("FreeSWITCH         ->  FreeSWITCH        [pause-processing]")
            Call_ID, Reception_ID = self.Call_Announced ()
            self.Step ("Call-Flow-Control  ->  Call-Flow-Control [wait 0.200 s]", Delay_In_Seconds = 0.200)
            self.Step ("Call-Flow-Control  ->  Call-Flow-Control [no responses\nto call-offer]")
            self.Step ("Call-Flow-Control  ->> FreeSWITCH        [force-end-pause: +45 21 49 08 04]")
            self.Step ("FreeSWITCH         ->> Call-Flow-Control [queued-unavailable: +45 21 49 08 04]")
            self.Step ("FreeSWITCH         ->> Opkalder          [dagssvar]")
            self.Receptionist.Wait_For_Call_Locked (Call_ID = Call_ID)
            self.Step ("Klient-N           ->> Receptionist-N    [Queue: JSA R&I (optaget)]")
