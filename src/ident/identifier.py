def validate(string):
    if string.isalnum() and string[0].isalpha() and len(string) >= 1 and len(string) <= 6:
        return 'Valido'
    else:
        return 'Invalido'