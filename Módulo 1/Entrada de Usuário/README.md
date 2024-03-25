# Entrada do usuário

Como todo bom programa, é necessário que o usuário tenha a possibilidade de interação nele, para isso usamos a função ```input()```que nos possibilita essa opção de forma muito conveniente.
No código a seguir perceba que passamos a função ```input()``` para a variável ```recebe```, isto permitirá com que o que o usuário(a) escrever dali para frente será armazenado em seguida na variável ```recebe```. Com o comando ```print()``` podemos ver de forma mais clara o que foi armazenado.
```python
    recebe = input()
    print(recebe)
```

## Boas práticas

"O que acontece se eu passar um número para ```input()```?" Ora, nada. "E se por acaso for decimal?" Não ocorre coisa alguma. "E se for um texto ou qualquer outra informação?" a função continua a receber normalmente qualquer tipo de dado que o usuário digitar. "Ah mas então isso é bom pois não há barreiras para a passagens de valores para a variável ```recebe```.", é justamente aí que mora o problema.
Em um programa de computador nunca teremos a garantia de que as pessoas o utilizarão da forma como pensamos que ele deve ser usado, as pessoas podem tanto cometer acidentes em inserir valores incorretos causando erros ou propositalmente forçar a inserção de dados incorretos para explorar vulnerabilidades no sistema. Para além disso é necessário exercer um controle maior sobre o que vai ou não ser armazenado no seu programa. Para tal veja o seguinte código:
```python
    nome = str(input("> Qual o seu nome?: "))
    idade = int(input("> Quantos anos você tem?: "))

    print("> Olá", nome, "você tem", idade, "anos!")
```
No código acima vemos que a variável ```nome``` recebe ```input()``` entre parênteses como parâmetro de ```str()```. Isso significa que tudo o que vai ser passado para nome, tem e deve ser objetivamente dados de texto.
Na segunda linha o mesmo ocorre com ``idade`` que agora obrigatoriamente vai exigir que todo e qualquer dado de idade que o usuário inserir deve ser um número inteiro, ou seja, um dado ``int()``.
A seguir tudo que é passado pelo usuário para as variáveis é impresso na tela através do ```print()``. 
