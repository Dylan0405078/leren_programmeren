
aantal_personen = 4
kosten_per_ticket = 7.45
tijd_vr_gameseat_minuten = 45

kosten_per_5_minuten_vr_gameseat = 0.37

# kosten voor de toegangstickets
totaal_kosten_tickets = aantal_personen * kosten_per_ticket

# kosten voor de VIP-VR-GameSeat
totaal_kosten_vr_gameseat = (tijd_vr_gameseat_minuten / 5) * aantal_personen * kosten_per_5_minuten_vr_gameseat

# totaal kosten
totaal_kosten = totaal_kosten_tickets + totaal_kosten_vr_gameseat


print(f"Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {tijd_vr_gameseat_minuten} minuten VR kost je maar {totaal_kosten} euro")
