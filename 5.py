def inverter_string(string):
    inverted_string = ''
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

# String a ser invertida
string_original = "exemplo"

# Inverter a string e imprimir o resultado
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
