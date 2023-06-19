from banco import db_cria_doacao, db_imprime_doacao, db_imprime_ongs
import time


class Doacao:

  def __init__(self,
               id_usuario,
               id_ong=None,
               valor=None,
               data=None,
               forma_pagamento=None):
    self.id_usuario = id_usuario
    self.id_ong = id_ong
    self.valor = valor
    self.data = data
    self.forma_pagamento = forma_pagamento

  def cria_doacao(self):
    return db_cria_doacao(self.id_usuario, self.id_ong, self.valor, self.data, self.forma_pagamento)

  

  def imprime_doacao(self):
    dict_ongs = {}
    dados_ongs = db_imprime_ongs()

    for i in dados_ongs:
      dict_ongs[i[0]] = i[1]
    

    time.sleep(0.1)
    dados = db_imprime_doacao(self.id_usuario)

    print("LISTA DE DOACÕES")
    for i in dados:
      print('-' * 60)
      print(f"ONG: {dict_ongs[i[2]]}")
      print(f"Valor: {i[3]}")
      print(f"Data: {i[4]}")
      print(f"Forma de pagamento : {i[5]}")