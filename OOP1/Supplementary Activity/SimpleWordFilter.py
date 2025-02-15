badList = ['stupid', 'defacated', 'peed']

def filter(stringInput, listInput):
    for bad_word in listInput:
        stringInput = stringInput.replace(bad_word, "*" * len(bad_word))
    return stringInput

stringInput = "that stupid neighbor's dog defacated, peed, and made a mess of our yard again."
string = filter(stringInput, badList)
print(string)