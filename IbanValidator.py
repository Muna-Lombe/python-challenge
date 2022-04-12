from re import findall, match, search, sub
import string

class Validator:
    def __init__(self):
        self.COUNTRY_CODES = ['AL', 'AD', 'AT', 'AZ', 'BH', 'BY', 'BE', 'BA', 'BR', 'BG', 'CR', 'HR', 'CY', 'CZ', 'DK', 'DO', 'SV', 'EE', 'FO','FI', 'FR', 'GE', 'DE', 'GI', 'GR', 'GL', 'GT', 'HU', 'IS', 'IQ', 'IE'
                                'IL', 'IT', 'JO', 'KZ', 'XK', 'KW', 'LV', 'LB', 'LI', 'LT', 'LU', 'MK', 'MT', 'MR', 'MU', 'MD', 'MC', 'ME', 'NL', 'NO', 'PK', 'PS', 'PL', 'PT', 'QA', 'RO', 'LC', 'SM', 'ST', 'SA', 'RS'
                                'SC', 'SK', 'SI', 'ES', 'SE', 'CH', 'TL', 'TN', 'TR', 'UA', 'AE', 'GB', 'VA', 'VG'
                            ]
        self.IBAN_MAX_LENGTH = 37
        self.SPECIAL_CHARACTER_PATTERN = "[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]" 
        self.SPECIAL_CHARACTER_PATTERN_SPACE = "[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/\s]" 
        self.MATCH_IBAN_PATTERN = "^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})$"
        self.LI_REGEX = "^([LI]{2}[ \-]?[0-9]{2})((?:[ \-]?[A-Z0-9]){5})((?:[ \-]?[A-Z0-9]{12}))$"
        self.LETTER_DIGIT_PAIR = {ord(t): str(i) for i, t in enumerate(string.digits + string.ascii_uppercase)} 
        pass

# extracts text with valid IBAN format from input
    def cleanedIbanText(self,text): 
        extracted_special_chars = findall(self.SPECIAL_CHARACTER_PATTERN,text) 
        unstripped_text =  text[text.index(extracted_special_chars[0])+1:] if len(extracted_special_chars) > 0 and len(text)> 30 else text
        stripped_text = sub(self.SPECIAL_CHARACTER_PATTERN_SPACE,"",unstripped_text.strip())
        if match(self.MATCH_IBAN_PATTERN,stripped_text):
            return stripped_text
        else:
            return False

# ccalculate and compare checkdigit with IBAN checkdigit
    def hasValidCheckDigit(self,iban):
        # only proceed if IBAN has valid length and valid IBAN country code
        if(len(iban) <= self.IBAN_MAX_LENGTH and iban[:2] in self.COUNTRY_CODES): 
            numberised_iban =  (iban[4:] + iban[:2] + '00').translate(self.LETTER_DIGIT_PAIR) # convert iban alphanumeric value to all digit values
            calculated_check_digit = 98 - (int(numberised_iban) % 97) # calculate the mod97 checkdigit value from the numberised_iban
            print('---- IBAN valid format and check digit:',calculated_check_digit == int(iban[2:4]))
            return calculated_check_digit == int(iban[2:4])
        else:
            return False
                
# check if valid IBAN is Liechtenstein standard
    def matchesCountryStandard(self,iban):
        validIban = self.hasValidCheckDigit(iban)
        print('---- Liechtenstein standard check:', True if(match(self.LI_REGEX,iban)) else False)
        return True  if(validIban and match(self.LI_REGEX,iban)) else False

# check if IBAN is valid Liechtenstein IBAN
    def isValidIban(self,text):
        iban = self.cleanedIbanText(text)
        if iban:
            print(f'-- Validating: ', iban)
            return f"{iban} is {'valid IBAN' if self.matchesCountryStandard(iban) else 'not valid'} for Liechtenstein"
        else:
            return "No IBAN Found"
    





