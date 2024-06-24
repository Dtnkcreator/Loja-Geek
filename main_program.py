from produto import Produto
from loja import Loja

def main():
    loja = Loja()
    usuario_logado = None

     # Adicionando produtos à loja
    produto1 = Produto("camisa", 29.99, 50)
    produto2 = Produto("oculos", 79.90, 30)
    produto3 = Produto("meia", 119.99, 20)

    loja.adicionar_produto(produto1)
    loja.adicionar_produto(produto2)
    loja.adicionar_produto(produto3)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Lista de Produtos")
        print("4 - Adicionar Produto ao Carrinho")
        print("5 - Remover Produto do Carrinho")
        print("6 - Ver Carrinho")
        print("7 - Finalizar Compra")
        print("8 - Sair")
        
        opcao = input("Opção: ").strip()

        if opcao == '1':
            nome_usuario = input("Digite o nome de usuário: ").strip()
            senha = input("Digite a senha: ").strip()
            loja.cadastrar_usuario(nome_usuario, senha)
        
        elif opcao == '2':
            nome_usuario = input("Digite o nome de usuário: ").strip()
            senha = input("Digite a senha: ").strip()
            usuario_logado = loja.fazer_login(nome_usuario, senha)
            if usuario_logado:
                print(f"Bem-vindo, {nome_usuario}!")
            else:
                print("Login ou senha incorretos.")
        
        elif opcao == '3':
            loja.listar_produtos()
        
        elif opcao == '4':
            if usuario_logado:
                nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ").strip()
                produto = loja.buscar_produto(nome_produto)
                if produto:
                    quantidade = int(input("Digite a quantidade desejada: "))
                    usuario_logado.adicionar_ao_carrinho(produto, quantidade)
                    print(f"{quantidade} unidades de {nome_produto} adicionadas ao carrinho.")
                else:
                    print("Produto não encontrado.")
            else:
                print("Faça login primeiro.")
        
        elif opcao == '5':
            if usuario_logado:
                nome_produto = input("Digite o nome do produto que deseja remover do carrinho: ").strip()
                produto = loja.buscar_produto(nome_produto)
                if produto:
                    usuario_logado.remover_do_carrinho(produto)
                    print(f"{nome_produto} removido do carrinho.")
                else:
                    print("Produto não encontrado no carrinho.")
            else:
                print("Faça login primeiro.")
        
        elif opcao == '6':
            if usuario_logado:
                print("Carrinho de compras:")
                for produto, quantidade in usuario_logado.carrinho:
                    print(f"{produto.nome}: {quantidade} unidades")
                total_carrinho = usuario_logado.calcular_total_carrinho()
                print(f"Total a pagar: R${total_carrinho:.2f}")
            else:
                print("Faça login primeiro.")
        
        elif opcao == '7':
            if usuario_logado:
                loja.processar_pagamento(usuario_logado)
            else:
                print("Faça login primeiro.")
        
        elif opcao == '8':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

