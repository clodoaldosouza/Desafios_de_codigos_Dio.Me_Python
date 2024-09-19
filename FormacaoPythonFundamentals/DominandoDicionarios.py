# Dominando Estrutura de Dados com Python
# 3 / 3 - Dominando Dicionários

def contar_caracteres(string):
    # TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    # TODO: Itere através de cada caractere na string string.
    # TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    for char in string:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador


# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
