from art_figures import figures
def loja_geek():
    while True:    
        print("Categorias:\n")
        print("1....Art Figures")
        print("2....Livros e Mangás")
        print("3....Músicas")
        print("4....Decorações")
        print("5....Sair\n")
        try:    
            categoria = input("Qual das Categorias gostaria de acessar? ")
            match categoria:
                case 1:
                        print("Você abriu a Categoria de Art Figures.")
                        figures()
                case 2:
                        print("Você abriu a Categoria de Livros e Mangás.")
                        break
                case 3:
                        print("Você abriu a Categoria de Músicas.")
                        break
                case 4:
                        print("Você abriu a Categoria de Decorações.")
                        break
                case 5:
                        print("\nSaindo...")
                        break
        except:
              print("Algo deu errado!")
              break
