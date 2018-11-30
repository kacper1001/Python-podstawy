class Contact:
    def __init__(self, name, addresses):
        self.name = name
        self.adresses = addresses

    def __str__(self):
        return f'{self.__dict__}'

    def __iadd__(self, other):
        self.adresses.append(other)
        return self

    def __contains__(self, item):
        for address in self.adresses:
            if address == item:
                return True
        return False


class Address:
    def __init__(self, location):
        self.location = location

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        if self.location == other.location:
            return True
        else:
            return False


contact = Contact(name='José Jiménez', addresses=[Address(location='JPL')])
contact += Address(location='Houston')
contact += Address(location='KSC')

print(contact)
# {'name': 'José Jiménez', 'addresses': [
#       {'location': 'JPL'},
#       {'location': 'Houston'},
#       {'location': 'KSC'}
# ]}

if Address(location='Houston') in contact:
    print(True)
else:
    print(False)
# True
