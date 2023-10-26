class Usuario:
    def __init__(self, nome, hierarquia, senha):
        self.nome = nome
        self.hierarquia = hierarquia
        self.senha = senha

# Cria uma lista vazia para armazenar informações dos usuários
usuarios = []

# Função para criar usuários
def registrar_usuario():
    print("\nRegistre um novo usuário:")
    nomeusuario = input("Nome: ")
    hierarquia = input("Hierarquia (1-Adm, 2-Moderador, 3-User): ")
    senha = input("Senha: ")

    if not nomeusuario.isalnum():
        print("\nNome de usuário só deve conter letras e números!")
        return

    if hierarquia not in ("1", "2", "3"):
        print("\nHierarquia inválida! Deve ser 1, 2 ou 3.")
        return

    # Cria um objeto de usuário e o adiciona à lista
    usuario = Usuario(nomeusuario, hierarquia, senha)
    usuarios.append(usuario)

    print("\nUsuário registrado com sucesso!")

def login():
    nomeusuario = input("Nome: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.nome == nomeusuario and usuario.senha == senha:
            if usuario.hierarquia == "1":
                hierarquia = "Adm"
            elif usuario.hierarquia == "2":
                hierarquia = "Moderador"
            else:
                hierarquia = "User"
            print(f"\nBem-vindo, {nomeusuario}! Você é um {hierarquia}.")
            return

    print("\nNome de usuário ou senha incorretos.")

def main():
    while True:
        opcao = input("\nEscolha uma opção (1-Registrar, 2-Entrar, 3-Sair): ")
        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("\nVocê saiu do programa.")
            print("Usuários registrados:")
            for usuario in usuarios:
                print(f"Nome: {usuario.nome}")
            break
        else:
            print("\nOpção inválida. Escolha 1 para registrar, 2 para entrar ou 3 para sair.")

if __name__ == "__main__":
    main()