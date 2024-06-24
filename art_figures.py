def figures():
    carrinho = {}
    print("1...Super Mario")
    print("2...Batman")
    print("3...Superman")
    print("4...Retornar para tela inicial")
    figures_pergunta = int(input("Qual opção gostaria de acessar? "))
    match figures_pergunta:
        case 1:
            print("\nInformações de Super Mario:\nPreço: R$50.00 \nTamanho: 50cm")
            pergunta_compra = input("Gostaria de comprá-lo? (1. Sim 2. Não) ")
            match pergunta_compra:
                    case 1:
                        adicionar_carrinho("supermario", carrinho)
                        print(carrinho)
        case 2:
            print("\nInformações de Batman:\nPreço: R$65.00 \nTamanho: 40cm")
        case 3:
            print("\nInformações de Superman:\nPreço: R$80.00 \nTamanho: 40cm")
        case 4:
            print("Retornando para o menu...")
            pass
        case _:
            print("Algo deu errado, tente novamente.")
            figures()

def adicionar_carrinho(produto, carrinho):
    if produto in carrinho:
        print(f"O produto {produto} já foi comprado.")
    else:
        print(f"O produto {produto} foi comprado!.")