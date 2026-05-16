# 📝 Fundamentos de Python: Tipagem e Interação

Este documento reúne os conceitos básicos de manipulação de variáveis, tipos de dados e entrada/saída de informações aprendidos em aula.

## 1. Verificação de Tipos e Variáveis

Em Python, podemos descobrir a natureza de qualquer dado utilizando funções integradas.

```python
teste = "teste"
# A função type() retorna o tipo de dado de uma variável.
# O valor da variável é exibido após a vírgula no print.
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

- Case Sensitive: Python diferencia letras maiúsculas de minúsculas (ex: Nome é diferente de nome).

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

- Sintaxe: Usa chaves ```{}``` e o formato ```chave: valor```.

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

Para projetos grandes, não colocamos tudo em um único arquivo. Organizamos o código para ser reutilizável.
### 9.1. Módulos

Um **Módulo** é apenas um arquivo ```.py``` contendo funções e variáveis.

- _Exemplos nativos_: ```math```, ```datetime```, ```random```.

### 9.2. Pacotes

Um **Pacote** é uma pasta que contém vários módulos. Para o Python entender que a pasta é um pacote, ela deve conter um arquivo (mesmo que vazio) chamado ```__init__.py```.

```python
import pandas as pd           # Importa o pacote com um apelido
from math import sqrt         # Importa apenas uma função específica
import meu_pacote.meu_modulo  # Importa de uma estrutura de pastas
```
## 10. 📝 Exercício de Fixação

Com base nos conceitos de Listas e Dicionários, realize as seguintes tarefas para organizar uma turma de alunos:

- **Tarefa 1**: Crie uma lista inicial de alunos e adicione um novo aluno que está ingressando nesta aula.

- **Tarefa 2**: Identifique um aluno que desistiu do curso e remova-o da lista de alunos ativos.

- **Tarefa 3**: Implemente uma busca utilizando um Dicionário (ex: Matrícula: Nome ou Nome: Nota), permitindo que um aluno específico seja localizado rapidamente pelo sistema através de sua chave.



- [📝 Fundamentos de Python: Tipagem e Interação](#-fundamentos-de-python-tipagem-e-interação)
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
    - [9.1. Módulos](#91-módulos)
    - [9.2. Pacotes](#92-pacotes)
  - [10. 📝 Exercício de Fixação](#10--exercício-de-fixação)

