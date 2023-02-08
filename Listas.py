# O CÓDIGO ABAIXO FOI ESCRITO EM UM IDE E NÃO O GOOGLE COLAB

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