# studie advies




#  constanten voor de teksten en stellingen
STUDIEDOKTER_TITEL = '''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
'''
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'

COMPETENTIE_ADVIES_TITEL = '''
*********************** STUDIEADVIES ***********************'''
COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''

# Vraag het aantal weken dat de gebruiker al bezig is
aantal_weken = int(input(AANTAL_WEKEN_VRAAG))

# Stel de stellingen op basis van het aantal weken
if aantal_weken >= 10:
    stellingen = [
        COMPETENTIE_STELLING_1,
        COMPETENTIE_STELLING_2,
        COMPETENTIE_STELLING_3,
        COMPETENTIE_STELLING_4,
        COMPETENTIE_STELLING_5,
        COMPETENTIE_STELLING_6,
        COMPETENTIE_STELLING_7,
    ]
else:
    stellingen = [
        COMPETENTIE_STELLING_1,
        COMPETENTIE_STELLING_2,
        COMPETENTIE_STELLING_3,
        COMPETENTIE_STELLING_4,
        COMPETENTIE_STELLING_5,
    ]

# Initialiseer variabelen voor het bijhouden van antwoorden
totaal_score = 0
aantal_altijd_vaak = 0
aantal_altijd_vaak_regelmatig = 0

# Vraag de gebruiker om antwoorden op de stellingen
for i, stelling in enumerate(stellingen, start=1):
    print(f"\nStelling {i}: {stelling}")
    print(OPTIES)
    antwoord = int(input("Jouw antwoord (0/1/2/3/4): "))
    
    totaal_score += antwoord
    
    if antwoord <= 1:
        aantal_altijd_vaak += 1
        if antwoord <= 2:
            aantal_altijd_vaak_regelmatig += 1

# Bereken de gemiddelde score
gemiddelde_score = totaal_score / len(stellingen)

# Bepaal het advies op basis van de gemiddelde score en antwoorden
if gemiddelde_score <= 2 or aantal_altijd_vaak > len(stellingen) / 2:
    advies = COMPETENTIE_ADVIES_ZORGELIJK
elif gemiddelde_score <= 3 or aantal_altijd_vaak_regelmatig > len(stellingen) / 2:
    advies = COMPETENTIE_ADVIES_TWIJFELACHTIG
else:
    advies = COMPETENTIE_ADVIES_GERUSTSTELLEND

# Toon het advies aan de gebruiker
print(COMPETENTIE_ADVIES_TITEL)
print(advies)