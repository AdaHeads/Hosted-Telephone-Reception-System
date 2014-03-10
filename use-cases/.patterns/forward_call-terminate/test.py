            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-afslut-udgaaende-samtale]")
            self.Receptionist_Hangs_Up ()
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [afslut telefon-N's udgaaende samtale]")
            self.Callee_Receives_Hangup ()
