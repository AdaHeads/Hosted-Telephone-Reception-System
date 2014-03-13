            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: opgiv-opkald]")
            self.Receptionist_Hangs_Up (Call_ID = Outgoing_Call_ID)
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [afslut telefon-N's udgaaende opkald]")
            self.Callee_Receives_Hang_Up ()
