            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: afslut-udgaaende-samtale]")
            self.Receptionist_Hangs_Up (Call_ID = Outgoing_Call_ID)
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [afslut telefon-N's udgaaende samtale]")
            self.Callee_Receives_Hangup ()
