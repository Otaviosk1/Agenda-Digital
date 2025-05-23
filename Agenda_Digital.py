agenda = {}

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    agenda[nome.lower()] = {"nome": nome, "telefone": telefone, "email": email}
    print(f"contato {nome} adicionado com sucesso!")

inserir_contato()

#Função deletar
def deletar_contato(self, nome):
    if nome.lower() in self.contatos:
        del self.contatos[nome.lower()]
        self.salvar_contatos()
        print(f"Contato {nome} deletado con sucesso.\n")
    else:
        print(f"Contato não encontrado.\n")