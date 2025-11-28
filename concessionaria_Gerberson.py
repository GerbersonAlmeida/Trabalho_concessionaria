#função para criar linha
def mostrar_linha():
    print(128 * "_")

#funcao para criar titulo
def mostrar_titulo(titulo):
    print(f" {30 * "="} {titulo} {30 * "="}")

#função para mostrar menú
def menu():
    print(f"{30 * "="} {"ESCOLHA QUAL OPERÇÃO VOCÊ DESEJA APLICAR:"} {30 * "="}\n")
    print(f"{30 * " "}1 - COMPRAR\n{30 * " "}2 - VENDER\n{30 * " "}3 - ALUGAR\n{30 * " "}0 - SAIR\n")

#Função usada para que o usuario nao digite seus dados errados
def cadastro_cliente():
    while True:
        cadastro['Nome'] = input("Digite o nome do cliente: ").title().strip()
        while True:
            telefone = input("Número para contato com DDD e 9 digitos: ").strip()
            print() #print vazio sendo utilizado apenas para pular linha
            
            if telefone.isdigit() and len(telefone) == 11: #if utilizado para conferir se se trata de apenas números para ser valido como telefone
                break                                                   #Um len() foi utilizado para ver se o número digitado se tem a quantidade correta de números
            elif telefone.isdigit() and len(telefone) != 11:
                print("O número de telefone digitado parece estar faltando digitos, \ninforme o número de elefone com DDD")
                print()
            else:
                print("O valor digitado não é um número de telefone, informe o número de telefone")
                print()
        while True:    
            saldo = input("Informe o saldo disponivel para negociar R$: ")
            if saldo.isdigit():
                saldo = float(saldo) #Transformando o valor string em float
                break
            else:
                print("\nValor digitado não parece ser um saldo,\npor favor digite o saldo disponivel para continuarmos!")
                print()
        cadastro['Saldo'] = saldo
        cadastro['Telefone'] = telefone
        
        break

def marcas():
    mostrar_titulo("MARCAS DISPONIVEIS")

    for marca in fipe.keys():
        print("")


    
carros = [{
          'id' :'001',# id 001 serão carros a venda 
          'Marca' : "Chevrolet",
          'Modelo' : 'Onix',
          'Ano' : '2022'
        }, 
        {
          'id': '001',
          'Marca' : "Chevrolet",
          'Modelo' : 'Onix',
          'Ano' : 2023
        }]

fipe = [
    {
        'Chevrolet' : [
            {'Onix': 69677},
            {'Tracker': 119000},
            {'S10': 239500},
            {'Cruze': 155000},
            {'Spin': 105000},
            {'Montana': 134490},
            {'Equinox': 189990}
        ],
        'Volksvagen' : [
            {'Gol': 58990},
            {'Voyage': 75590},
            {'Nivus': 105190},
            {'Polo': 85290},
            {'T-Cross': 125000},
            {'Amarok': 295000}
        ],
        'Hyundai' : [
            {'HB20': 72340},
            {'Creta': 135990},
            {'Tucson': 199990},
            {'Azera': 225000},
            {'Santa Fe': 310000}                  
        ]
    },
]
print(fipe)
# Dicionario vazio criado para guardar temporariamente o cadastro do cliente
cadastro = {

}

mostrar_titulo("CADASTRO DE CLIENTES")

#Codigo criado para adicionar as chaves e valores no dicionario cadastro = {}
while True:
    cadastro_cliente()
    #estrutura de repetição criada para mostrar os dados cadastrado
    mostrar_titulo("REVISÃO DE DADOS DO CLIENTE")
    print(f"\n{30 * " "}Nome = {cadastro['Nome']}")
    print(f"{30 * " "}Telefone = {cadastro['Telefone']}")
    print(f"{30 * " "}Saldo = R${cadastro['Saldo']:.2f}\n")
    decisao = input("Os dados informados estâo corretos: [S/N] ").capitalize()
    if decisao == "S":
        mostrar_linha()
        print(" " * 30, "DADOS CADASTRADOS COM SUCESSO!!\n")

            #Mostrando os dados finais do cliente
        print(f"{30 * " "}Nome = {cadastro['Nome']}")
        print(f"{30 * " "}Telefone = {cadastro['Telefone']}")
        print(f"{30 * " "}Saldo = R${cadastro['Saldo']:.2f}")
        break
        #Se incorreto os dados esse else vai deletar os dados guardados no dicionario cadastro
    elif decisao == "N":
        print("Digite novamente os dados do cliente!")
        del cadastro["Nome"]
        del cadastro["Saldo"]
        del cadastro["Telefone"]
        mostrar_linha()
    
    else:
        print("\nOpção invalida, por favor digite apenas [S ou N]!")
        mostrar_linha()
        print()


#Lista para guardar os dicionarios dos carros contendo: marca, modelo e km
mostrar_linha()        

mostrar_linha()
#Codigo para escolher o tipo de transação
mostrar_titulo(" MENÚ DE TRANSAÇÃO ")
print("\n\n1 - Comprar\n 2 - Vender\n 3 - alugar\n 0 - cancelar\n\n")
mostrar_linha()
menu1 = int(input("Escolha uma das opções acima: "))
while True:
    menu()
    match menu1:
        case 1:
            ''' Venda de Veículos (Cliente → Empresa)
            • O cliente informa marca e modelo do veículo.
            • O sistema consulta o valor FIPE (armazenado em um dicionário).
            • A proposta da empresa deve ser o valor FIPE com 12% de desconto.
            • Se o cliente aceitar, o valor é adicionado ao saldo e o veículo entra na lista da empresa'''
            while True:
                while True:
                    marca_cliente = input(f"Informe qual é a marca do veiculo a ser vendido: ").captalize()
                    if marca_cliente in fipe.values():
                        print("ENCONTRADO")
                    break
                break
''' case 2:
            while True:

        case 3:

        case 0:

        case _:


#Codigo para mostrar os modelos disponiveis para compra
#Código para mostrar os modelos disponivies para aluguel 
#Codigo para mostrar o valor pelo qual será recebido o veiculo usado na troca ou na venda.'''
