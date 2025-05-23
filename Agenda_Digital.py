# Método para buscar um contato na agenda
def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ").lower()
    if nome in agenda:
        contato = agenda[nome]
        print(f"\nNome: {contato['nome']}")
        print(f"\nTelefone: {contato['telefone']}")
        print(f"\nE-mail: {contato['email']}\n")
    else:
        print("Contato não encontrado.\n")

# Criação do menu principal da agenda
def menu():
    while True:
        print("Agenda Digital")
        print("1. Inserir Contato")
        print("2. Buscar Contato")
        print("3. Deletar Contato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_contato()
        elif opcao == "2":
            buscar_contato()
        elif opcao == "3":
            deletar_contato()
        elif opcao == "4":
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu principal
menu()