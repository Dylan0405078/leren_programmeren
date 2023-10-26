# Vraag de gebruiker om twee gehele getallen in te voeren
a = int(input("Voer het eerste gehele getal in: "))
b = int(input("Voer het tweede gehele getal in: "))



# Controleer of a groter is dan b
if a > b:
    Max = a
    Min = b
    print("a is het grootste getal:", Max)
# Controleer of a kleiner is dan b
elif a < b:
    Min = a
    Max = b
    print("a is het kleinste getal:", Min)
# Als geen van beide voorwaarden waar is, zijn a en b gelijk
else:
    Min = a
    Max = a
    print("a en b zijn even groot")

# Print het minimum en maximum
print("Het minimum is:", Min)
print("Het maximum is:", Max)
