agenda = {}

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    agenda[nome.lower()] = {"nome": nome, "telefone": telefone, "email": email}
    print(f"contato {nome} adicionado com sucesso!")

#Função deletar
def deletar_contato(self, nome):
    if nome.lower() in self.contatos:
        del self.contatos[nome.lower()]
        self.salvar_contatos()
        print(f"Contato {nome} deletado con sucesso.\n")
    else:
        print(f"Contato não encontrado.\n")
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

