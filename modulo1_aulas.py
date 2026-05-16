#print("Meu Programa em Python")
#teste = "teste"
# a função type() retorna o tipo de dado de uma variável, e o valor da variável é exibido após a vírgula.
#print(type(teste), teste)
#teste1 = 1
#teste2 = 2
# a soma de dois números é feita utilizando o operador +, e o resultado é a soma dos dois números.
#print(teste1 + teste2)

#teste3 = "teste3"
# a função len() retorna o número de caracteres de uma string, incluindo espaços.
#print(len(teste3))
# O python é uma linguagem de programação dinamica e interpretada, ou seja, não precisa ser compilada para ser executada.
# o python é case sensitive, ou seja, diferencia maiúsculas de minúsculas.
# a função input() é utilizada para ler dados do usuário, e o valor digitado é armazenado na variável nome.
#nome = input("Digite seu nome: ")
# a função print() é utilizada para exibir mensagens na tela, e a concatenação de strings é feita utilizando o operador +.
#print("Olá, " + nome + ", Prazer em te conhecer!")

#uma lista é uma coleção de itens ordenada e mutável, que pode conter elementos de diferentes tipos de dados.
#o primeiro elemento de uma lista tem índice 0, o segundo elemento tem índice 1, e assim por diante.

#telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']
#print(f" elemento na posição 0: {telefones[0]}") #imprime o primeiro elemento da lista, que é '1234-5678'

#append é um método utilizado para adicionar um elemento ao final de uma lista.
#telefones.append('5555-5555')
#print(f" metodo append {telefones}") #imprime a lista atualizada, que agora inclui o novo número de telefone '5555-5555' no final da lista.

#o método insert() é utilizado para inserir um elemento em uma posição específica de uma lista, deslocando os elementos subsequentes para a direita.
#telefones.insert(0, '1111-1111')
#print(f" metodo insert {telefones}") #imprime a lista atualizada, que agora inclui o novo número de telefone '1111-1111' na posição 0.

#o método remove() é utilizado para remover a primeira ocorrência de um elemento específico de uma lista. Se o elemento não estiver presente na lista, uma exceção ValueError será levantada.
#telefones.remove('1111-1111')
#print(f" metodo remove {telefones}") #imprime a lista atualizada, que agora não inclui mais

#o método pop() é utilizado para remover um elemento de uma lista com base em seu índice e retornar o valor removido. Se o índice não for especificado, o último elemento da lista será removido e retornado.
#telefones.pop(1) #remove o elemento na posição 1, que é '9999-9999'
#print(f" metodo pop {telefones}") #imprime a lista atualizada, que agora não inclui mais o número de telefone '9999-9999' que foi removido usando o método pop().

#tuplas são semelhantes às listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação da tupla. As tuplas são definidas usando parênteses () em vez de colchetes [].
#contato = ('yan', '324-5678') #cria uma tupla chamada contato com dois elementos: 'yan' e '324-5678'.

#telefones2 = []

#telefones2.append(contato) #adiciona a tupla contato à lista telefones2 usando o método append().

#print(f" tupla {telefones2}") #imprime a lista telefones2, que agora contém a tupla contato como seu único elemento. O resultado será: [('yan', '324-5678')].

#telefones3 = [('yan', '324-5678'), ('ana', '987-6543'), ('maria', '555-5555')] #cria uma lista chamada telefones3 que contém três tuplas, cada uma representando um contato com um nome e um número de telefone.

#print(f" tuplas {telefones3}") #imprime a lista telefones3, que contém as três tuplas de contatos. O resultado será: [('yan', '324-5678'), ('ana', '987-6543'), ('maria', '555-5555')].

# dicionários são estruturas de dados que armazenam pares de chave-valor. Cada chave é única e é usada para acessar o valor correspondente. Os dicionários são definidos usando chaves {} e os pares de chave-valor são separados por dois pontos :.
#telefones3_dict = dict(telefones3) #converte a lista de tuplas telefones3 em um dicionário usando a função dict(). Cada tupla na lista é tratada como um par de chave-valor, onde o primeiro elemento da tupla é a chave e o segundo elemento é o valor.
#print(f" dicionário {telefones3_dict}") #imprime o dicionário telefones3_dict, que agora contém os pares de chave-valor correspondentes aos contatos. O resultado será: {'yan': '324-5678', 'ana': '987-6543', 'maria': '555-5555'}.

#print(telefones3_dict['yan']) #acessa o valor associado à chave 'yan' no dicionário telefones3_dict e imprime o número de telefone correspondente, que é '324-5678'.

#telefones3_dict['Paulo'] = '3456-7890' #adiciona um novo par de chave-valor ao dicionário telefones3_dict, onde a chave é 'Paulo' e o valor é '3456-7890'.
#print(f" dicionário atualizado {telefones3_dict}") #imprime o dicionário telefones3_dict atualizado, que agora inclui o novo par de chave-valor para 'Paulo'. O resultado será: {'yan': '324-5678', 'ana': '987-6543', 'maria': '555-5555', 'Paulo': '3456-7890'}.

#telefones3_dict.pop('Paulo') #remove o par de chave-valor associado à chave 'Paulo' do dicionário telefones3_dict usando o método pop().

#print(f" dicionário atualizado {telefones3_dict}") #imprime o dicionário telefones3_dict atualizado, que agora não inclui mais o par de chave-valor para 'Paulo' que foi removido usando o método pop(). O resultado será: {'yan': '324-5678', 'ana': '987-6543', 'maria': '555-5555'}.


#pacotes são uma forma de organizar módulos relacionados em um diretório. Um pacote é simplesmente um diretório que contém um arquivo __init__.py, que pode estar vazio ou conter código de inicialização para o pacote. Os pacotes permitem que você organize seu código em uma hierarquia de módulos, facilitando a manutenção e a reutilização do código.
#exemplo de pacote: numpy, pandas, matplotlib, scikit-learn, entre outros. Esses pacotes contêm uma variedade de módulos e funções que são amplamente utilizados em ciência de dados, análise de dados, visualização de dados e aprendizado de máquina.
#modulos e pacotes são formas de organizar e reutilizar código em Python. Um módulo é um arquivo que contém definições de funções, classes e variáveis, enquanto um pacote é um diretório que contém um arquivo __init__.py e outros módulos ou subpacotes. Ambos os módulos e pacotes permitem que você importe e utilize código de forma eficiente em seus projetos Python.
#modulos e pacotes são essenciais para a organização e reutilização de código em Python, permitindo que os desenvolvedores criem bibliotecas e frameworks que podem ser facilmente compartilhados e utilizados por outros. Eles ajudam a manter o código limpo, modular e fácil de entender, promovendo a colaboração e a eficiência no desenvolvimento de software.
#exemplo de módulo: math, random, datetime, os, sys, entre outros. Esses módulos fornecem uma variedade de funções e classes que são amplamente utilizadas em diferentes áreas da programação, como matemática, manipulação de arquivos, gerenciamento de tempo e muito mais.
#import meu_modulo
#import pandas as pd
#from meu_modulo import minha_funcao

#import meu_pacote.meu_modulo

#from meu_pacote.meu_modulo import minha_funcao

#Exercicio: Então crie uma lista de alunos e realize as seguintes operações:
#1. Adicione um novo aluno que estão fazendo essa aula.
#2. Um dos alunos desistiu da aula, agora precisa remover ele da lista.
#3. Por fim, use o conceito de dicionário para que possa pesquisar um alunos em especifico nessa lista.

#Aula 6 e 7 - Estruturas de dados, fluxos de controle e loops
#Pilha é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento adicionado é o primeiro a ser removido. Em Python, podemos usar uma lista para implementar uma pilha, utilizando os métodos append() para adicionar elementos e pop() para remover elementos.
pilha = [] #cria uma lista vazia chamada pilha, que será usada para implementar a estrutura de dados de pilha.
pilha.append(1) #adiciona o número 1 à pilha usando o método append().
pilha.append(2) #adiciona o número 2 à pilha usando o
pilha.append(3) #adiciona o número 3 à pilha usando o método append().
print(f" pilha {pilha}") #imprime a pilha atual, que contém os números 1, 2 e 3. O resultado será: pilha [1, 2, 3].
pilha.pop() #remove o último elemento adicionado à pilha, que é o número 3, usando o método pop().
print(f" pilha {pilha}") #imprime a pilha atualizada, que agora contém apenas os números 1 e 2. O resultado será: pilha [1, 2].

#fila é uma estrutura de dados que segue o princípio FIFO (First In, First Out), ou seja, o primeiro elemento adicionado é o primeiro a ser removido. Em Python, podemos usar uma lista para implementar uma fila, utilizando os métodos append() para adicionar elementos e pop(0) para remover elementos.
from collections import deque #importa a classe deque do módulo collections, que é uma estrutura de dados otimizada para operações de fila.
fila = deque() #cria uma fila vazia usando a classe deque.
fila.append(1) #adiciona o número 1 à fila usando o método append
fila.append(2) #adiciona o número 2 à fila usando o método append().
fila.append(3) #adiciona o número 3 à fila usando o método append
print(f" fila {fila}") #imprime a fila atual, que contém os números 1, 2 e 3. O resultado será: fila deque([1, 2, 3]).
fila.popleft() #remove o primeiro elemento adicionado à fila, que é o número 1, usando o método popleft() da classe deque.
print(f" fila {fila}") #imprime a fila atualizada, que agora contém apenas os números 2 e 3. O resultado será: fila deque([2, 3]).

#Fluxos de controles são estruturas que permitem controlar o fluxo de execução do código com base em condições ou repetições. Em Python, os principais fluxos de controle são: if, elif, else.
#loops são estruturas de controle de fluxo que permitem repetir um bloco de código enquanto uma condição for verdadeira. Em Python, os principais tipos de loops são: for e while.
frutas = ['Maça', 'Laranja', 'Banana'] #cria uma lista chamada frutas que contém três elementos: 'Maça', 'Laranja' e 'Banana'.
for fruta in frutas: #inicia um loop for que itera sobre cada elemento da lista
    print(fruta) #imprime o nome da fruta atual em cada iteração do loop. O resultado será: fruta: Maça, fruta: Laranja, fruta: Banana.

num = 1
while num <= 5: #inicia um loop while que continuará executando enquanto a variável num for menor ou igual a 5.
    print(num) #imprime o valor atual de num em cada iteração do loop. O resultado será: 1, 2, 3, 4, 5.
    num += 1 #incrementa o valor de num em 1 a cada iteração do loop, garantindo que o loop eventualmente termine quando num ultrapassar o valor de 5.

#1. Crie uma lista e use a declaração da lista.
#2. Depois aplique os principios de pilha, fila e lista que aprendemos nessa aula, adicionando e inserindo frutas.
#3. Utilize o laço de repetição para imprimir todos os elementos dessa lista.
#4. e por fim, crie condições para imprimir somente a maça e laranja. Você só pode imprimir maçã e laranja.