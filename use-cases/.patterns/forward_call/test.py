            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: stil-igennem]")
            self.Receptionist_Forwards_Call (Incoming_Call = Call_ID,
                                             Outgoing_Call = Outgoing_Call_ID)
            self.Step (Message = "Klient-N           ->> Klient-N          [ny tilstand: ledig]")
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [connect: incoming, outgoing]")
            self.Receptionist_Waits_For_Hang_Up ()
            self.Step (Message = "FreeSWITCH         ->> Call-Flow-Control [free: telefon-N]")
            self.Step (Message = "FreeSWITCH         ->> FreeSWITCH        [connect: incoming, outgoing]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

