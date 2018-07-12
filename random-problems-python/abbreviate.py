
def abbreviate(input_word):
    """
    Abbreviates a string into:
    [first letter] + [number of letters removed] + [last letter]

    Examples:
    internationalization => i18n
    localization => l10n
    hello => h3o

    :param input_word The string to abbreviate
    :return The abbreviated string
    """
    
    if (len(input_word) > 2 ):
        length = str(len(input_word) - 2)
        abstr = []
        abstr.append(input_word[0])
        abstr.append(length)
        abstr.append(input_word[len(input_word)-1])
    
        abstring = ''.join(abstr)
        
        return abstring
        
    else:
        return input_word
    
print(abbreviate('abcdefghijklmnopqrstuvwxyz'))