            self.Step (Message = "Klient-N           ->> Klient-N          [ryd alle 'send besked'-felter]")
            self.Step (Message = "Receptionist-N    <<-  Klient-N          [ryddet 'send besked'-dialog]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

