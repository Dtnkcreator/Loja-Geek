from cadastro_login import cadastrar_usuario,fazer_login
import sys
sys.path.append("C:/Users/182400219/Documents/Projetos python/Loja-Geek/loja/")
from loja import Loja

def main():
    database = {}
    Loja().entra()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Entrar Na Loja")
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(nome, senha, database)

        elif opcao == '2':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            fazer_login(nome, senha, database)

        elif opcao == '3':
            print("Entrando na Loja !!")
            
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

