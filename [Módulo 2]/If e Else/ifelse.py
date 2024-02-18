# Controle de Fluxo - If e Else

print("Descubra se o número é impar ou par!")

# Aqui a variável 'numero' está recebendo o a entrada do usuário mas apenas com o tipo int()

numero = int(input("> "))

# Aqui estamos calculando se dividir 'numero' por 2, irá restar 0
# Se restar 0 então é par

if numero % 2 == 0:
    print(numero, "é um número é par!")
# Se não restar 0 na divisão por 2 então é impar
else:
    print(numero, "é um número ímpar")