            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-opgiv-opkald]")
            self.Receptionist_Hangs_Up ()
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [afslut telefon-N's udgaaende opkald]")
            self.Step (Message = "FreeSWITCH         ->> Medarbejder       [SIP: hang-up]")
