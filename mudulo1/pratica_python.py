#nome = input("Qual é o seu nome: ")
#idade = int(input("Qual é a sua idade: "))
#print(f"Olá {nome}, você terá {(2030 - (2026 - idade))} anos em 2030!")


#Exercicio: Então crie uma lista de alunos e realize as seguintes operações:
#1. Adicione um novo aluno que estão fazendo essa aula.
#2. Um dos alunos desistiu da aula, agora precisa remover ele da lista.
#3. Por fim, use o conceito de dicionário para que possa pesquisar um alunos em especifico nessa lista.

# alunos = ['ana', 'bruno', 'helio', 'aragao', 'jefferson']
# alunos.append('jorge')
# alunos.remove('helio')
# alunos_dict = {} 
# for aluno in alunos:
#     alunos_dict['12345' + str(alunos.index(aluno))] = aluno
#     print(alunos_dict)

# print(alunos_dict['123450'])
# print(alunos_dict['123453'])
# print(alunos_dict.get('123455', 'Aluno não encontrado'))


    



#Exercicio:
#1. Utilize o laço de repetição ´for' para contar ou iterar entre um intervalo de números e imprimir no terminal todos os números pares dentro desse intervalo de números.
#2. Escreva um programa que solicita ao usuário dois números: o início e o fim de um intervalo [inclusivos].
#3. O programa deve imprimir todos os números pares dentro desse intervalo.
# O resultado desse código, seria apresentar no terminal os números pares entre 1 e 10, que seriam: 2, 4, 6, 8 e 10. O programa deve ser capaz de lidar com qualquer intervalo de números fornecido pelo usuário, garantindo que apenas os números pares sejam exibidos no resultado.

#numero_1 = int(input("Digite um número do Intervalo Inicial: "))
#numero_2 = int(input("Digite um número do Intervalo Final: "))
#for i in range(numero_1, numero_2 + 1):
#    if i % 2 == 0:
#        print(i, end=' ')

#1. Crie uma classe chamada Carro;
#2. Defina seus atributos, devem conter: modelo, marca e ano;
#3. Em seguida, crie os seguintes métodos: mostrarplaca() e ao instaciar a classe a partir de um objeto, mostre a placa deste veiculo.

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