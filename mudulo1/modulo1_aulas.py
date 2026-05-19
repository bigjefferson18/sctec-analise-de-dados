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
#pilha = [] #cria uma lista vazia chamada pilha, que será usada para implementar a estrutura de dados de pilha.
#pilha.append(1) #adiciona o número 1 à pilha usando o método append().
#pilha.append(2) #adiciona o número 2 à pilha usando o
#pilha.append(3) #adiciona o número 3 à pilha usando o método append().
#print(f" pilha {pilha}") #imprime a pilha atual, que contém os números 1, 2 e 3. O resultado será: pilha [1, 2, 3].
#pilha.pop() #remove o último elemento adicionado à pilha, que é o número 3, usando o método pop().
#print(f" pilha {pilha}") #imprime a pilha atualizada, que agora contém apenas os números 1 e 2. O resultado será: pilha [1, 2].

#fila é uma estrutura de dados que segue o princípio FIFO (First In, First Out), ou seja, o primeiro elemento adicionado é o primeiro a ser removido. Em Python, podemos usar uma lista para implementar uma fila, utilizando os métodos append() para adicionar elementos e pop(0) para remover elementos.
#from collections import deque #importa a classe deque do módulo collections, que é uma estrutura de dados otimizada para operações de fila.
#fila = deque() #cria uma fila vazia usando a classe deque.
#fila.append(1) #adiciona o número 1 à fila usando o método append
#fila.append(2) #adiciona o número 2 à fila usando o método append().
#fila.append(3) #adiciona o número 3 à fila usando o método append
#print(f" fila {fila}") #imprime a fila atual, que contém os números 1, 2 e 3. O resultado será: fila deque([1, 2, 3]).
#fila.popleft() #remove o primeiro elemento adicionado à fila, que é o número 1, usando o método popleft() da classe deque.
#print(f" fila {fila}") #imprime a fila atualizada, que agora contém apenas os números 2 e 3. O resultado será: fila deque([2, 3]).

#Fluxos de controles são estruturas que permitem controlar o fluxo de execução do código com base em condições ou repetições. Em Python, os principais fluxos de controle são: if, elif, else.
#loops são estruturas de controle de fluxo que permitem repetir um bloco de código enquanto uma condição for verdadeira. Em Python, os principais tipos de loops são: for e while.
#frutas = ['Maça', 'Laranja', 'Banana'] #cria uma lista chamada frutas que contém três elementos: 'Maça', 'Laranja' e 'Banana'.
#for fruta in frutas: #inicia um loop for que itera sobre cada elemento da lista
#    print(fruta) #imprime o nome da fruta atual em cada iteração do loop. O resultado será: fruta: Maça, fruta: Laranja, fruta: Banana.

#num = 1
#while num <= 5: #inicia um loop while que continuará executando enquanto a variável num for menor ou igual a 5.
#    print(num) #imprime o valor atual de num em cada iteração do loop. O resultado será: 1, 2, 3, 4, 5.
#    num += 1 #incrementa o valor de num em 1 a cada iteração do loop, garantindo que o loop eventualmente termine quando num ultrapassar o valor de 5.

#1. Crie uma lista e use a declaração da lista.
#2. Depois aplique os principios de pilha, fila e lista que aprendemos nessa aula, adicionando e inserindo frutas.
#3. Utilize o laço de repetição para imprimir todos os elementos dessa lista.
#4. e por fim, crie condições para imprimir somente a maça e laranja. Você só pode imprimir maçã e laranja.

#Aula 8 e 9 - Aplicando o conhecimento de estruturas de dados, fluxos de controle.
# condicionais são estruturas de controle de fluxo que permitem executar blocos de código com base em condições específicas. Em Python, os principais tipos de condicionais são: if, elif e else.
#hora = 9 #atribui o valor 9 à variável hora, que representa a hora do dia.
#humor = 'sono' #atribui a string 'sono' à variável humor, que representa o estado de espírito da pessoa.

#if humor == 'sono' and hora < 10: #inicia uma estrutura condicional if que verifica se o humor é 'sono' e a hora é menor que 10.
#    print("Café") #imprime a palavra "Café" se a condição do if for verdadeira, ou seja, se o humor for 'sono' e a hora for menor que 10.
#elif humor == 'sedento' or hora < 2: #inicia uma estrutura condicional elif que verifica se o humor é 'sedento' ou a hora é menor que 2.
#    print("Limonada") #imprime a palavra "Limonada" se a condição do elif for verdadeira, ou seja, se o humor for 'sedento' ou a hora for menor que 2.
#else: #inicia uma estrutura condicional else que será executada se nenhuma das condições anteriores for verdadeira.
#    print("Água") #imprime a palavra "Água" se a condição do else for executada, ou seja, se o humor não for 'sono' nem 'sedento', e a hora não for menor que 10 nem menor que 2.   


#praticar o laço de repetição for, planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno'] #cria uma lista chamada planetas que contém os nomes dos planetas do sistema solar.
#planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno'] #cria uma lista chamada planetas que contém os nomes dos planetas do sistema solar.

#for planeta in planetas: #inicia um loop for que itera sobre cada elemento da lista planetas, atribuindo o nome do planeta atual à variável planeta em cada iteração.
#    print(f'planeta: {planeta}') #imprime o nome do planeta atual em cada iteração do loop, formatando a string para exibir "planeta: " seguido pelo nome do planeta. O resultado será: planeta: Mercúrio, planeta: Vênus, planeta: Terra, planeta: Marte, planeta: Júpiter, planeta: Saturno, planeta: Urano, planeta: Netuno.


#funcão range() é uma função embutida em Python que gera uma sequência de números inteiros. Ela é comumente usada em loops for para iterar sobre um intervalo de números. A função range() pode ser chamada com um, dois ou três argumentos: range(stop), range(start, stop) ou range(start, stop, step).
#for i in range(5): #inicia um loop for que itera sobre uma sequência de números gerada pela função range(5), que cria uma sequência de números inteiros de 0 a 4.
#    print(f'i: {i}') #imprime o valor atual de i em cada iteração do loop, formatando a string para exibir "i: " seguido pelo valor de i. O resultado será: i: 0, i: 1, i: 2, i: 3, i: 4.

#laço while é uma estrutura de controle de fluxo que permite repetir um bloco de código enquanto uma condição for verdadeira. O loop while é útil quando não sabemos de antemão quantas vezes o loop deve ser executado, ou quando queremos criar um loop infinito que só será interrompido por uma condição específica.
#i = 0 #atribui o valor 0 à variável i, que será usada como contador para o loop while.
#while i < 10: #inicia um loop while que continuará executando enquanto a variável i for menor que 10.
#    print(f'{i}', end=' ') #imprime o valor atual de i em cada iteração do loop, formatando a string para exibir apenas o valor de i. O argumento end=' ' é usado para evitar que a função print() adicione uma nova linha após cada impressão, resultando em uma saída contínua dos números de 0 a 9 separados por espaços.
#    i += 1 #incrementa o valor de i em 1 a cada iteração do loop, garantindo que o loop eventualmente termine quando i atingir o valor de 10. O resultado será: 0 1 2 3 4 5 6 7 8 9.


#Exercicio:
#1. Utilize o laço de repetição ´for' para contar ou iterar entre um intervalo de números e imprimir no terminal todos os números pares dentro desse intervalo de números.
#2. Escreva um programa que solicita ao usuário dois números: o início e o fim de um intervalo [inclusivos].
#3. O programa deve imprimir todos os números pares dentro desse intervalo.
# O resultado desse código, seria apresentar no terminal os números pares entre 1 e 10, que seriam: 2, 4, 6, 8 e 10. O programa deve ser capaz de lidar com qualquer intervalo de números fornecido pelo usuário, garantindo que apenas os números pares sejam exibidos no resultado.


#Aulas 10 e 11 - Programação funcional e lidando com erros de Programação.
#programação funcional é um paradigma de programação que trata a computação como a avaliação de funções matemáticas e evita o estado mutável e os efeitos colaterais. definir funções é uma parte fundamental da programação funcional, permitindo que você crie blocos de código reutilizáveis e modulares. Em Python, as funções são definidas usando a palavra-chave def, seguida pelo nome da função e parênteses que podem conter parâmetros. O corpo da função é indentado e pode conter uma declaração return para retornar um valor.
#função é um bloco de código reutilizável que realiza uma tarefa específica. As funções permitem que você organize seu código, evite repetição e torne seu programa mais modular e fácil de entender. Em Python, as funções são definidas usando a palavra-chave def, seguida pelo nome da função e parênteses que podem conter parâmetros. O corpo da função é indentado e pode conter uma declaração return para retornar um valor.
#programação procedural é um paradigma de programação que se concentra na criação de procedimentos ou rotinas para manipular dados. Em programação procedural, o código é organizado em blocos de código chamados procedimentos ou funções, que são executados em uma sequência específica. A programação procedural é baseada em uma abordagem top-down, onde o programa é dividido em partes menores e mais gerenciáveis, facilitando a compreensão e a manutenção do código. Em Python, a programação procedural é suportada por meio da definição de funções e do uso de estruturas de controle de fluxo para organizar a execução do código.
#paradigama programação orientada a objetos é um paradigma de programação que se concentra na criação de objetos que encapsulam dados e comportamentos relacionados. Em programação orientada a objetos, o código é organizado em classes, que são moldes para criar objetos. Cada objeto é uma instância de uma classe e pode ter atributos (dados) e métodos (comportamentos). A programação orientada a objetos promove a reutilização de código, a modularidade e a organização do código, facilitando a manutenção e a escalabilidade dos programas. Em Python, a programação orientada a objetos é suportada por meio da definição de classes e da criação de objetos a partir dessas classes.
#paradigama declarativo é um paradigma de programação que se concentra em descrever o que o programa deve fazer, em vez de como ele deve fazer. Em programação declarativa, o código é escrito de forma a expressar a lógica do programa sem especificar os detalhes de implementação. A programação declarativa é baseada em uma abordagem bottom-up, onde o programa é construído a partir de componentes menores e mais abstratos. Em Python, a programação declarativa pode ser alcançada por meio do uso de expressões lambda, compreensão de listas e outras construções que permitem escrever código de forma mais concisa e expressiva.

#def pure_increments(elements, index):
#    elements[index] += 1
#    return elements

#lista = [1, 2, 3, 4, 5 ,6, 7, 8, 9]

#print(pure_increments(lista, 0))

#print(lista)

#def pure_increments(elements, index):
#     new_elements = elements.copy()  # Cria uma cópia da lista original para evitar mutação
#     new_elements[index] += 1
#     return new_elements

# lista = [1, 2, 3, 4, 5 ,6, 7, 8, 9]

# print(pure_increments(lista, 0))

# print(lista)

#alguns funções nativas do python são puras, como a função sorted(), que retorna uma nova lista ordenada sem modificar a lista original.
#map é uma função nativa do Python que aplica uma função a cada item de um iterável (como uma lista) e retorna um iterador com os resultados. A função map() é considerada uma função pura, pois não modifica o iterável original e sempre retorna o mesmo resultado para os mesmos argumentos.
#função filter() é uma função nativa do Python que constrói um iterador a partir de elementos de um iterável para os quais uma função retorna verdadeiro. A função filter() é considerada uma função pura, pois não modifica o iterável original e sempre retorna o mesmo resultado para os mesmos argumentos.
# Erro de exceção é um evento que ocorre durante a execução de um programa e interrompe o fluxo normal do programa. Em Python, as exceções são tratadas usando blocos try,except e finally. O bloco try contém o código que pode gerar uma exceção, o bloco except contém o código que será executado se uma exceção ocorrer, e o bloco finally contém o código que será executado independentemente de uma exceção ter ocorrido ou não. O tratamento de exceções é importante para garantir que seu programa possa lidar com erros de forma graciosa e evitar falhas inesperadas.


# def dividir(a, b):
#     try:
#         resultado = a / b
#         return resultado
#     except ZeroDivisionError:
#         print("Erro: Divisão por zero não é permitida.")
#     except TypeError:
#         print("Erro: Ambos os argumentos devem ser números.")
#     except Exception as e:
#         print(f"Erro inesperado: {e}")
#     finally:
#         print("Operação de divisão concluída.")

# dividir(10, 2)  # Saída: 5.0
# dividir(10, 0) # Saída: Erro: Divisão por zero não é permitida.
# dividir(10, 'a')  # Saída: Erro: Ambos os argumentos devem ser números.


#programação orientada a objetos é um paradigma de programação que se concentra na criação de objetos que encapsulam dados e comportamentos relacionados. Em programação orientada a objetos, o código é organizado em classes, que são moldes para criar objetos. Cada objeto é uma instância de uma classe e pode ter atributos (dados) e métodos (comportamentos). A programação orientada a objetos promove a reutilização de código, a modularidade e a organização do código, facilitando a manutenção e a escalabilidade dos programas. Em Python, a programação orientada a objetos é suportada por meio da definição de classes e da criação de objetos a partir dessas classes.   
#uma classe é um molde para criar objetos, definindo atributos e métodos que os objetos criados a partir da classe terão. Em Python, as classes são definidas usando a palavra-chave class, seguida pelo nome da classe e dois pontos. O corpo da classe é indentado e pode conter atributos (variáveis) e métodos (funções) que definem o comportamento dos objetos criados a partir da classe. A criação de objetos a partir de uma classe é feita instanciando a classe, ou seja, chamando a classe como se fosse uma função e atribuindo o resultado a uma variável.
#propriedades são atributos de uma classe que são acessados como se fossem atributos normais, mas na verdade são métodos que calculam ou retornam um valor com base em outros atributos da classe. Em Python, as propriedades são definidas usando o decorador @property, que permite que um método seja acessado como um atributo. As propriedades são úteis para encapsular a lógica de cálculo ou validação de um atributo, permitindo que você controle o acesso e a modificação dos dados de forma mais eficiente e segura.
#comportamentos são as ações ou métodos que um objeto pode realizar. Em programação orientada a objetos, os comportamentos são definidos como métodos dentro de uma classe. Os métodos são funções que operam nos dados (atributos) de um objeto e podem ser chamados para executar uma ação específica. Os comportamentos permitem que os objetos interajam uns com os outros e realizem tarefas, tornando a programação orientada a objetos uma abordagem poderosa para modelar o mundo real e criar software modular e reutilizável.

# class Pessoa:
#     def __init__(self, nome, idade, altura):
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura

#         def apresentar(self):
#             print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha altura é {self.altura} metros.")

# p1 = Pessoa("João", 30, "1,80")
# p1.apresentar()
# p2 = Pessoa("Karina", 28, "1,70")
# p2.apresentar()


#1. Crie uma classe chamada Carro;
#2. Defina seus atributos, devem conter: modelo, marca e ano;
#3. Em seguida, crie os seguintes métodos: mostrarplaca() e ao instaciar a classe a partir de um objeto, mostre a placa deste veiculo.


#encapsular significa ocultar os detalhes internos de uma classe e fornecer uma interface pública para interagir com os objetos dessa classe. Em Python, o encapsulamento é alcançado usando convenções de nomenclatura para indicar que um atributo ou método é privado (por exemplo, prefixando o nome com um sublinhado _). O encapsulamento ajuda a proteger os dados e a lógica interna de uma classe, permitindo que você controle o acesso e a modificação dos atributos e métodos, promovendo a segurança e a integridade dos objetos criados a partir da classe.
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos e minha altura é {self.altura} metros.")

    def get_nome(self):
        return self.__nome
        
    def set_idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválida. A idade deve ser um número positivo.")
        elif nova_idade > 120:
            print("Idade inválida. A idade deve ser um número realista.")
        elif nova_idade < self.__idade:
            print("Idade inválida. A nova idade não pode ser menor que a idade atual.")
        else:
            self.__idade = nova_idade


p1 = Pessoa("João", 30, "1,80")
p1.apresentar()
p2 = Pessoa("Karina", 28, "1,70")
p2.apresentar()

p1.set_idade(25) # Tenta definir uma idade menor que a atual, o que é inválido
p1.set_idade(150) # Tenta definir uma idade irrealista, o que é inválido
p1.set_idade(-5) # Tenta definir uma idade negativa, o que é inválido
p1.set_idade(35) # Define uma idade válida
p1.apresentar() # Apresenta a pessoa com a nova idade definida


print(p1.get_nome())

#conceito de herança é um princípio fundamental da programação orientada a objetos que permite criar uma nova classe (chamada classe filha ou subclasse) a partir de uma classe existente (chamada classe pai ou superclasse). A classe filha herda os atributos e métodos da classe pai, permitindo que você reutilize código e crie hierarquias de classes. Em Python, a herança é implementada definindo a classe filha com o nome da classe pai entre parênteses. A classe filha pode adicionar novos atributos e métodos ou sobrescrever os métodos da classe pai para fornecer uma implementação específica. A herança promove a reutilização de código, a modularidade e a organização do código, facilitando a manutenção e a escalabilidade dos programas orientados a objetos.

# class Aluno(Pessoa):
#     def __init__(self, nome, idade, altura, matricula):
#         super().__init__(nome, idade, altura)
#         self.matricula = matricula
    
#     def estudante(self):
#         print(f'A matrícula do aluno {self.get_nome()} é {self.matricula}.')

# aluno1 = Aluno("Pedro", 30, "1,90", "000678908")

# aluno1.estudante()

#polimorfismo é um princípio fundamental da programação orientada a objetos que permite que objetos de diferentes classes sejam tratados como objetos da mesma classe através de uma interface comum. O polimorfismo é alcançado por meio da herança e da sobrescrita de métodos, permitindo que uma classe filha forneça uma implementação específica de um método definido na classe pai. Em Python, o polimorfismo é suportado por meio do uso de métodos e atributos comuns em classes relacionadas, permitindo que você escreva código que pode trabalhar com objetos de diferentes classes de forma transparente, promovendo a flexibilidade e a reutilização do código em programas orientados a objetos.

class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura)
        self.matricula = matricula
    
    def estudante(self):
        print(f'A matrícula do aluno {self.get_nome()} é {self.matricula}.')
    
    def apresentar(self):
        print(f"Olá, meu nome é {super().get_nome()} e minha matrícula é {self.matricula}.")

aluno1 = Aluno("Pedro", 30, "1,90", "000678908")

aluno1.estudante()
aluno1.apresentar()

#Livros, filmes, documentários, sites e canais recomendados:
#1. "Introdução à Programação com Python" de Nilo Ney Coutinho Menezes
#2. "Python_Podcast_br" - Podcast em português sobre Python e desenvolvimento de software.
#3. "Moneyball" - Filme baseado em uma história real sobre como o uso de dados e estatísticas revolucionou o beisebol.
#4. "A era dos dados" - Documentário que explora o impacto dos dados e da inteligência artificial na sociedade.
#5. "w3schools" - Site com tutoriais e referências sobre diversas linguagens de programação, incluindo Python.