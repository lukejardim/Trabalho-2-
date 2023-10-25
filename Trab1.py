# Cria um vetor vazio para armazenar informações dos usuários
usuarios = {}

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

    # Armazena as infos do usuário criado 
    usuario_info = {
        "Nome": nomeusuario,
        "Hierarquia": hierarquia,
        "Senha": senha
    }

    # Aramazena os usuários e utiliza o nomeusuario como referência
    usuarios[nomeusuario] = usuario_info

    print("\nUsuário registrado com sucesso!")

def login():
    nomeusuario = input("Nome: ")
    senha = input("Senha: ")

    if nomeusuario in usuarios and usuarios[nomeusuario]["Senha"] == senha:
        posto = {usuarios[nomeusuario]['Hierarquia']}
        if posto == {'1'}:
            hierarquia = "Adm"
        elif posto == '2':
            hierarquia = "Moderador"
        else:
            hierarquia = "User"
        print(f"\nBem-vindo, {nomeusuario}! Você é um {hierarquia}.")
    else:
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
            for usuario, info in usuarios.items():
                print(f"Nome: {info['Nome']}")
            break
        else:
            print("\nOpção inválida. Escolha 1 para registrar, 2 para entrar ou 3 para sair.")

if __name__ == "__main__":
    main()