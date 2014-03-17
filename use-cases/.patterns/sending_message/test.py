            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: send-besked]")
            self.Step (Message = "Klient-N           ->> Call-Flow-Control [send <besked> til <modtagerliste>]")
            self.Step (Message = "Call-Flow-Control  ->> Message-Spool     [send <besked> til <modtagerliste>]")
            self.Step (Message = "Message-Spool      ->> Medarbejder       [<besked>", note = "muligvis\ntil flere]")
            self.Step (Message = "Receptionist-N    <<-  Klient-N          [ryddet 'send besked'-dialog]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

