from banco import db_imprime_ongs

menu = 60


def cabecalho(texto):
  print("\033[32m-" * menu)
  print("{:^60}".format(f"{texto}"))
  print("-" * menu, '\033[m')


def menu_inicial():
  resposta = 5
  cabecalho("Diversidade Brasil")
  while resposta != 1 and resposta != 2 and resposta != 3 and resposta != 0:
    try:

      print("1 - Cadastrar:\n2 - Logar\n3 - Anônimo:")
      resposta = int(input("Selecione uma opção: "))
    except ValueError:
      print("Por favor insira um número")
    if resposta != 1 and resposta != 2 and resposta != 3 and resposta != 0:
      print("Por favor, insira um número entre 0 a 3.")

  return resposta


def menu_cadastro_usuario():
  cabecalho("Cadastro")
  print("Por favor, insira seus dados.")
  nome = input("Insira seu nome: ")
  email = input("Insira seu email: ")
  login = input("Insira seu login: ")
  senha = input("Insira sua senha: ")

  return {'nome': nome, 'email': email, 'login': login, 'senha': senha}


def menu_login_usuario():
  cabecalho("Login")
  login = input("Insira o login do usuário: ").lower().strip()
  senha = input("Insira sua senha: ").strip()

  return {'login': login, 'senha': senha}


def menu_localizacao():

  estado = input("Insira o estado da denúncia : ")
  cidade = input("Insira a cidade da denúncia : ")
  cep = input("Insira o cep da denuncia : ")
  rua = input("Insira a rua da denuncia : ")

  return {'estado': estado, 'cidade': cidade, 'cep': cep, 'rua': rua}


def menu_denuncia():
  resposta = -1
  while resposta != 1 and resposta != 2 and resposta != 0:
    try:
      resposta = int(
        input("1 - Realizar denúncia\n2 - Visualizar denúncias\n0.Voltar : "))
    except ValueError:
      print("Insira um valor numérico!")

    if resposta != 1 and resposta != 2 and resposta != 0:
      print("Insira um valor entre 0 a 2!")

  return resposta


def menu_cria_denuncia():
  resposta = -1
  categorias = {
    1: 'Queimadas',
    2: 'Poluição do ar',
    3: 'Poluição da água',
    4: 'Desmatamento'
  }

  while resposta < 0 or resposta > 4:
    try:
      resposta = int(
        input(
          f"1 - Queimadas\n2 - Poluição do ar\n3 - Poluição da água\n4 - Desmatamento\n0.Sair\n"
        ))

    except ValueError:
      print("Insira um valor numérico.")

    if resposta < 0 or resposta > 4:
      print("Insira uma valor entre 0 e 4!")
  if resposta > 0:
    print(f"Você selecionou a categoria {categorias[resposta]}")
  return resposta


def menu_logado(nome):

  resposta = 5

  while resposta != 1 and resposta != 2 and resposta != 3 and resposta != 0:
    try:
      resposta = int(
        input(
          f"Olá, {nome.capitalize()}. Selecione uma opção:\n1 - Denúncia\n2 - Doação\n3 - Dados Pessoais\n0 - Sair: "
        ))
    except ValueError:
      print("Por favor, insira um número")
    if resposta != 1 and resposta != 2 and resposta != 3 and resposta != 0:
      print("Por favor, insira um numero entre 0 a 3.")
  return resposta


def menu_altera_usuario():
  resposta = 0

  while resposta < 1 or resposta > 4:
    try:
      print("ALTERAR USUÁRIO")
      print("1- Alterar nome")
      print("2- Alterar email")
      print("3- Alterar login")
      print("4- Alterar senha")
      resposta = int(input("Selecione uma das opções : "))
    except ValueError:
      print("Por favor insira um número.")
    if resposta < 1 or resposta > 4:
      print("Número inválido. Por favor, insira um número entre 1 a 4.")

  coluna_selecionada = {1: 'nome', 2: 'email', 3: 'login', 4: 'senha'}
  novo_valor = ""

  while novo_valor.strip() == "":
    novo_valor = input(
      f"Insira um novo valor para {coluna_selecionada[resposta]} : ")

  coluna = coluna_selecionada[resposta]
  return {coluna, novo_valor}


def menu_dados_usuario():
  print("DADOS USUARIO")
  resposta = 0
  while resposta != 1 and resposta != 2 and resposta != 3:
    try:
      resposta = int(
        input("1 - Alterar Usuario\n2 - Excluir conta\n3 - Telefone: "))

    except ValueError:
      print("Por favor insira um número.")

    if resposta != 1 and resposta != 2 and resposta != 3:
      print("Insira uma número entre 1 e 3!")

  return resposta


def menu_telefone():
  resposta = -1

  while resposta < 0 or resposta > 4:
    try:
      print("ALTERAR USUÁRIO")
      print("1- Criar telefone")
      print("2- Imprimir lista de telefones")
      print("3- Alterar telefone")
      print("4- Excluir telefone")
      print("0 - Voltar")
      resposta = int(input("Selecione uma das opcoes: "))
    except ValueError:
      print("Por favor insira um número.")
    if resposta < 1 or resposta > 4:
      print("Numero invalido. Por favor, insira um numero entre 0 a 4")
  return resposta


def menu_altera_telefone(dict_telefone):
  resposta = 0
  existe_no_dict = False
  while existe_no_dict == False:
    resposta = int(input("Selecione o telefone que deseja alterar: "))

    for i in dict_telefone:
      if i == resposta:
        existe_no_dict = True

  novo_valor = ""
  while novo_valor.strip() == "":
    novo_valor = input("Insira o novo numero para o telefone: ")

  return {'id': dict_telefone[resposta], 'novo_valor': novo_valor}


def menu_deleta_telefone(dict_telefone):
  resposta = 0
  existe_no_dict = False
  while existe_no_dict == False:
    resposta = int(input("Selecione o telefone que deseja alterar: "))

    for i in dict_telefone:
      if i == resposta:
        existe_no_dict = True

  return dict_telefone[resposta]


def menu_seleciona_ongs():
  dados = db_imprime_ongs()
  print("LISTA DE ONGS")
  for tupla in dados:
    print("-" * 60)
    print(f"{tupla[0]}: {tupla[1]}")
    print(f"Essa ONG tem como missão {tupla[3]}")
    print(f"Contato: {tupla[2]}")

  resposta = -1

  while resposta < 0 or resposta > 9:
    try:
      resposta = int(
        input("Selecione uma das ONGs acima ou aperte 0 para sair: "))
    except ValueError:
      print("Por favor insira um número.")
    if resposta < 0 or resposta > 9:
      print("Numero invalido.")

  return resposta


def menu_valor_doacao():
  valor = 0.0
  while valor < 1.0:
    try:
      valor = float(input("Insira o valor da doacão: "))
    except ValueError:
      print("Insira um valor numérico")
    if valor < 1.0:
      print("O valor mínimo para doação é 1 real")
  return valor


def menu_forma_pagamento():
  resposta = -1
  pagamento = {1: 'PIX', 2: 'Cartão de crédito'}
  while resposta != 1 and resposta != 2 and resposta != 0:
    for i in pagamento:
      print(f'{i}: {pagamento[i]}')
    try:
      resposta = int(input("Insira uma forma de pagamento: "))
    except ValueError:
      print("Insira um valor numérico!")

    if resposta != 1 and resposta != 2 and resposta != 0:
      print("Insira um valor entre 0 e 2!")

  return pagamento[resposta]


def menu_doacao():
  resposta = -1

  while resposta < 0 or resposta > 2:
    try:
      resposta = int(
        input("1.Realizar doacao\n2.Lista de doacoes realizadas\n0.Sair: "))
    except ValueError:
      print("Insira um valor numérico")
    if resposta < 0 or resposta > 2:
      print("Insira um número válido.")

  return resposta
