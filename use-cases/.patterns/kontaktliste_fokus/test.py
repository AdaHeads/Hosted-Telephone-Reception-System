# -*- coding: utf-8 -*-
# ${WIKI_URL}

from find_contact import Test_Case

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions ()

            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvej: for-kontaktliste]")
            self.Step (Message = "Receptionist-N    <<-  Klient-N          [fokus: kontaktliste og soegefelt]")
