1. FreeSWITCH modtager et SIP-opkald fra [opkalder](Terminologi#opkalder) til en [reception](Terminologi#reception).
1. FreeSWITCH afspiller (ganske kort) ringetone for opkalder.
1. FreeSWITCH finder den relevante interne kaldplan og konstaterer at opkaldet skal sendes i kø (i en bestemt gruppe).
1. FreeSWITCH annoncerer til Call-Flow-Control at opkaldet sendes i kø med ringetone i den gruppe.
1. FreeSWITCH sætter behandlingen opkaldet på pause så længe som køens ringetone må vare.

???

1. Call-Flow-Control giver FreeSWITCH besked om at afslutte pausen og sende opkaldet videre til dagssvar.
1. FreeSWITCH annoncerer til Call-Flow-Control at opkaldet får afspillet dagssvar.
1. FreeSWITCH afspiller dagssvar for opkalder.
1. Call-Flow-Control annoncerer opkaldets tilstand videre til alle de [klienter](Terminologi#klient), der behandler opkald til den gruppe.
1. Klient-N viser opkaldet (med optaget-indikering) i listen med ventende opkald (til Receptionist-N).
