"""
    This example demonstrates the conversion of
    arabic numbers to roman numbers

    Prerequisites:
        - variable
        - type conversion
        - loops
        - conditional tests
        - print and input
    Not mandatory but to use in advanced coding:
        - list
        - tuple
        - string methods (f strings, isdigit)
        - list/string slicing
"""

# coding: UTF-8

# create a list of tuples containing
# roman symbols and their matching value in arabic number
# including exceptions (ie IV, XC, ...)
Symbols = [
    ("M", 1000), 
    ("CM", 900), 
    ("D", 500), 
    ("CD", 400), 
    ("C", 100), 
    ("XC", 90), 
    ("L", 50), 
    ("XL", 40), 
    ("X", 10), 
    ("IX", 9), 
    ("V", 5), 
    ("IV", 4), 
    ("I", 1)]
# Extract only roman symbols
RomanSymbols = [
    Symbol[0] 
    for Symbol 
    in Symbols 
    if len(Symbol[0]) == 1]


def Main():
    """
        Main function
    """
    
    # start application
    print("\nConvertisseur de chiffres romains <-> arabes")
    print("------------------------------------------------")

    # initialize number to convert and main loop condition
    Continue = True
    NumberToConvert = ""

    while Continue:
        Conversion = None
        
        # ask for a number
        NumberToConvert = input("\nEntre un nombre arabe ou romain supérieur à 0 (vide pour quitter) : ").strip().upper()
        
        if NumberToConvert == "":
            # exit
            Continue = False
            
        elif NumberToConvert.isdigit() and int(NumberToConvert) > 0:
            # arabian to roman
            Conversion = "A-R"
            
        else:
            # check if roman number
            Conversion = "R-A"
            for Letter in NumberToConvert:
                if Letter not in RomanSymbols:
                    Conversion = None
                
            if Conversion is None:
                # bad entry
                print(f"\nDésolé mais {NumberToConvert} n'est ni un nombre arabe positif ni un nombre romain...")

        if Conversion == "A-R":
            # convert from arabian to roman
            ArabianToRoman(NumberToConvert)
        
        elif Conversion == "R-A":
            # convert from roman to arabian
            RomanToArabian(NumberToConvert)

    # exit application
    print("\nAu revoir.\n")  
          

def ArabianToRoman(Number):
    """
        Convert Number from arabian to roman
    """     
        
    # get remaining number to convert
    # and reset conversion result
    RemainingNumber = int(Number)
    ConversionResult = ""
    
    # for each roman symbol in list
    for Symbol in Symbols:

        # get tuple data (roman letter and value in arabic number)
        RomanSymbol = Symbol[0]
        SymbolValue = Symbol[1]

        # check how many times remaining arabic number
        # can be divided by current symbol value
        NumberOfMatches = RemainingNumber // SymbolValue

        # add to roman number as many symbols as number of matches
        for i in range(0, NumberOfMatches):
            ConversionResult += RomanSymbol

        # update remaining arabic number to be converted
        RemainingNumber -= NumberOfMatches * SymbolValue

        if RemainingNumber == 0:
            # if number has been converted, exit from loop
            # (no use to check remaining symbols)
            break
    
    # print final result
    print(f"\n{Number} en chiffres arabes = {ConversionResult} en chiffres romains")
        

def RomanToArabian(Number):
    """
        Convert Number from roman to arabian
    """     
            
    # get remaining number to convert
    # and reset conversion result
    RemainingNumber = Number
    ConversionResult = 0
    
    for Symbol in Symbols:

        # get tuple data (roman letter and value in arabic number)
        RomanSymbol = Symbol[0]
        SymbolValue = Symbol[1]
        
        # while number to convert starts with current roman symbol
        while RemainingNumber.startswith(RomanSymbol):
            # add symbol value to conversion result
            ConversionResult += SymbolValue
            # remove roman symbol from number to convert
            RemainingNumber = RemainingNumber[len(RomanSymbol):]

        if RemainingNumber == "":
            # if number has been converted, exit from loop
            # (no use to check remaining symbols)
            break
    
    # print final result
    print(f"\n{Number} en chiffres romains = {ConversionResult} en chiffres arabes")


# Code start
if __name__ == "__main__":
    Main()
