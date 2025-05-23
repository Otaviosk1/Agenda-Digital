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