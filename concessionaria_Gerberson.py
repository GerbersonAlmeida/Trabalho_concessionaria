#função para criar linha
def mostrar_linha():
    print(128 * "_")

#funcao para criar titulo
def mostrar_titulo(titulo):
    print(f" {30 * "="} {titulo} {30 * "="}")
    
    
# Dicionario vazio criado para guardar temporariamente o cadastro do cliente
cadastro = {

}

mostrar_titulo("CADASTRO DE CLIENTES")

#Codigo criado para adicionar as chaves e valores no dicionario cadastro = {}
while True:
    cadastro['nome'] = input("Digite o nome do cliente: ").title()
    cadastro['Telefone'] = input("Número para contato: ").num()
    cadastro['saldo'] = input("Informe o saldo disponivel para negociar: ")

    #estrutura de repetição criada para mostrar os dados cadastrado
    mostrar_titulo("CONFIRA O CADASTRO")
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
#Lista para guardar os dicionarios dos carros contendo: marca, modelo e km
carros = {
          'id' :'001',
          'Marca' : "Chevrolet",
          'Modelo' : 'Onix',
          'km' : 10000
        }, 
        {
          'id': '002',
          'Marca' : "Chevrolet",
          'Modelo' : 'Onix',
          'km' : 10000
        }

mostrar_linha()
#Codigo para escolher o tipo de transação
mostrar_titulo(" MENÚ DE TRANSAÇÃO ")
print("\n\n1 - Comprar\n 2 - Vender\n 3 - alugar\n 0 - cancelar\n\n")
mostrar_linha()
menu = int(input("Escolha uma das opções acima: "))
while True:
    match menu:
        case 1:
            while True:
                
        case 2:
        
        case 3:

        case 0:

        case _:


#Codigo para mostrar os modelos disponiveis para compra
#Código para mostrar os modelos disponivies para aluguel 
#Codigo para mostrar o valor pelo qual será recebido o veiculo usado na troca ou na venda. 
