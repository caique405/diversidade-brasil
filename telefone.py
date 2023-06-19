from banco import db_cria_telefone, db_imprime_telefone, db_altera_telefone, db_deleta_telefone


class Telefone:

  def __init__(self, id_usuario, telefone=None, id_telefone=None): 
      self.id_telefone = id_telefone
      self.id_usuario = id_usuario
      self.telefone = telefone


  def cria_telefone(self):
    return db_cria_telefone(self.id_usuario, self.telefone)

  def imprime_telefone(self):
    dados = db_imprime_telefone(self.id_usuario)
    contador = 1
    telefone_dict = {}

    for i in dados:
        print(f"Telefone {contador}: {i[2]}")
        telefone_dict[contador] = i[0]
        contador += 1

    return telefone_dict

  def altera_telefone(self, id_telefone, novo_valor):
    return db_altera_telefone(id_telefone, novo_valor)
    
  def deleta_telefone(self, id_telefone):  
    return db_deleta_telefone(id_telefone)
  