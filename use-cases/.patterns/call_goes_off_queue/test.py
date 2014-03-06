            Reception_Data = self.Request_Information (Reception_ID = Reception_ID)
            logging.info ("- Call stealer interferes")
            self.Offer_To_Pick_Up_Call (Call_Flow_Control = self.Call_Steal_Control,
                                        Call_ID           = Call_ID)
            sleep (0.250) # To assure that client-N will miss the 200 ms time-window for responding
            self.Offer_To_Pick_Up_Call (Call_Flow_Control = self.Call_Flow_Control,
                                        Call_ID           = Call_ID)
            Call_Information = self.Call_Allocation_Acknowledgement (Call_ID         = Call_ID,
                                                                     Receptionist_ID = Call_Stealer.ID)
            self.Step (Message = "Client-N->Receptionist-N: Un-queue: JSA R&I.")
