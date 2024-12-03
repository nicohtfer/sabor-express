import os

restaurantes = [{"nome" : "Sushinami", "categoria" : "Japonês", "ativo" : False}, 
                {"nome" : "PizzaHut", "categoria" : "Pizza", "ativo" : True}, 
                {"nome" : "Cantina Italiana", "categoria" : "Italiano", "ativo" : False}]

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar status do restaurante")
    print("4. Sair\n")
    
def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print("")

def voltando_ao_menu():
    input("\nAperte qualquer tecla para voltar ao menu principal")
    main()

def finalizando_programa():
    exibir_subtitulo("Encerrando o programa.")

def opcao_invalida():
    print("Opcão invalida!\n")
    voltando_ao_menu()

def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    cadastrando_restaurante = input("Digite o nome do restaurante que você deseja cadastrar: ")
    categoria_restaurante = input(f"\nDigite a categoria do restuarante {cadastrando_restaurante}: ")
    dados_restaurante = {"nome" : cadastrando_restaurante, "categoria": categoria_restaurante, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"\nO restaurante {cadastrando_restaurante} foi cadastrado com sucesso!")
    voltando_ao_menu()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltando_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encotnrado")
    
    voltando_ao_menu()

def selecionar_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizando_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    selecionar_opcao()

if __name__ == "__main__":
    main()