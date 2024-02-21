# Inversão de caracteres de uma string:

def inverter_string(string):
    inverted_string = ''
    for i in range(len(string)-1, -1, -1):
        inverted_string += string[i]
    return inverted_string

string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
