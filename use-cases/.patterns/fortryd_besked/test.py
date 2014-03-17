            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: fortryd-besked]")
            self.Step (Message = "Receptionist-N    <<-  Klient-N          [ryddet 'send besked'-dialog]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

