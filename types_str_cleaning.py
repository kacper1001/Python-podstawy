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

w = a+b+c+d+e+f+g+h+i+j+k
w=w.upper()
w=w.replace('\n\n', '').replace('\t', '') \
    .replace('ULICA.', '').replace('ULICA', '').replace('UL.', '').replace('UL', '') \
    .replace('1/2', '').replace('1 /2', '').replace('1/2.', '').replace('1APT2', '').replace('1 APT 2', '').replace('APT', '').replace('1 M. 2', '') \
    .replace('3', 'III').replace('TRZECIEGO', 'III') \
    .replace('J', '_J').replace('GO ', 'GO').split('_')
print(w)