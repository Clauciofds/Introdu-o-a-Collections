# O CÓDIGO ABAIXO FOI ESCRITO EM UM IDE E NÃO O GOOGLE COLAB
import numpy as numpy

# Documentação relevante: https://docs.python.org/pt-br/3/tutorial/datastructures.html

# Criando um lista
idades = [45, 30, 55, 34]

print('linha 5:', idades)

print('') # imprimindo os elementos da lista um a um
for idade in idades:
    print('linha 10:', idade)

print('') # inserindo um elemento no fim da lista
idades.append(15)
print('linha 14:', idades)

print('') # acessano uma posição especifica de um elemento
print('linha 18:', idades[3])

print('') # removendo um elemento da lista
idades.remove(30)
print('linha 21:', idades)

print('') # check se elemento pertence a lista
print('linha 25:', 29 in idades)

print('') # inserindo um elemento em um posição especifica
idades.insert(0, 20)
print('linha 28:', idades)

print('') # verifincando se o elemento 15 pertence a lista
if 15 in idades:
    idades.remove(15)
    print('linha 32:', idades)

print('') # nesta linha tenandomos inserir vários elementos na lista, mas o que o código
# realmente faz desta forma e inserir uma nova lista dentro de lista
# origianal
idades.append([18, 44])
print('linha 37:', idades)

print('') # imprimindo a lista acima passando por todos os elementos
for elementos in idades:
    print('linha 43: Recebi o elemento', elementos)

print('') # check do tipo de elementos na lista
print('linha 47:', type(idades))

# reescrendo a lista
idades = [45, 30, 55, 34]

print('') # agora sim vamos inserir os vários elementos na lista extendendo o tamanho da mesma
idades.extend([18, 44])
print('linha 53:', idades)

print('') # somando um ano a cada elemento da lista
idades_no_proximo_ano = []
for elementos in idades:
    idades_no_proximo_ano.append(elementos+1)
print('linha 57:', idades_no_proximo_ano)

print('') # mesmo processo anterior de uma forma sintetizada e performática
idades_no_proximo_ano = [elementos+1 for elementos in idades]
print('linha 63:', idades_no_proximo_ano)

print('') # filtrando os elementos
idades_maior_35 = [elementos for elementos in idades if elementos > 35]
print('linha 67:', idades_maior_35)

print('') # o mesmo código anterior, mas definimos um função para acresentar
          # 1 anos a idade de todos
def proximo_ano(elementos):
    return elementos+1

idades_maior_35 = [proximo_ano(elementos) for elementos in idades if elementos > 35]
print('linha 71:', idades_maior_35)

print('') # esse parte do código fica melhor explicado no link:
          # https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52938
def faz_processamento_de_visualizacao(lista):
    print('linha 79: Tamanho da lista>', len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
print(idades)

print('') # nessa etapa demostrando a volatividades dos objetos mutáveis.
def faz_processamento_de_visualizacao(lista = []):
    print('linha 89: Tamanho da lista>', len(lista))
    lista.append(13)
    # print(lista)
print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())

print('') # Então, não é recomendável colocar uma lista como parâmetro default, e, sim,
          # None e verificar se é None, mas isso também se estende para outros objetos que
          # você pode usar como parâmetro de valor opcional, que é mutável. Portanto, 
          # é sempre bom ter esse cuidado, listas e objetos que são mutáveis.
          
          # NO LINK VOCÊ PODE ENTERDER MELHOR TODA LÓGICA DOS OBJETOS MUTÁVEIS:
          # https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52938
def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
        # print(lista)
    print('linha 98: Tamanho da lista>', len(lista))
    lista.append(13)

print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())

print('') # <<< OBJETOS PRÓPRIOS >>>

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self.codigo, self.saldo)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
print('linha 116:', conta_do_gui)

print('')
conta_da_Dani = ContaCorrente(45666)
conta_da_Dani.deposita(1000)
print('linha 133:', conta_da_Dani)

print('') # Criando um lista com os objetos contas (objeto mutável)
contas = [conta_da_Dani, conta_do_gui]
print('linha 138:', contas)

print('') # imprimindo cada elemento da lista.
for conta in contas:
    print('linha 142:', conta)

print('') # incluindo um elemento duplicado na lista
contas = [conta_da_Dani, conta_do_gui, conta_da_Dani]
print('linha 146:', contas[0])

print('') # realizando um depósito
conta_da_Dani.deposita(100)
print('linha 149:', contas[0])

print('') # imprimindo conta da Dani
print('linha 154:', conta_da_Dani)

print('') # imprimindo chamando o elemento da lista na posição 2
print('linha 157:', contas[2])

# Então a maneira de interpretarmos deve ser sempre: ao colocarmos objetos numa lista,
# não devemos instanciar esses objetos. Assim como passar parâmetros para métodos, não
# instância objetos. Só instanciamos um objeto novo de verdade quando chamamos o "construção"
# dele, a "instanciação". Quando construimos com ContaCorrente(), então, criamos uma conta corrente.
# Resumindo devemos tomar extremo cuidado com criação de elemento em uma lista mutável. A forma como
# escrevemos o nosso código, estamos apanas criando referências a um elemento da lista.

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

print('') #
contas = [conta_do_gui, conta_da_Dani]
print('linha 172:', contas[0], contas[1])
deposita_para_todas(contas)
print('linha 172:', contas[0], contas[1])

# print('') # Atribuindo a lista o código da conta
# contas.insert(0, 76)
# print('linha 177:', contas[0], contas[1], contas[2])
#
# print('') # tentando depositar com a lista modificada
# deposita_para_todas(contas)
# print('linha 172:', contas[0], contas[1])

# para seguranção de criação de um lista não mutável e aconselhavel cria-se tuplas
conta_do_gui = (15, 1100)
conta_da_Dani = (31, 1500)

print('') # para alteramos os valores de um tupla o correto é criarmos um função onde criamos
          # um novo saldo temporário e assim pode atribuir esse novo valor a conta
def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

# enta evocamos a nova função e atribuimos a conta um novo valor
conta_do_gui = deposita(conta_do_gui)
print('linha 189:', conta_do_gui)

guilherme = ('Guilherme', 37, 1983)
daniela = ('Daniela', 25, 1987)

print('') # criando lista com os elementos sendo tuplas
usuarios = [guilherme, daniela]
print('linha 200:', usuarios)

print('') # com isso podemos adiciona tuplas na nosse lista de usuários
usuarios.append(('Paulo', 34, 1985))
print('linha 207:', usuarios)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_Dani = ContaCorrente(2345)
conta_da_Dani.deposita(1000)

print('') # Agora possuimos dois objentos diferentes de tuplas
contas = (conta_do_gui, conta_da_Dani)
print(contas)

print('') # assim quando tentamos alterar um elemento, que nesse caso é um tupla não iremos
          # consigir, garantindo a imutabilidade do nosso objeto
# contas.append(3435)
# print(contas)

print('') # imprimindo nos lista de tuples
for conta in contas:
    print('linha 225:', conta)

# <<<HERANÇA E POLIMORFISMO>>>

from abc import ABCMeta, abstractmethod
class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self._codigo, self._saldo)

print('') # Criando um conta com as classes
print('linha 242:', Conta(88))

print('') # usanda o método de herança para manipular nossos elementos
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print('linha 245:', conta16)

print('') #
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(2500)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes() # duck tuping
    print('linha 260:', conta)

import array as arr

arr.array('d', [1, 3.5 ])

print('') # otimizando as funções de listagem com numpy
import numpy as np

numeros = np.array([1, 3.5])
print('linha 276:', numeros)

numeros += 3
print('linha 282:', numeros)

print('') # Neste caso estamos tentando criar uma nova instância, mas com uma impletação na classe
          # mãe tornando os métodos abstratos, isso forca o erro e a indetificação do mesmo.
          # Agora vou rodar o código, interpretou e vou tentar criar uma conta
          # normal. Já deu erro, porque a classe Conta virou uma classe abstrata. Ela tem um
          # método abstrato e não pode ser instanciada, porque ainda não implementaram todos
          # os métodos abstratos, o método passa_o_mês().
class ContaInvestimento(Conta):
    pass

ContaInvestimento(762)
print(ContaInvestimento)

print('') # Criando um nova classe para conta salário
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>>>Código {} - Saldo {}<<<]'.format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
print('linha 315:', conta1)

conta2 = ContaSalario(37)
print('linha 319:', conta2)

print('') # comparando contas Salário. Nesta comparação estamos verificando dois objetos distintos na
          # memória
print('linha 321: A conta1 é igual a conta2?', conta1 == conta2)

print('') # Criando um nova classe para conta salário, agora com a implementação da funçao de
          # comparações nos elementos específico nos objetos
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        return self._codigo == outro._codigo

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>>>Código {} - Saldo {}<<<]'.format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)
conta3 = ContaSalario(37)

print('linha 349:', conta1 == conta3)

print('linha 351:', conta1 == conta2)

print('linha 353:', isinstance(ContaCorrente(34), ContaCorrente))

print('linha 355:', isinstance(ContaCorrente(34), Conta))

print('linha 357:', conta2 in [conta1])

print('') # novas funcoes
idades = [15, 87, 65, 56, 32, 49, 37, 49]

for i in range(len(idades)): #lazy
    print('linha 362:', i, idades[i])

print('') # lazy
print('linha 366:', enumerate(idades))

print('') # 
print('linha 369:', type(range(len(idades))))

print('') # 
print(list(range(len(idades)))) # forcei a geração dos valores

print('') # 
print(list(enumerate(idades)))

print('') # 
for valor in enumerate(idades):
    print(valor)

print('') # unpacking da nossa tupla
for indice, idade in enumerate(idades):
    print(indice, 'x', idade)

print('') # 
usuarios = (
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Paulo', 39,1979)
)

for nome, idade, nascimento in usuarios:
    print(nome, '-- Idade:', idade)

print('') # ja desempacotando, ignorando o resto
for nome, _, _, in usuarios:
    print(nome)

print('') # 
print('linha 400:', sorted(idades))

print('') # 
print('linha 403:', sorted(idades, reverse=True))

print('') # 
print('linha 406:', reversed(idades))

print('') # 
print('linha 409:', idades)

print('') # 
print('linha 412:', list(reversed(idades)))

print('') # 
idades.sort()
print('linha 416:', idades)

print('') # 
print('linha 419:', list(reversed(sorted(idades))))

print('') # 
print('linha 422:', idades)

print('') # 