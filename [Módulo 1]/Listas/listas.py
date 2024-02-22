# Tipos de Dados - Listas

# Listas basicamente são um conjunto de elementos em sequência
lista_numeros = [
    8,
    16,
    32,
    64,
    128
]

# Aqui nós escrevemos toda a lista
print (
    "Lista de números: ",
    lista_numeros
)


# Aqui nós escrevemos apenas um dos números da lista
print (
    "Acessando o valor",
    lista_numeros[2], # Dessa forma você acessa o valor
    "do endereço",
    lista_numeros.index(32) # E dessa forma o valor da posição em que o número '256' está
)

# Adicionando um novo elemento a lista

lista_numeros.append(256) # Aqui colocamos o elemento 256 na lista veja:

print (
	"Lista de números atualizada com o 256: ",
	lista_numeros
)

# Removendo o elemento criado da lista

lista_numeros.remove(256) # Aqui removemos o 256 da lista de numeros veja:

print (
	"Lista de números atualizada sem o 256",
	lista_numeros
)


