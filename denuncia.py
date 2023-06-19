from banco import db_cria_denuncia, db_imprime_denuncia
from menu import menu_localizacao, menu_denuncia

class Denuncia:

  def __init__(self, id_usuario, id_categoria=None, estado=None, cidade=None, rua=None, cep=None, data=None):
    self.id_usuario = id_usuario
    self.id_categoria = id_categoria
    self.cep = cep 
    self.estado = estado
    self.cidade = cidade
    self.rua = rua
    self.data = data

  def cria_denuncia(self):
    return db_cria_denuncia(self.id_usuario, self.id_categoria, self.estado, self.cidade, self.rua, self.cep, self.data)

  def imprime_denuncia(self):
    dados = db_imprime_denuncia(self.id_usuario)

    for i in dados:
      print("-" * 60)
      print(f"Estado : {i[3]}")
      print(f"Cidade : {i[4]}")
      print(f"Rua : {i[5]}")
      print(f"CEP : {i[6]}")
      print(f"Data e hora : {i[7]}")