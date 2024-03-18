# Controle de Fluxo - Loop While

# Variável recebe verdadeiro
continuar_rodando = True

# Enquanto o programar continuar rodando for igual a verdadeiro, ele vai receber 
# um valor inteiro da variável
while continuar_rodando == True:
    recebe_numero = int(input("Digite um número que seja par: "))
    
    if recebe_numero % 2 == 0:
        print(recebe_numero, " é um número par!")
        continuar_rodando = False
    else:
        print(recebe_numero, " não é um número par, tente novamente\n")