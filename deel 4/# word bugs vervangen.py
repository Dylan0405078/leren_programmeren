# word bugs vervangen
woord1 = input('Geef een woord: ')
woord2 = input('Geef nog een woord: ')

if len(woord1) > len(woord2):
    print('Woord 1 heeft meer letters dan woord 2')
elif len(woord1) < len(woord2):
    print('Woord 1 heeft minder letters dan woord 2')
else:
    print('Woord 1 en woord 2 hebben evenveel letters')
