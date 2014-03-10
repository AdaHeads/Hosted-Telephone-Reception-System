            self.Step (Message = "FreeSWITCH         ->  FreeSWITCH        [label = "forbind opkalder og telefon-N]")
            self.Step (Message = "=== loop ===")
            self.Step (Message = "Receptionist-N     ->> Telefon-N         [label = "snak]")
            self.Step (Message = "Telefon-N          ->> FreeSWITCH        [label = "SIP: lyd]")
            self.Step (Message = "FreeSWITCH         ->> Opkalder          [label = "SIP: lyd]")
            self.Step (Message = "Opkalder           ->> FreeSWITCH        [label = "SIP: lyd]")
            self.Step (Message = "FreeSWITCH         ->> Telefon-N         [label = "SIP: lyd]")
            self.Step (Message = "Telefon-N          ->> Receptionist-N    [label = "snak]")
            self.Step (Message = "=== end loop ===")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

