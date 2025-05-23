agenda = {}

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    agenda[nome.lower()] = {"nome": nome, "telefone": telefone, "email": email}
    print(f"contato {nome} adicionado com sucesso!")

inserir_contato()