aantal_personen = int(input("Met hoeveel mensen ben je?"))
KOSTEN_PER_TICKET = 7.45
tijd_vr_gameseat_minuten = int(input("hoeveel minuten vr gaming ga je doen?"))

KOSTEN_PER_5_MINUTEN_VR_GAMESEAT = 0.37


totaal_kosten_tickets = aantal_personen * KOSTEN_PER_TICKET


totaal_kosten_vr_gameseat = (tijd_vr_gameseat_minuten / 5) * aantal_personen * KOSTEN_PER_5_MINUTEN_VR_GAMESEAT


totaal_kosten = totaal_kosten_tickets + totaal_kosten_vr_gameseat


print(f"Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {tijd_vr_gameseat_minuten} minuten VR kost je maar {totaal_kosten} euro")
