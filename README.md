# Task: Writing a validator for IBANs
- Details: write us an IBAN validator, that works for IBANs from Liechtenstein

- Requirement: Create a function that takes an IBAN (as string) and returns true if the IBAN is a valid one from Liechtenstein.
 Make sure to use a code style and approach that you would use when coding for a company, as this is not mainly about solving the issue but also to see what kind of code your write.

# IBAN Breakdown format and structure
Each IBAN includes the same basic set of information:

- A 2 letter country code (for example, ES for Spain, or GB for the United Kingdom).
- 2 digits which are used to validate the IBAN before a payment is processed.
- The BBAN (Basic Bank Account Number) for the specific account. This follows the protocols of the country the account is held in, and can be up to 30 characters long.

# Example IBANS 
- DE89 3704 0044 0532 0130 00
- AT61 1904 3002 3457 3201
- FR14 2004 1010 0505 0001 3

# Standard IBAN Format in Germany
Below is the typical IBAN for Germany. It contains 22 characters. Below you will find a detailed breakdown of the IBAN structure in Germany.

- 2 letters ISO country code
- 2 digits IBAN check digits
- 8 digits blz
- 10 digits account number

# Example IBANS in Germany
- DE89 3704 0044 0532 0130 00

# Standard IBAN Format in Liechtenstein
Below is the typical IBAN for Liechtenstein. It contains 21 characters. Below you will find a detailed breakdown of the IBAN structure in Liechtenstein.

- 2 letters ISO country code
- 2 digits IBAN check digits
- 5 digits bank code
- 12 characters account number

# Example IBANS in Liechtenstein
- LI 21 08810 0002324013AA
- Standard format
	LI21088100002324013AA
- Print format
    LI21 0881 0000 2324 013A A

# IBAN validation should return the following:
IBAN Validation Result
✔ IBAN: LI21088100002324013AA is VALID.
 - should have country code and checksum digit and <= Iban max length 34
✔ IBAN checksum is VALID.
 - checksum should be int and valid digit for country
✔ IBAN respects Length standard for Liechtenstein (LI).
 - length should equal country standard
✔ IBAN respects Format and Structure standard for Liechtenstein (LI).
 - should follow Liechtenstein format of:
    - 2 letters ISO country code
    - 2 digits IBAN check digits
    - 5 digits bank code
    - 12 characters account number

- Note: 
    - currently added length and country code validators ✔
