from art_figures import figures
def loja_geek():
    while True:
        print("Categorias:")
        print("1 - Art Figures")
        print("2 - Livros e Mangás")
        print("3 - Músicas")
        print("4 - Decorações\n")
        categoria = int(input("Qual das Categorias gostaria de acessar? "))
        match categoria:
            case 1:
                print("Você abriu a Categoria de Art Figures.")
                figures()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                print("A opção escolhida não está válida, tente novamente!")
                loja_geek()

loja_geek()

