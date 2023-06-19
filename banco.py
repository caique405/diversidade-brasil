import sqlite3
import time

banco = sqlite3.connect("app_denuncias.db")
cursor = banco.cursor()

#cursor.execute("CREATE TABLE usuarios (id_user INTEGER PRIMARY KEY, nome TEXT, email TEXT, login TEXT UNIQUE,  senha TEXT)")
#cursor.execute("CREATE TABLE categorias (id_categoria INTEGER PRIMARY KEY, tipo TEXT)")
#cursor.execute("CREATE TABLE denuncias (id_denuncia INTEGER PRIMARY KEY, id_usuario INTEGER, id_categoria INTEGER, estado TEXT, cidade TEXT, rua TEXT, cep TEXT, data TEXT)")
#cursor.execute("CREATE TABLE telefones (id_telefone INTEGER PRIMARY KEY, id_usuario INTEGER, telefone TEXT)")
#cursor.execute("Create TABLE ongs (id_ong INTEGER PRIMARY KEY, nome TEXT, email TEXT, missao TEXT)")
# cursor.execute()

#cursor.execute("CREATE TABLE doacao (id_doacao INTEGER PRIMARY KEY, id_usuario INTEGER, id_ong INTEGER,   valor DECIMAL, data TEXT, forma_pagamento TEXT)")

#   "INSERT INTO ongs (nome, email, missao) VALUES ('Salvar o Planeta','contato@salvaroplaneta.com', 'Combater as mudanças climáticas e promover a sustentabilidade'), ('Guardiões da Floresta', 'contato@guardioesdafloresta.org', 'Preservar as florestas tropicais e proteger a biodiversidade'), ('Mar Limpo', 'contato@marlimpo.org', 'Combater a poluição dos oceanos e preservar a vida marinha'), ('Cerrado Vivo', 'contato@cerradovivo.org', 'Proteger o Cerrado e promover o desenvolvimento sustentável da região'), ('Águas Limpas', 'contato@aguaslimpas.org', 'Preservar os recursos hídricos e garantir o acesso à água potável'),('Floresta Viva', 'contato@florestaviva.org', 'Promover a conservação das florestas e a conscientização sobre sua importância'),('Biodiversidade em Foco', 'contato@biodiversidadeemfoco.org', 'Preservar a biodiversidade e os ecossistemas frágeis'), ('Resgate Animal', 'contato@resgateanimal.org', 'Proteger e reabilitar animais em situação de risco ou maus-tratos'), ('Resgate Animal', 'contato@resgateanimal.org', 'Proteger e reabilitar animais em situação de risco ou maus-tratos')")
# banco.commit()

#cursor.execute("INSERT INTO categorias (id_categoria, tipo) VALUES (1, 'Queimadas'), (2, 'Poluição do ar'), (3, 'Poluição da água'), (4, 'Desmatamento')")
#banco.commit()


#create - Insere no banco (id, nome, email, login e senha)
def db_cria_usuario(nome, email, login, senha):
  try:

    cursor.execute(
      f"INSERT INTO usuarios (nome, email, login, senha) VALUES ('{nome}', '{email}', '{login}', '{senha}')"
    )

    print("\033[32mUsuário inserido com sucesso!\033[m")
    banco.commit()
    time.sleep(1)

  except sqlite3.IntegrityError:

    print(
      "\033[31mUsuário já existe. Não foi possível realizar a inserção.\033[m")
    banco.rollback()
    time.sleep(1)


#read - Retorna uma tupla com todos os dados do cliente (id, nome, emaail, login e senha)
def db_imprime_usuario(login):
  try:
    dados = cursor.execute(
      f"SELECT * FROM usuarios WHERE usuarios.login = '{login}'")
    for i in dados:
      return i
    print("\033[31mO login não foi encontrado no banco de dados.\033[m")
    time.sleep(1)
    return [None, None, None]
  except Exception as e:
    print("\033[31mOcorreu um erro ao acessar o banco de dados:\033[m", str(e))
    time.sleep(1)
    return [None, None, None]


def db_altera_usuario(login, coluna, novo_valor):
  try:
    cursor.execute(
      f"UPDATE usuarios set {coluna} = '{novo_valor}' where login = '{login}'")

    print(f"{coluna.capitalize()} alterado(a) para {novo_valor}.")
    banco.commit()
    time.sleep(1)

  except sqlite3.IntegrityError:

    print(
      "\033[31mLogin já existe. Não foi possível realizar a alteração.\033[m")
    banco.rollback()
    time.sleep(1)


def db_loga_usuario(login, senha):
  if login == "anonimo":
    return
  cursor.execute(
    f"SELECT login, senha FROM usuarios where usuarios.login = '{login}' AND usuarios.senha = '{senha}'"
  )
  result = cursor.fetchall()
  try:
    if result == []:
      return 0

    elif login in result[0] and senha in result[0]:
      return 1

  except:
    print("\033[31mNão foi possivel executar a opeação!\033[m")
    time.sleep(1)


def db_deleta_usuario(login):
  try:
    cursor.execute(f"DELETE from usuarios where login = '{login}'")
    banco.commit()

    print("\033[32mUsuário deletado com sucesso!\033[m")
    time.sleep(1)
  except Exception:
    banco.rollback()

    print("\033[31mErro ao deletar o usuário.\033[m")
    time.sleep(1)


def db_cria_denuncia(id_usuario, id_categoria, estado, cidade, rua, cep, data):
  try:
    cursor.execute(
      f"INSERT INTO denuncias (id_usuario, id_categoria, estado, cidade, rua, cep, data) VALUES ('{id_usuario}', '{id_categoria}', '{estado}', '{cidade}', '{rua}', '{cep}', '{data}')"
    )

    print("\033[32mDenúncia inserida com sucesso!\033[m")
    banco.commit()
    time.sleep(1)
  except Exception:
    print("\033[32mNão foi possivel fazer a denúncia.\033[m")
    banco.rollback()
    time.sleep(5)


def db_imprime_denuncia(id_usuario):
  try:
    dados = cursor.execute(
      f"SELECT * FROM denuncias WHERE denuncias.id_usuario = {id_usuario}")
    return dados
    print("\033[31mO login não foi encontrado no banco de dados.\033[m")
    time.sleep(1)
    return
  except Exception as e:
    print("\033[31mOcorreu um erro ao acessar o banco de dados:\033[m", str(e))
    time.sleep(1)
    return


def db_cria_telefone(id_usuario, telefone):
  try:
    cursor.execute(
      f"INSERT INTO telefones (id_usuario, telefone) values ({id_usuario}, '{telefone}')"
    )

    print("\033[32mTelefone inserido com sucesso!\033[m")
    banco.commit()
    time.sleep(1)
  except Exception:
    print("\033[31mNão foi possivel criar o telefone.\033[m")
    banco.rollback()
    time.sleep(1)


def db_imprime_telefone(id_usuario):
  try:
    dados = cursor.execute(
      f"SELECT * FROM telefones WHERE telefones.id_usuario = {id_usuario}")
    return dados
  except Exception as e:
    print("\033[31mOcorreu um erro ao acessar o banco de dados:\033[m", str(e))
    time.sleep(1)
    return


def db_altera_telefone(id_telefone, novo_valor):
  try:
    cursor.execute(
      f"UPDATE telefones set telefone = '{novo_valor}' where id_telefone = {id_telefone}"
    )

    print(f"\033[32mTelefone alterado(a) para {novo_valor}.\033[m")
    banco.commit()
    time.sleep(1)

  except sqlite3.IntegrityError:

    print("\033[31mNão foi possível alterar o telefone\033[m")
    banco.rollback()


def db_deleta_telefone(id_telefone):
  try:
    cursor.execute(f"DELETE from telefones where id_telefone = {id_telefone}")

    banco.commit()

    print("\033[32mTelefone deletado com sucesso!\033[m")
    time.sleep(1)
  except Exception:
    banco.rollback()

    print("\033[31mErro ao deletar o telefone.\033[m")
    time.sleep(1)


def db_imprime_ongs():
  try:
    dados = cursor.execute("select * from ongs")
    return dados
  except Exception:
    print("\033[31mErro ao visualizar a lista de ONGs.\033[m")
    time.sleep(1)


def db_cria_doacao(id_usuario, id_ong, valor, data, forma_pagamento):
  try:
    cursor.execute(
      f"INSERT INTO doacao (id_usuario, id_ong, valor, data, forma_pagamento) values ({id_usuario},{id_ong}, {valor}, '{data}', '{forma_pagamento}')"
    )

    print("\033[32mDoacão efetuada com sucesso!\033[m")
    banco.commit()
    time.sleep(1)
  except Exception:
    print("\033[31mNão foi possivel efetuar a doação.\033[m")
    banco.rollback()
    time.sleep(1)


def db_imprime_doacao(id_usuario):
  try:
    dados = cursor.execute(
      f"SELECT * from doacao WHERE doacao.id_usuario = {id_usuario}")
    return dados
    print("\033[31mO login não foi encontrado no banco de dados.\033[m")
    time.sleep(1)
  except Exception as e:
    print("\033[31mOcorreu um erro ao acessar o banco de dados:\033[m", str(e))
    time.sleep(1)
    return


# query = cursor.execute("select * from usuarios")
# print(cursor.fetchall())
