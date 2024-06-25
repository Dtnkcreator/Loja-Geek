class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}")