from loja_geek import loja_geek

def cadastrar_usuario(nome, senha, database):

    if nome in database:
        print(f"Usuário '{nome}' já existe. Escolha outro nome de usuário.")
    else:
        database[nome] = senha
        print(f"Usuário '{nome}' cadastrado com sucesso.")



def fazer_login(nome, senha, database):

    if nome in database and database[nome] == senha:
        print(f"Login bem-sucedido. Bem-vindo, {nome}!")
        loja_geek()
    else:
        print("Nome de usuário ou senha incorretos.")


