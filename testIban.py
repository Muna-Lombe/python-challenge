from IbanValidator import Validator
from re import RegexFlag, findall, fullmatch, match, search, split, sub
ibans = [
        'this is an Iban: DE89 3704 0044 0532 0130 00',
        'this is an Iban - DE89 3704 0044 0532 0130 00',
        'Iban = DE89 3704 0044 0532 0130 00',
        'Iban => DE89 3704 0044 0532 0130 00',
        'AT61 1904 3002 3457 3201',
        'FR14-2004-1010-0505-0001-3',
        'RO13RZBR0000060007134800',
        'LI21088100002324013AA',
        'LI7408806123456789012',
        'LI2325614568954121785',
        '123456789011212343345'
        ]


# rp4 = "^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})([ \-]?[A-Z0-9]{1,3})?$" #buggy, not clear, but works with cleaned text
rp4 = "^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})$" #buggy, not clear, but works with cleaned text
rp5 = "[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]" #to match for special characters...works!!!
rp9 = "[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/\s]" #to match for special characters including spaces...works!!!


if __name__ == "__main__":
    val = Validator()

    for iban in ibans:
        print('////////////////////////////////////')
        print(val.isValidIban(iban,'Liechtenstein'))
        print('////////////////////////////////////')