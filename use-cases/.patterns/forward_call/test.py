            self.Step ("Receptionist-N     ->> Klient-N          [genvejstast-stil-igennem]")
            self.Step ("Klient-N           ->> Call-Flow-Control [stil-igennem]")
            self.Step ("Klient-N           ->> Klient-N          [ny tilstand:\nledig]")
            self.Step ("Call-Flow-Control  ->> FreeSWITCH        [connect: incoming, outgoing]")
            self.Step ("FreeSWITCH         ->> Telefon-N         [SIP: hang-up]")
            self.Step ("FreeSWITCH         ->> Call-Flow-Control [free: telefon-N]")
            self.Step ("FreeSWITCH         ->> FreeSWITCH        [connect: incoming, outgoing]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

