from produto import Produto
from usuario import Usuario
class Loja:
    def __init__(self):
        self.produtos = []
        self.usuarios_cadastrados = {}
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def listar_produtos(self:Produto):
        print("Produtos disponíveis:")
        for produto in self.produtos:
            produto.exibir()
    
    def cadastrar_usuario(self, nome_usuario, senha):
        if nome_usuario not in self.usuarios_cadastrados:
            self.usuarios_cadastrados[nome_usuario] = Usuario(nome_usuario, senha)
            print("Usuário cadastrado com sucesso.")
        else:
            print("Nome de usuário já existe. Tente outro nome.")
    
    def fazer_login(self, nome_usuario, senha):
        if nome_usuario in self.usuarios_cadastrados and self.usuarios_cadastrados[nome_usuario].senha == senha:
            return self.usuarios_cadastrados[nome_usuario]
        else:
            return None
        
    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None
    
    def processar_pagamento(self, usuario):
        total_a_pagar = usuario.calcular_total_carrinho()
        if total_a_pagar > 0:
            print(f"Total a pagar: R${total_a_pagar:.2f}")
            opcao = input("Confirmar pagamento (sim/nao)? ").strip().lower()
            if opcao == 'sim':
                usuario.limpar_carrinho()
                print("Pagamento realizado com sucesso.")
            else:
                print("Pagamento cancelado.")
        else:
            print("Carrinho vazio. Nada a pagar.")
