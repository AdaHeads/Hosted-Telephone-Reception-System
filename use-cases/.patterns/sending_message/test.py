            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: send-besked]")
            self.Receptionist_Send_Message ()
            self.Step (Message = "Call-Flow-Control  ->> Message-Spool     [send <besked> til <modtagerliste>]")
            self.Callee_Checks_For_Message ()
            self.Step (Message = "Receptionist-N    <<-  Klient-N          [ryddet 'send besked'-dialog]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

