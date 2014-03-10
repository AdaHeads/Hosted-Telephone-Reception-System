            Reception_Data = self.Request_Information (Reception_ID = Reception_ID)
            self.Log (Message = "- Call stealer interferes")
            self.Offer_To_Pick_Up_Call (Call_Flow_Control = self.Receptionist_2.call_control,
                                        Call_ID           = Call_ID)
            self.Log (Message = "We wait 210 ms to assure that client-N will miss the 200 ms time-window for responding.", Delay_In_Seconds = 0.210)
            self.Offer_To_Pick_Up_Call (Call_Flow_Control = self.Receptionist.call_control,
                                        Call_ID           = Call_ID)
            Call_Information = self.Call_Allocation_Acknowledgement (Call_ID         = Call_ID,
                                                                     Receptionist_ID = self.Receptionist_2.ID)
            self.Step (Message = "Client-N->Receptionist-N: Un-queue: <reception name>.")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

