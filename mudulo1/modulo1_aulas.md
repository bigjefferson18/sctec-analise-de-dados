# 📝 Módulo 1: Fundamentos de Python, Estruturas de Dados e POO

Este documento reúne todas as anotações teóricas, explicações de conceitos e exemplos práticos desenvolvidos ao longo das aulas do Módulo 1.

---

## 📌 Índice

- [📝 Módulo 1: Fundamentos de Python, Estruturas de Dados e POO](#-módulo-1-fundamentos-de-python-estruturas-de-dados-e-poo)
  - [📌 Índice](#-índice)
  - [1. Verificação de Tipos e Variáveis](#1-verificação-de-tipos-e-variáveis)
  - [2. Operações Matemáticas](#2-operações-matemáticas)
  - [3. Manipulação de Strings](#3-manipulação-de-strings)
  - [4. Características da Linguagem](#4-características-da-linguagem)
  - [5. Interação com o Usuário](#5-interação-com-o-usuário)
  - [6. Listas (Arrays Dinâmicos)](#6-listas-arrays-dinâmicos)
    - [6.1. Índices e Acesso](#61-índices-e-acesso)
    - [6.2. Manipulação de Elementos](#62-manipulação-de-elementos)
  - [💡 Resumo de Métodos de Lista](#-resumo-de-métodos-de-lista)
  - [7. Tuplas (Imutabilidade)](#7-tuplas-imutabilidade)
  - [8. Dicionários (Pares Chave-Valor)](#8-dicionários-pares-chave-valor)
  - [9. Módulos e Pacotes](#9-módulos-e-pacotes)
  - [10. Estruturas de Dados Avançadas (Pilhas e Filas)](#10-estruturas-de-dados-avançadas-pilhas-e-filas)
    - [10.1. Pilha (LIFO - Last In, First Out)](#101-pilha-lifo---last-in-first-out)
    - [10.2. Fila (FIFO - First In, First Out)](#102-fila-fifo---first-in-first-out)
  - [11. Fluxos de Controle e Laços de Repetição](#11-fluxos-de-controle-e-laços-de-repetição)
    - [11.1. Estruturas Condicionais (if, elif, else)](#111-estruturas-condicionais-if-elif-else)
    - [11.2. Laço for](#112-laço-for)
    - [11.3. Laço while](#113-laço-while)
  - [12. Paradigmas de Programação e Programação Funcional](#12-paradigmas-de-programação-e-programação-funcional)
    - [⚙️ Funções Nativas Puras:](#️-funções-nativas-puras)
  - [13. Tratamento de Exceções e Erros](#13-tratamento-de-exceções-e-erros)
  - [14. Programação Orientada a Objetos (POO)](#14-programação-orientada-a-objetos-poo)
    - [14.1. Encapsulamento](#141-encapsulamento)
    - [14.2. Herança e Polimorfismo](#142-herança-e-polimorfismo)
  - [15. 📝 Exercícios de Fixação Resolvidos](#15--exercícios-de-fixação-resolvidos)
    - [Exercício 1: Cálculo de Idade Futura](#exercício-1-cálculo-de-idade-futura)
    - [Exercício 2: Sistema de Manipulação de Alunos (Listas e Dicionários)](#exercício-2-sistema-de-manipulação-de-alunos-listas-e-dicionários)
    - [Exercício 3: Impressão Controlada de Intervalos Pares](#exercício-3-impressão-controlada-de-intervalos-pares)
    - [Exercício 4: Instanciação Básica de Objeto (Classe Carro)](#exercício-4-instanciação-básica-de-objeto-classe-carro)
  - [16. 📚 Recomendações de Conteúdo](#16--recomendações-de-conteúdo)

---

## 1. Verificação de Tipos e Variáveis

Em Python, podemos descobrir a natureza de qualquer dado utilizando funções integradas.

```python
teste = "teste"
# A função type() retorna o tipo de dado de uma variável.
print(type(teste), teste)
```

## 2. Operações Matemáticas

O Python permite realizar cálculos de forma direta utilizando operadores aritméticos.

```python
teste1 = 1
teste2 = 2
# A soma de dois números é feita utilizando o operador +
print(teste1 + teste2)
```

## 3. Manipulação de Strings

Podemos medir e transformar textos utilizando funções específicas para strings.

```python
teste3 = "teste3"
# A função len() retorna o número de caracteres de uma string, incluindo espaços.
print(len(teste3))
```

## 4. Características da Linguagem

- Dinâmica e Interpretada: O código é executado linha a linha por um interpretador, sem necessidade de compilação prévia.

- Case Sensitive: Python diferencia letras maiúsculas de minúsculas (ex: `Nome` é diferente de `nome`).

## 5. Interação com o Usuário

O fluxo básico de entrada e saída de dados funciona da seguinte forma:

```python
# A função input() lê dados digitados pelo usuário.
nome = input("Digite seu nome: ")

# A função print() exibe mensagens na tela.
# A concatenação (junção) de strings é feita utilizando o operador +.
print("Olá, " + nome + ", Prazer em te conhecer!")
```

## 6. Listas (Arrays Dinâmicos)
Uma lista em Python é uma coleção de itens ordenada e mutável. Isso significa que a ordem importa e você pode alterar os elementos depois que a lista foi criada.
### 6.1. Índices e Acesso
O Python utiliza indexação baseada em zero. Ou seja, a contagem sempre começa do 0.
```python
# Definindo uma lista de strings
telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']

# Acessando o primeiro elemento (índice 0)
print(telefones[0])  # Saída: '1234-5678'
```
### 6.2. Manipulação de Elementos
Existem métodos específicos para adicionar novos dados à lista, dependendo de onde você quer que eles fiquem:
```append()```: Adiciona o item ao final da lista.
```insert(índice, valor)```: Insere o item em uma posição específica, "empurrando" os outros para a direita.

```python
# Adicionando ao final
telefones.append('5555-5555')
print(telefones) 

# Inserindo na primeira posição (índice 0)
telefones.insert(0, '1111-1111')
print(telefones) 
```
## 💡 Resumo de Métodos de Lista
| Método | O que faz | Exemplo |
| :--- | :--- | :--- |
| ```append``` | Adiciona no fim | ```lista.append('novo')``` |
| ```insert``` | Adiciona em qualquer lugar | ```lista.insert(1, 'segundo')``` |
| ```pop``` | Remove o último item | ```lista.pop()``` |
| ```sort``` | Ordena a lista | ```lista.sort()``` |
| ```remove```| Remove o elemento da lista | ```lista.remove('555-5555')``` |

## 7. Tuplas (Imutabilidade)

Tuplas são muito parecidas com listas, mas com uma diferença crucial: elas são imutáveis. Uma vez criada, você não pode alterar, adicionar ou remover elementos dela.

- **Sintaxe**: Usa parênteses ```()``` (enquanto listas usam ```[]```).

- **Uso Comum**: Dados que não devem mudar, como coordenadas geográficas ou configurações fixas.

```python

# Criando uma tupla
contato = ('yan', '324-5678')

# Podemos guardar tuplas dentro de listas
telefones2 = []
telefones2.append(contato)

print(f"Lista contendo uma tupla: {telefones2}") 
# Resultado: [('yan', '324-5678')]
```

## 8. Dicionários (Pares Chave-Valor)

Dicionários são coleções poderosas onde você acessa um valor através de uma chave única, em vez de um índice numérico.

- Sintaxe: Usa chaves `{}` e o formato `chave: valor`.

```python

# Convertendo uma lista de tuplas em um dicionário
telefones3 = [('yan', '324-5678'), ('ana', '987-6543'), ('maria', '555-5555')]
telefones3_dict = dict(telefones3)

# Acessando um valor pela chave
print(telefones3_dict['yan'])  # Saída: '324-5678'

# Adicionando/Atualizando dados
telefones3_dict['Paulo'] = '3456-7890'

# Removendo dados com pop()
telefones3_dict.pop('Paulo')
```

## 9. Módulos e Pacotes

São formas fundamentais para organizar e reutilizar código em Python, promovendo a modularidade e mantendo o código limpo.

- **Módulo**: É um arquivo único contendo a extensão `.py` com definições de funções, classes e variáveis (ex: `math`, `random`, `datetime`, `os`, `sys`).

- **Pacote**: É um diretório/pasta que reúne vários módulos relacionados. Para ser reconhecido, historicamente continha um arquivo `__init__.py`. Exemplos famosos em análise de dados incluem `numpy`, `pandas`, `matplotlib` e `scikit-learn`.
- 
```python
import pandas as pd
from math import sqrt
```

## 10. Estruturas de Dados Avançadas (Pilhas e Filas)

Dependendo de como inserimos e removemos os dados de uma lista, simulamos estruturas clássicas:
### 10.1. Pilha (LIFO - Last In, First Out)

O último elemento adicionado é o primeiro a ser removido (como uma pilha de pratos).

- Adicionar: `append()`

- Remover: `pop()`

### 10.2. Fila (FIFO - First In, First Out)

O primeiro elemento adicionado é o primeiro a ser removido (como uma fila de banco). Para melhor performance computacional, utilizamos a classe estruturada deque do módulo collections.

- Adicionar: `append()`

- Remover: `popleft()`

## 11. Fluxos de Controle e Laços de Repetição
### 11.1. Estruturas Condicionais (if, elif, else)

Permitem controlar o fluxo de execução com base em condições lógicas utilizando operadores como and e or.

```python
hora = 9
humor = 'sono'

if humor == 'sono' and hora < 10:
    print("Café")
elif humor == 'sedento' or hora < 2:
    print("Limonada")
else:
    print("Água")
```
### 11.2. Laço for

Utilizado para iterar ou percorrer coleções conhecidas item por item. A função embutida range(start, stop, step) é usada para gerar sequências numéricas inteiras.
```python
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte']
for planeta in planetas:
    print(f'Planeta: {planeta}')
```
### 11.3. Laço while

Executa um bloco de código repetidamente enquanto uma condição lógica se mantiver verdadeira. Exige um ponto de parada ou incremento para evitar loops infinitos.

## 12. Paradigmas de Programação e Programação Funcional

O Python é uma linguagem multiparadigma, aceitando diferentes formas de estruturar o desenvolvimento:

- **Programação Procedural**: Focada em procedimentos, rotinas sequenciais e funções estruturadas de cima para baixo (top-down).

- **Programação Declarativa**: Concentra-se em descrever o que o programa deve fazer, e não como fazer (ex: expressões lambda, compreensões de lista).

- **Programação Funcional**: Trata a computação como avaliações de funções matemáticas, evitando estados mutáveis e efeitos colaterais através de funções puras (funções que não alteram os dados originais recebidos).

```python
# Exemplo de Função Pura (Não modifica a lista original, usa .copy())
def pure_increments(elements, index):
     new_elements = elements.copy()
     new_elements[index] += 1
     return new_elements
```
### ⚙️ Funções Nativas Puras:

- `sorted()`: Ordena elementos retornando uma nova lista sem modificar a original.

- `map()`: Aplica uma função específica sobre cada item de um iterável.

- `filter()`: Filtra e constrói um iterador contendo apenas elementos que retornem verdadeiro para uma dada condição.

## 13. Tratamento de Exceções e Erros

Exceções são eventos que ocorrem durante a execução e interrompem o fluxo normal do script. Tratamos erros de forma graciosa usando as cláusulas try, except e finally.

```python
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except TypeError:
        print("Erro: Ambos os argumentos devem ser números.")
    finally:
        print("Operação de divisão concluída.")
```

## 14. Programação Orientada a Objetos (POO)

Paradigma que foca na criação de Objetos que encapsulam dados (atributos) e comportamentos (métodos) relacionados.

- **Classe**: É o molde ou contrato base do mundo real usado para construir os objetos (instâncias).

- **Atributos (Propriedades)**: Variáveis internas contendo as características do objeto.

- **Métodos (Comportamentos)**: Funções internas que determinam as ações que o objeto pode realizar.

### 14.1. Encapsulamento

Significa ocultar detalhes internos de funcionamento e proteger o acesso direto aos dados. Em Python, usamos a convenção de prefixar atributos com sublinhado duplo (`__`) para torná-los estritamente privados. O acesso controlado passa a ser feito por métodos de leitura/escrita (`Getters` e `Setters`).
### 14.2. Herança e Polimorfismo

- **Herança**: Permite criar uma classe filha (subclasse) que herda automaticamente os atributos e métodos de uma classe pai (superclasse), reutilizando código.

- **Polimorfismo**: Permite que subclasses compartilhem assinaturas de métodos idênticas, porém com comportamentos e implementações internas totalmente diferentes/sobrescritas. Usamos `super()` para invocar rotinas originais da classe pai.

```python
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome # Atributo Privado
        self.__idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome} e tenho {self.__idade} anos.")

    def get_nome(self):
        return self.__nome

# Aplicando Herança
class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura)
        self.matricula = matricula
    
    # Aplicando Polimorfismo (Sobrescrita de método)
    def apresentar(self):
        print(f"Olá, meu nome é {super().get_nome()} e minha matrícula é {self.matricula}.")
```
## 15. 📝 Exercícios de Fixação Resolvidos

Nesta seção encontram-se as implementações reais dos desafios passados em aula, extraídos do arquivo `pratica_python.py`.
### Exercício 1: Cálculo de Idade Futura
```python
nome = input("Qual é o seu nome: ")
idade = int(input("Qual é a sua idade: "))
print(f"Olá {nome}, você terá {(2030 - (2026 - idade))} anos em 2030!")
```
### Exercício 2: Sistema de Manipulação de Alunos (Listas e Dicionários)
```python
# 1. Criação e manipulação de listas
alunos = ['ana', 'bruno', 'helio', 'aragao', 'jefferson']
alunos.append('jorge')
alunos.remove('helio')

# 2. Convertendo e indexando dados em Dicionário dinamicamente
alunos_dict = {} 
for aluno in alunos:
    alunos_dict['12345' + str(alunos.index(aluno))] = aluno

# 3. Testando buscas controladas
print(alunos_dict['123450'])
print(alunos_dict.get('123455', 'Aluno não encontrado'))
```
### Exercício 3: Impressão Controlada de Intervalos Pares
```python
numero_1 = int(input("Digite um número do Intervalo Inicial: "))
numero_2 = int(input("Digite um número do Intervalo Final: "))

for i in range(numero_1, numero_2 + 1):
    if i % 2 == 0:
        print(i, end=' ')
```
### Exercício 4: Instanciação Básica de Objeto (Classe Carro)
```python
class Carro:
    def __init__(self, modelo, marca, ano, placa):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.placa = placa

    def mostrar_placa(self):
        print(f'A placa do carro é: {self.placa}')

carro1 = Carro('Civic', 'Honda', 2020, 'ABC-1234')
carro1.mostrar_placa()
```
## 16. 📚 Recomendações de Conteúdo

- **Livro**: "*Introdução à Programação com Python*" – Nilo Ney Coutinho Menezes.

- **Podcast**: Python_Podcast_br – Discussões sobre a linguagem e ecossistema de desenvolvimento.

- **Filme**: Moneyball (O Homem que Mudou o Jogo) – Como a análise de dados estatísticos transformou o beisebol.

- **Documentário**: A Era dos Dados (Netflix) – Explora o impacto global da IA e processamento de informações.

- **Plataforma Web**: W3Schools – Excelente guia prático de referência sintática.





