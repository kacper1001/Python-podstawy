a = '  Jana III Sobieskiego 1 apt 2'
b = 'ul Jana III SobIESkiego 1/2'
c = '\tul. Jana trzeciego Sobieskiego 1/2'
d = 'ul.Jana III Sob\n\nieskiego 1/2'
e = 'ulicaJana III Sobieskiego 1/2'
f = 'UL. JA\tNA 3 SOBIES\tKIEGO 1/2'
g = 'UL. III SOBiesKIEGO 1/2'
h = 'ULICA JANA III SOBIESKIEGO 1 /2  '
i = 'ULICA. JANA III SOBI'
j = ' Jana 3 Sobieskiego 1/2 '
k = 'Jana III Sobieskiego 1 m. 2'


def clean(text):
    text = text.upper()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('ULICA.', '')
    text = text.replace('ULICA', '')
    text = text.replace('UL.', '')
    text = text.replace('1 /2', '')
    text = text.replace('1/2', '')
    text = text.replace('1 M. 2', '')
    text = text.replace('1 APT 2', '')
    return text


a = clean(a)
b = clean(b)
c = clean(c)
d = clean(d)
e = clean(e)
f = clean(f)
g = clean(g)
h = clean(h)

print (a)
