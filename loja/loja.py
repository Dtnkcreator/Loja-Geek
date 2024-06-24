class Loja:

    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def listar_produtos(self):
        print("Produtos disponíveis:")
        for produto in self.produtos:
            produto.exibir()
    
    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None
    def entra(self):
        print("entrou na loja")
    
    def vender_produto(self, nome, quantidade):
        produto = self.buscar_produto(nome)
        if produto:
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                print(f"{quantidade} unidades de {nome} vendidas.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

