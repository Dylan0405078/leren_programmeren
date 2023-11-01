#ego centrische brief


import re

# deelzinnen uit een tekst 
def get_sub_sentences(text):
    # Vervang alle separators door een marker "|"
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")  # Split de tekst op marker "|"
    
    # Verwijder leidende en volgende spaties en converteer naar lowercase
    sub_sentences = [sentence.strip().lower() for sentence in sub_sentences if len(sentence) > 0]
    
    return sub_sentences

# Tweede functie om de ego-score te berekenen
def calculate_ego_score(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        words = sentence.split(' ')  # Split de zin in woorden
        # Controleer of de eerste twee woorden van de zin gelijk zijn aan "ik" of "mijn"
        if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
            ego_score += 1
    return ego_score

# gebruik:
text = "Geachte heer/mevrouw,Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team. Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie"
sub_sentences = get_sub_sentences(text)
ego_score = calculate_ego_score(sub_sentences)
print(f"de ego scoren van de persoon is {ego_score}")