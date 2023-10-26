
AANTAL_PERSONEN = 1
KOSTEN_PER_TICKET = 7.45
TIJD_VR_GAMESEAT_MINUTEN = 5

KOSTEN_PER_5_MINUTEN_VR_GAMESEAT = 0.37


totaal_kosten_tickets = AANTAL_PERSONEN * KOSTEN_PER_TICKET


totaal_kosten_vr_gameseat = (TIJD_VR_GAMESEAT_MINUTEN / 5) * AANTAL_PERSONEN * KOSTEN_PER_5_MINUTEN_VR_GAMESEAT


totaal_kosten = totaal_kosten_tickets + totaal_kosten_vr_gameseat


print(f"Dit geweldige dagje-uit met {AANTAL_PERSONEN} mensen in de Speelhal met {TIJD_VR_GAMESEAT_MINUTEN} minuten VR kost je maar {totaal_kosten} euro")
