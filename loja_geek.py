        
def loja_geek():
    print("Categorias:\n")
    print("1 - Art figures")
    print("2 - Livros e Mangás")
    print("3 - Músicas")
    print("4 - Decorações\n")
    categoria = int(input("Qual das Categorias gostaria de acessar? "))
    match categoria:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print("A opção escolhida não está válida, tente novamente!")
            loja_geek()