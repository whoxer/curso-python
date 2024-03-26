# Operadores Aritméticos

Assim como em todas as outras linguagens de programação e em vários seguimentos da nossa vida, nós precisamos da matemática e seus operadores aritméticos para diversas coisas. Seja para a soma de pontos do jogador em um jogo que estamos desenvolvendo ou para calcularmos a colisão de um objeto com outro. As possibilidades são finitas e Python não ficaria de fora disso lógicamente :D.
Veja o código a seguir:
```python
    print("Esse é o resultado das respectivas operações matemáticas: ")
    print("1 + 1 =", 1 + 1)
```
Através dessa forma você é capaz de utilizar o próprio Python como uma calculadora pessoal através de um simples script. Poderíamos torná-lo um pouco mais complexo com o que se segue.
```python
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    print('Esta é o resultado da soma de', numero1, 'com', numero2, ':', numero1 + numero2)
```
O código acima permite com que os dados passados pelo usuário(a) sejam somados e exibidos o resultado na função ```print()```.

## Outras utilidades

Os operadores aritméticos do Python não servem apenas para a soma de números, subtração ou multiplicação, você pode somar e multiplicar o texto também ;D.

A exemplo prático:

```python
    texto = 'Seremos todos como Che!'
    print(texto + ' Viva ao Socialismo!')
```
ou

```python
    texto = 'Cuba livre!\n'
    print(texto * 4)
```

Note que ao final de ```texto = 'Cuba livre!\n'```foi adicionado um ``'\n'``, isso é um "newline", quer dizer que todo final de frase impressa pelo ``print()`` ele vai pular uma linha.
