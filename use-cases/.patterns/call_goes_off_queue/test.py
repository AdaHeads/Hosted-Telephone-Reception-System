            Reception_Data = self.Request_Information (Reception_ID = Reception_ID)
            logging.info ("- Call stealer interferes")
            self.Call_Strealer.Offer_To_Pick_Up_Call (Call_ID = Call_ID)
            self.Log ("We wait 210 ms to assure that client-N will miss the 200 ms time-window for responding.", Delay_In_Seconds = 0.210)
            self.Receptionist.Offer_To_Pick_Up_Call (Call_ID = Call_ID)
            Call_Information = self.Call_Allocation_Acknowledgement (Call_ID         = Call_ID,
                                                                     Receptionist_ID = Call_Stealer.ID)
            self.Step (Message = "Client-N->Receptionist-N: Un-queue: JSA R&I.")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

