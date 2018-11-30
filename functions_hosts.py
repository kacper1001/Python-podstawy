FILENAME = r'C:\Users\Administrator\Desktop\hosts.txt'
hosts = {}

try:
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        zawartosc = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


def print_host(*args):
    print(locals())


for line in zawartosc:
    if line.startswith('#') or line.isspace():
        continue

    ip = line.split()[0]
    host = line.split()[1:]
    hosts={ip:host}

print_host()
