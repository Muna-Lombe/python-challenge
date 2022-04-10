from re import RegexFlag, findall, fullmatch, match, search, split, sub
from countryCode import isValidCode, getCheckSum

class Validator:
    def __init__(self):
        self.IBAN_MAX_LENGTH = 37
        self.DIGIT_VALUES = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15', 'G':'16','H':'17','I':'18',
                            'J':'19','K':'20','L':'21','M':'22','N':'23', 'O':'24','P':'25','Q':'26','R':'27','S':'28',
                            'T':'29','U':'30','V':'31','W':'32','X':'33','Y':'34','Z':'35'}
        self.MATCH_IBAN_FORMAT_PATTERN = "[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]" #to match for special characters...works!!!
        self.SUB_DASHES_PATTERN = "[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/\s]" #to match for special characters including spaces...works!!!

        self.SEPERATE_IBAN_PATTERN = "^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})$"
        self.LI_REGEX = "^([LI]{2}[ \-]?[0-9]{2})((?:[ \-]?[A-Z0-9]){5})((?:[ \-]?[A-Z0-9]{12}))$"
        pass

# get IBAN from input text
    def cleanedIbanText(self,text):
        pos = findall(self.MATCH_IBAN_FORMAT_PATTERN,text)
        txt =  text[text.index(pos[0])+1:] if len(pos) > 0 and len(text)> 30 else text
        strippedTxt = sub(self.SUB_DASHES_PATTERN,"",txt.strip())
        return strippedTxt

# check is IBAN check digit is of valid IBAN format
    def hasValidCheckDigit(self,iban):
        if(len(iban) <= self.IBAN_MAX_LENGTH and isValidCode(country_code)): 
            filtered_iban = findall(self.SEPERATE_IBAN_PATTERN,iban)[0]
            country_code_with_check_digit = filtered_iban[0]
            current_check_digit = country_code_with_check_digit[2:]
            country_code = country_code_with_check_digit[:2]
            BBAN = filtered_iban[1] 
            
            # set check digit to 00
            zeroed_check_digit = '00'

            # convert new country code to digits
            country_code_digit = self.DIGIT_VALUES[country_code[0]] + '' + self.DIGIT_VALUES[country_code[1]]
            
            # append zeroed check digit to country code digit
            new_country_code = country_code_digit + zeroed_check_digit
            tempBBAN = ""

            # convert all letters in BBAN to their digit values
            for i in BBAN:
                tempBBAN += self.DIGIT_VALUES[i] if i.isalpha() else i
                
            new_filtered_iban = int(tempBBAN + new_country_code)
            
            # calculate mod 97
            # passing it as int will auto strip leading 0s
            mod97 = new_filtered_iban % 97
            
            # subtract from 98 to get checkdigit
            calculated_check_digit = 98 - mod97
        
            # pass check_digit as integer
            current_check_digit = int(current_check_digit)
            
            # check is checksum epual to check digit
            print('IBAN valid format:',calculated_check_digit == current_check_digit)
            return calculated_check_digit == current_check_digit
        else:
            return False
                
# check if valid IBAN is Liechtenstein standard
    def matchesCountryStandard(self,iban):
        validIban = self.hasValidCheckDigit(iban)
        print('-- Liechtenstein standard check:', True if(match(self.LI_REGEX,iban)) else False)
        return True  if(validIban and match(self.LI_REGEX,iban)) else False

# check if IBAN is valid Liechtenstein IBAN
    def isValidIban(self,text, country):
        iban = self.cleanedIbanText(text)
        print(f'-- checking--', iban)
        return f"IBAN is {'valid' if self.matchesCountryStandard(iban) else 'not valid'} for {country}"
    





