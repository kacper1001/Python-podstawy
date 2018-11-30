

passwd_FILENAME = r'C:\Users\Administrator\Desktop\passwd.txt'

try:
    with open(passwd_FILENAME, mode='r', encoding='utf-8') as passwd_file:
        passwd = passwd_file.readlines()

except FileNotFoundError:
    print('File passwd does not exist')

except PermissionError:
    print('Permission denied - passwd')

shadow_FILENAME = r'C:\Users\Administrator\Desktop\shadow.txt'

try:
    with open(shadow_FILENAME, mode='r', encoding='utf-8') as shadow_file:
        shadow = shadow_file.readlines()

except FileNotFoundError:
    print('File shadow does not exist')

except PermissionError:
    print('Permission denied - shadow')

group_FILENAME = r'C:\Users\Administrator\Desktop\group.txt'

try:
    with open(group_FILENAME, mode='r', encoding='utf-8') as group_file:
        group = group_file.readlines()

except FileNotFoundError:
    print('File group does not exist')

except PermissionError:
    print('Permission denied - group')

users = []

for line in passwd:
    if line.startswith('#') or line.isspace():
        continue

    User_name, UID, GID, home, shell = line.split(':')[0], line.split(':')[2], line.split(':')[3], line.split(':')[5], \
                                       line.split(':')[6]

    for line in shadow:
        if line.startswith('#') or line.isspace():
            continue

        try:
            if line.split('$')[1] == '6':
                algorithm = 'MD5'
            else:
                algorithm = 'SHA-512'

            password = line.split('$')[3]

            locked = False
            if line.split(':')[1] == '!':
                locked = True

        except IndexError:
            username = line.split(':')[0]

        for line in group:
            przynalezaca_grupa = {}
            if line.startswith('#') or line.isspace():
                continue

            user_name_group = line.split(':')[3]
            if user_name_group.find(User_name) == True:
                przynalezaca_grupa.extend(line.split(':')[0])

        users.append({
            'login': User_name,
            'uid': UID,
            'gid': GID,
            'home': home,
            'shell': shell,
            'algorithm': algorithm,
            'password': password,
            'groups': przynalezaca_grupa,
            'locked': locked,
        })

from pprint import pprint
pprint(users)
