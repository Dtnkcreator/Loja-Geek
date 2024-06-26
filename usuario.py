class Usuario:
    def __init__(self, nome_usuario, senha):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.carrinho = []
    
    def adicionar_ao_carrinho(self, produto, quantidade):
        self.carrinho.append((produto, quantidade))
    
    def remover_do_carrinho(self, produto):
        novo_carrinho = []
        for p, q in self.carrinho:
            if p != produto:
                novo_carrinho.append((p, q))
        self.carrinho = novo_carrinho
        
    def limpar_carrinho(self):
        self.carrinho = []
    
    def calcular_total_carrinho(self):
        total = 0
        for produto, quantidade in self.carrinho:
            total += produto.preco * quantidade
        return total
