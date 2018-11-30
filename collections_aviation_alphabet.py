
a={
'A': 'Alfa',
'B': 'Bravo',
'C': 'Charlie',
'D': 'Delta',
'E': 'Echo',
'F': 'Foxtrot',
'G': 'Golf',
'H': 'Hotel',
'I': 'India',
'J': 'Juliet',
'K': 'Kilo',
'L': 'Lima',
'M': 'Mike',
'N': 'Novembe',
'O': 'Oscar',
'P': 'Papa',
'Q': 'Quebec',
'R': 'Romeo',
'S': 'Sierra',
'T': 'Tango',
'U': 'Uniform',
'V': 'Victor',
'W': 'Whisky',
'X': 'X-Ray',
'Z': 'Zulu',
}

b = input('wpisz coś:   ')

wsk = b[0].upper()

print(a.get(wsk), "Pilots don’t say that")
