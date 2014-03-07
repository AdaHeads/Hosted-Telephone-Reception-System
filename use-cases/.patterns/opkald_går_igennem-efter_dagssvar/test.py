            Reception_Data = self.Request_Information (Reception_ID = Reception_ID)
            self.Offer_To_Pick_Up_Call (Call_Flow_Control = self.Call_Flow_Control,
                                        Call_ID           = Call_ID)
            Call_Information = self.Call_Allocation_Acknowledgement (Call_ID         = Call_ID,
                                                                     Receptionist_ID = Receptionist.ID)
            self.Step (Message = "Call-Flow-Control->FreeSWITCH: connect call to phone-N")
            self.Receptionist_Answers (Call_Information      = Call_Information,
                                       Reception_Information = Reception_Data,
                                       After_Greeting_Played = True)

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise
