from banco import db_cria_usuario, db_loga_usuario, db_imprime_usuario, db_altera_usuario, db_deleta_usuario
from menu import menu_altera_usuario

class Usuario:

  def __init__(self, nome, email, login, senha):
    self.nome = nome
    self.email = email
    self.login = login
    self.senha = senha
    
  def cria_usuario(self):
    return db_cria_usuario(self.nome, self.email, self.login, self.senha)

  def imprime_usuario(self):
    dados = db_imprime_usuario(self.login)
    print(f"Nome: {dados[1]}")
    print(f"Email: {dados[2]}")
    print(f"Login: {dados[3]}")
    print(f"Senha: {dados[4]}")
    
  def altera_usuario(self):
    coluna, novo_valor = menu_altera_usuario()
    return db_altera_usuario(self.login, coluna, novo_valor)

  def deleta_usuario(self):
    return db_deleta_usuario(self.login)
    
  def loga_usuario(self):
    return db_loga_usuario(self.login, self.senha)



  