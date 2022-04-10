from re import RegexFlag, findall, fullmatch, match, search, split, sub
from countryCode import isValidCode, getCheckSum

class Validator:

    
    def __init__(self):
        self.IBAN_MAX_LENGTH = 37
        self.DIGIT_VALUES = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15', 'G':'16','H':'17','I':'18',
                            'J':'19','K':'20','L':'21','M':'22','N':'23', 'O':'24','P':'25','Q':'26','R':'27','S':'28',
                            'T':'29','U':'30','V':'31','W':'32','X':'33','Y':'34','Z':'35'}
        self.REGEX_PATTERN = "^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})$"
        pass

# check if iban checksum is valid, how?
    def hasValidCheckSum(self,iban):
        filtered_iban = findall(self.REGEX_PATTERN,iban)[0]
        country_code_with_check_digit = filtered_iban[0]
        current_check_digit = country_code_with_check_digit[2:]
        country_code = country_code_with_check_digit[:2]
        bBan = filtered_iban[1]
        basic_bank_code = bBan[:5]
        account_number = bBan[5:]
        
        if(len(iban) <= self.IBAN_MAX_LENGTH and isValidCode(country_code)):    
            
            # set check digit to 00
            zeroed_check_digit = '00'

            # convert new country code to digits
            country_code_digit = self.DIGIT_VALUES[country_code[0]]+ '' + self.DIGIT_VALUES[country_code[1]]
            
            # append zeroed check digit to country code digit
            new_country_code = country_code_digit + zeroed_check_digit
            tempbBan = ""

            # convert all letters in bBan to their digit values
            for i in bBan:
                tempbBan += self.DIGIT_VALUES[i] if i.isalpha() else i
                
            new_filtered_iban = int(tempbBan + new_country_code)
            
            # calculate mod 97
            # passing it as int will auto strip leading 0s
            mod97 = new_filtered_iban % 97
            
            # subtract from 98 to get checkdigit
            calculated_check_digit = 98 - mod97
        
            # pass check_digit as integer
            current_check_digit = int(current_check_digit)
            
            # check is checksum epual to check digit
            # return {'filtered_iban': filtered_iban, 'check_digit': check_digit, 'basic_bank_code': basic_bank_code, 'account_number':account_number} if checksum == check_digit else False
            return [calculated_check_digit, basic_bank_code, account_number, country_code, calculated_check_digit == current_check_digit] if calculated_check_digit == current_check_digit else False
        else:
            return False

    def matchesCountryStandard(self,iban):
        countryIbanLength = 21
        countryStandardBankCode = 5
        countryStandardAccountNumber = 12
        validIban = self.hasValidCheckSum(iban)
        if(validIban):
            # hasValidStandard = True if(len(iban) == countryIbanLength and validIban[0] == countryIbanCheckSum and validIban[1] == countryStandardBankCode and validIban[2] == countryStandardAccountNumber and len(validIban[3]) == iban[:2] ) else False
            hasValidStandard = True if(
                len(iban) == countryIbanLength
                # and validIban[0] == countryIbanCheckSum 
                and len(validIban[1]) == countryStandardBankCode 
                and len(validIban[2]) == countryStandardAccountNumber
                and validIban[3] == iban[:2]
                and validIban[4] 
            ) else False
            print('standard check:', hasValidStandard)
            return hasValidStandard
        else:
            return False

    def isValidIban(self,iban, country):
        print(f'-- checking--', iban)
        return f"IBAN is {'valid' if self.matchesCountryStandard(iban) else 'not valid'} for {country}"
    





