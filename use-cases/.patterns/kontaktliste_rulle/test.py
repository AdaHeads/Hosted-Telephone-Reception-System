            self.Step (Message = "=== loop ===")
            self.Step (Message = "Receptionist-N     ->> Klient-N          [arrow up/down]")
            self.Step (Message = "Receptionist-N    <<-  Klient-N          [update contact view]")
            self.Step (Message = "=== end loop ===")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

