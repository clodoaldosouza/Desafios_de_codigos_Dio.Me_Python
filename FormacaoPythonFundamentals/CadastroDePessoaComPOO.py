# Treinando Orientação a Objetos com Python
# 2 / 3 - Cadastro de Pessoa com POO

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obter_informacoes_formatadas(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


# TODO: Crie um método para retornar as informações formatas com Nome e Idade:

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:
pessoa = Pessoa(nome, idade)
# TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
print(pessoa.obter_informacoes_formatadas())
