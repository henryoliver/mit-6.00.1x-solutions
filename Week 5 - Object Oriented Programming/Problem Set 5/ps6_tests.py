import string

def build_shift_dict(shift):
    mapping = {}
    alphabet = string.ascii_lowercase + string.ascii_lowercase[: shift]

    for i in range(len(alphabet)):
        try:
            mapping.update({ alphabet[i]: alphabet[i + shift] })
        except IndexError:
            break
    
    mapping.update(dict((k.upper(), v.upper()) for k, v in mapping.items()))

    return mapping

def apply_shift(shift):
    cipherText = ''
    text = 'Hello World'
    shiftDict = build_shift_dict(shift)

    for char in text:
        if (char in shiftDict):
            cipherText += shiftDict[char]
        else:
            cipherText += char

    return cipherText

apply_shift(0)
