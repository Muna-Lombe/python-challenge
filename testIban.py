from IbanValidator import Validator

ibans = [
        'this is an Iban: DE89 3704 0044 0532 0130 00', 'this is an Iban - DE89 3704 0044 0532 0130 00', 'Iban = DE89 3704 0044 0532 0130 00',
        'Iban => DE89 3704 0044 0532 0130 00', 'AT61 1904 3002 3457 3201', 'FR14-2004-1010-0505-0001-3', 'RO13RZBR0000060007134800',
        'LI21088100002324013AA', 'LI7408806123456789012', 'LI2325614568954121785', '123456789011212343345', 'there - is - no - IBAN - here',
        '1234-5678-1010-4312-2354','ASWE-QWRE-REWE-DESD-SDFE'
        ]

banner = """                   _____ ____          _   _                   
                  |_   _|  _ \   /\   | \ | |                  
                    | | | |_) | /  \  |  \| |                  
                    | | |  _ < / /\ \ | . ` |                  
                   _| |_| |_) / ____ \| |\  |                  
 __      __     _ |_____|____/_/__  \_\_|_\_|___ ____  _____   
 \ \    / /\   | |    |_   _|  __ \   /\|__   __/ __ \|  __ \  
  \ \  / /  \  | |      | | | |  | | /  \  | | | |  | | |__) | 
   \ \/ / /\ \ | |      | | | |  | |/ /\ \ | | | |  | |  _  /  
    \  / ____ \| |____ _| |_| |__| / ____ \| | | |__| | | \ \  
     \/_/    \_\______|_____|_____/_/    \_\_|  \____/|_|  \_\ 

            """

if __name__ == "__main__":
    val = Validator()
    print(banner)
    j = input("Enter IBAN or type 'TEST' to try out example validations\n")
    
    if(j.lower() == "test"):
        for iban in ibans:
            print('------------------------------------\n')
            print(val.isValidIban(iban))
            print('------------------------------------\n')
    else:
        print(val.isValidIban(str(j)))