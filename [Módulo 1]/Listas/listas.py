

#Listas basicamente são um conjunto de elementos em sequencia


lista_numeros = [1, 2, 3, 4, 5]

# E como adiciono um novo numero na lista?

lista_numeros.append(6) 

# Se quiser acessar um numero dentro da lista

lista_numeros[3] = 10

# Você acessou o numero '3' dentro da lista
# Removendo o segundo elemento da lista (índice 1)
del lista_numeros[1]

# Imprimindo a lista resultante
print(lista_numeros)  # Saída: [1, 3, 10, 5, 6]
