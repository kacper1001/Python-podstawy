FILENAME = r'C:\Users\Administrator\Desktop\hosts.txt'

tabela = []

try:
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        zawartosc = file.readlines()


except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')

for line in zawartosc:
    if line.startswith('#') or line.isspace():
        continue

    ip = line.split()[0]
    host = line.split()[1:]

    if ip.startswith(':'):
        iptype = 'IPv6'
    else:
        iptype = 'IPv4'
    tabela.append({'hostname': host, 'ip': ip, 'protocol' : iptype})

print(tabela)
