from cadastro_login import cadastrar_usuario
from cadastro_login import fazer_login
def main():
    database = {}

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(nome, senha, database)

        elif opcao == '2':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            fazer_login(nome, senha, database)
            break
        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()