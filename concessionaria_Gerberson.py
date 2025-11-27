#função para criar linha
def mostrar_linha():
    print(128 * "_")

#funcao para criar titulo
def mostrar_titulo(titulo):
    print(f" {30 * "="} {titulo} {30 * "="}")

#função para mostrar menú
def menu():
    print(f" {30 * "="} {"ESCOLHA QUAL OPERÇÃO VOCÊ DESEJA APLICAR:\n"} {30 * "="}")
    print(f" {30 * " "} {"\n1 - COMPRAR\n2 - VENDER\n3 - ALUGAR\n 0 - SAIR\n"} {30 * "="}")

#Função usada para que o usuario nao digite seus dados errados
def cadastro_cliente():
    while True:
        cadastro['nome'] = input("Digite o nome do cliente: ").title().strip()
        while True:
            cadastro['Telefone'] = input("Número para contato com DDD e 9 digitos: ").strip()
            print() #print vazio sendo utilizado apenas para pular linha
            
            if cadastro['Telefone'].isdigit() and len(cadastro['Telefone']) == 11: #if utilizado para conferir se se trata de apenas números para ser valido como telefone
                break                                                   #Um len() foi utilizado para ver se o número digitado se tem a quantidade correta de números
            elif cadastro['Telefone'].isdigit() and len(cadastro['Telefone']) != 11:
                print("O número de telefone digitado parece estar faltando digitos, \ninforme o número de elefone com DDD")
                print()
            else:
                print("O valor digitado não é um número de telefone, informe o número de telefone")
                print()
        while True:    
            cadastro['saldo'] = input("Informe o saldo disponivel para negociar R$: ")
            if cadastro['saldo'].isdigit():
                saldo = cadastro['saldo']
                cadastro['saldo'] :  float(saldo)
                print(cadastro['saldo'])
                break
            else:
                print("Valor digitado não parece ser um saldo,\n por favor digite o saldo disponivel para continuarmos!")
                print()

        break

    
carros = [{
          'id' :'001',# id 001 serão carros a venda 
          'Marca' : "Chevrolet",
          'Modelo' : 'Onix',
          'ano' : '2022',
          'km' : 1000
        }, 
        {
          'id': '001',
          'Marca' : "Chevrolet",
          'Modelo' : 'Onix',
          'km' : 10000
        }]
# Dicionario vazio criado para guardar temporariamente o cadastro do cliente
cadastro = {

}

mostrar_titulo("CADASTRO DE CLIENTES")

#Codigo criado para adicionar as chaves e valores no dicionario cadastro = {}
while True:
    cadastro_cliente()
    #estrutura de repetição criada para mostrar os dados cadastrado
    
    for k, v in cadastro.items():
        print(f"{k} = {v}")
        decisao = input("Os dados informados estâo corretos: [S/N] ").capitalize()
        if decisao == "S":
            mostrar_linha()
            print(" " * 30, "DADOS CADASTRADOS COM SUCESSO!!\n")

            #Mostrando os dados finais do cliente
            for k, v in cadastro.items():
                print(f"{" " * 30} {k} = {v}")
            break
        #Se incorreto os dados esse else vai deletar os dados guardados no dicionario cadastro
        else:
            print("Digite novamente os dados do cliente!")
            del cadastro["Nome"]
            del cadastro["Saldo"]
            del cadastro["Telefone"]
            mostrar_linha()

    break
#Lista para guardar os dicionarios dos carros contendo: marca, modelo e km
        
'''
mostrar_linha()
#Codigo para escolher o tipo de transação
mostrar_titulo(" MENÚ DE TRANSAÇÃO ")
print("\n\n1 - Comprar\n 2 - Vender\n 3 - alugar\n 0 - cancelar\n\n")
mostrar_linha()
menu = int(input("Escolha uma das opções acima: "))
while True:
    menu()
    match menu:
        case 1:
            while True:
                
        case 2:
            while True:

        case 3:

        case 0:

        case _:


#Codigo para mostrar os modelos disponiveis para compra
#Código para mostrar os modelos disponivies para aluguel 
#Codigo para mostrar o valor pelo qual será recebido o veiculo usado na troca ou na venda. '''
