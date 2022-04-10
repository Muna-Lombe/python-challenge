import string
LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)


def generate_iban_check_digits(iban):
    print
    rearranged_iban = iban[:2] + '00' + iban[4:]
    number_iban = _number_iban(rearranged_iban)
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban(iban)) % 97 == 1


if __name__ == '__main__':
    my_ibans = [
                'AT61 1904 3002 3457 3201',
                'FR14-2004-1010-0505-0001-3',
                'RO13RZBR0000060007134800'
                ]
    for iban in my_ibans:
        if generate_iban_check_digits(iban) == iban[2:4] and valid_iban(iban):
            print('IBAN ok!\n')
        else:
            print('IBAN not ok!\n')