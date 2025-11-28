#função para criar linha
def mostrar_linha():
    l = 128 * "_"
    lformatado = l[:80]
    print(lformatado)

#funcao para criar titulo
def mostrar_titulo(titulo):
    t = f"{30 * "="} {titulo} {30 * "="}"
    tformatado = t[:80]
    print(tformatado)

#função para mostrar menú
def menu():
    m = f"{30 * "="} {"ESCOLHA QUAL OPERÇÃO VOCÊ DESEJA APLICAR:"} {30 * "="}"
    mformatado = m[:80]
    print(mformatado)
    print()
    print(f"{30 * " "}1 - VENDER\n{30 * " "}2 - COMPRAR\n{30 * " "}3 - ALUGAR\n{30 * " "}0 - SAIR\n")

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



def marcas(texto):
    mostrar_titulo(texto)
    i = 1 #Contador para colocar numeração nas marcas
    for k in fipe.keys():
        print(f"{" " * 30}{i} - {k}")
        i += 1
    print(f"{" " * 30}0 - Sair")
    
carros = [
    {# Chevrolet
        'Marca' : "Chevrolet",
        'Modelo' : 'Onix',
        'Ano' : 2022
    }, 
    {
        'Marca' : "Chevrolet",
        'Modelo' : 'Onix',
        'Ano' : 2023
    },
    {
        'Marca' : "Chevrolet",
        'Modelo' : 'S10',
        'Ano' : 2024
    },
    {
        'Marca' : "Chevrolet",
        'Modelo' : 'Cruze',
        'Ano' : 2022
    },
    {
        'Marca' : "Chevrolet",
        'Modelo' : 'Spin',
        'Ano' : 2023
    },
    {
        'Marca' : "Chevrolet",
        'Modelo' : 'Montana',
        'Ano' : 2024
    },
    {
        'Marca' : "Chevrolet",
        'Modelo' : 'Equinox',
        'Ano' : 2023
    },
    # Volksvagen
    {
        'Marca' : "Volksvagen",
        'Modelo' : 'Gol',
        'Ano' : 2022
    },
    {
        'Marca' : "Volksvagen",
        'Modelo' : 'Voyage',
        'Ano' : 2021
    },
    {
        'Marca' : "Volksvagen",
        'Modelo' : 'Nivus',
        'Ano' : 2023
    },
    {
        'Marca' : "Volksvagen",
        'Modelo' : 'Polo',
        'Ano' : 2024
    },
    {
        'Marca' : "Volksvagen",
        'Modelo' : 'T-Cross',
        'Ano' : 2023
    },
    {
        'Marca' : "Volksvagen",
        'Modelo' : 'Amarok',
        'Ano' : 2024
    },
    # Hyundai
    {
        'Marca' : "Hyundai",
        'Modelo' : 'HB20',
        'Ano' : 2023
    },
    {
        'Marca' : "Hyundai",
        'Modelo' : 'Creta',
        'Ano' : 2024
    },
    {
        'Marca' : "Hyundai",
        'Modelo' : 'Tucson',
        'Ano' : 2022
    },
    {
        'Marca' : "Hyundai",
        'Modelo' : 'Azera',
        'Ano' : 2021
    },
    {
        'Marca' : "Hyundai",
        'Modelo' : 'Santa Fe',
        'Ano' : 2023
    }
        ]

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
    }
        ]

# Dicionario vazio criado para guardar temporariamente o cadastro do cliente
cadastro = {

}

mostrar_titulo("CADASTRO DE CLIENTES")

#Codigo criado para adicionar as chaves e valores no dicionario cadastro = {}
'''while True:
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
        print()'''


#Lista para guardar os dicionarios dos carros contendo: marca, modelo e km
mostrar_linha()        

mostrar_linha()

while True:
    #Codigo para escolher o tipo de transação
    mostrar_titulo(" MENÚ DE TRANSAÇÃO ")
    menu()
    mostrar_linha()
    menu1 = int(input("Escolha uma das opções acima: "))
    print()
    match menu1:
        case 1:
            ''' Venda de Veículos (Cliente → Empresa)
            • O cliente informa marca e modelo do veículo.
            • O sistema consulta o valor FIPE (armazenado em um dicionário).
            • A proposta da empresa deve ser o valor FIPE com 12% de desconto.
            • Se o cliente aceitar, o valor é adicionado ao saldo e o veículo entra na lista da empresa'''
            marcas("ESCOLHA UMA DAS OPPÇÕES ACEITAS")
            while True:
                while True:
                    marca_cliente = input(f"Informe qual é a marca do veiculo a ser vendido: ").capitalize()
                    if marca_cliente == 1:
                        marca = 0
                        break
                    elif marca_cliente == 2:
                        marca = 1
                        break
                    elif marca_cliente == 3:
                        marca = 2
                        break
                    else:
                        print("Opção invalida!")
                    
                    
                modelo_cliente = input(f"Informe o modelo do veiculo a ser negociado: ").capitalize()
                ano = input("Informe o ano do veiculo a ser vendido: [AAAA]")
                    while True:
                        if ano.isdigit() and len(ano) == 4:
                            break
                        else:
                                print("Formato de ano não aceito, tente novamente!")
                    else:
                        print("Não trabalhamos com essa marca\n")
                        escolha = input(f"O que deseja fazer:\n{" " * 20}1 - Continuar a compra sem o veiculo na troca\n{" " * 20}2 - finalizar sessão")
                        if escolha == 1:
                            print("Continuando...")
                            break
                        else:
                            print()
                
                break
    
        case _:
            print("Opcão invalida, tente novamente!")
    break

#Codigo para mostrar os modelos disponiveis para compra
#Código para mostrar os modelos disponivies para aluguel 
#Codigo para mostrar o valor pelo qual será recebido o veiculo usado na troca ou na venda.'''
