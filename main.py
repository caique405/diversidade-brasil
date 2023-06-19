from usuario import Usuario
from denuncia import Denuncia
from menu import menu_inicial, menu_logado, menu_cadastro_usuario, menu_login_usuario, menu_altera_usuario, menu_dados_usuario, menu_denuncia, menu_localizacao, menu_cria_denuncia, menu_telefone, menu_altera_telefone, menu_deleta_telefone, menu_seleciona_ongs, menu_valor_doacao,  menu_forma_pagamento, menu_doacao, cabecalho
from banco import db_imprime_usuario
from telefone import Telefone
from doacao import Doacao
import os
import datetime
import time

def clear():
  # Replit roda em linux
  if os.name == 'posix':
    _ = os.system('clear')

  #caso esse código estiver rodando em windows
  else:
    _ = os.system('cls')


def main():
  #MENU INICIAL
  while True:
    
    resposta = menu_inicial()
    clear()
    #cria usuario
    if resposta == 1:
      
      dados = menu_cadastro_usuario()
      clear()
      usuario = Usuario(dados['nome'], dados['email'], dados['login'],
                        dados['senha'])
      usuario.cria_usuario()
      
    #Logar
    elif resposta == 2:
      nome = None
      email = None
      while nome == None or email == None:
        dados = menu_login_usuario()
        clear()
        nome = db_imprime_usuario(dados['login'])[1]
        if nome != None:
          email = db_imprime_usuario(dados['login'])[2]
      
      usuario = Usuario(nome, email, dados['login'], dados['senha'])
      logar = usuario.loga_usuario()
      if logar == 1:
        #MENU LOGADO
        while True:
          cabecalho("Menu")
          resposta = menu_logado(nome)
          clear()
          match resposta:
            #DENUNCIA
            case 1: 
              resposta = menu_denuncia()
              clear()
              match resposta:
                #CRIA DENUNCIA
                case 1:
                  id_categoria = menu_cria_denuncia()
                  if id_categoria == 0:
                    pass
                  else:
                    clear()
                    id_usuario = db_imprime_usuario(dados['login'])[0]
                    localizacao = menu_localizacao()
                    clear()
                    data = datetime.datetime.now()
                    denuncia = Denuncia(id_usuario, id_categoria, localizacao['estado'], localizacao['cidade'], localizacao['rua'], localizacao['cep'], data)
                    denuncia.cria_denuncia()
                #IMPRIME DENUNCIA
                case 2:
                  id_usuario = db_imprime_usuario(dados['login'])[0]
                  denuncia = Denuncia(id_usuario)
                  denuncia.imprime_denuncia()
                #SAIR
                case 0: 
                  pass
            #DOACAO
            case 2:
              resposta = menu_doacao()
              clear()
              match resposta:
                #CRIA DOACAO
                case 1:
                  id_usuario = int(db_imprime_usuario(dados['login'])[0])
                  id_ong = menu_seleciona_ongs()
                  clear()
                  valor = menu_valor_doacao()
                  clear()
                  data = datetime.datetime.now()
                  forma_pagamento = menu_forma_pagamento()
                  clear()
                  doacao = Doacao(id_usuario, id_ong, valor, data, forma_pagamento)
                  doacao.cria_doacao()
                #IMPRIME DOACAO
                case 2:
                  id_usuario = int(db_imprime_usuario(dados['login'])[0])
                  doacao = Doacao(id_usuario)
                  doacao.imprime_doacao()
                #VOLTAR
                case 0:
                  pass
            #DADOS PESSOAIS
            case 3:
              usuario.imprime_usuario()
              resposta = menu_dados_usuario()
              clear()
              match resposta:
                #ALTERA USUARIO
                case 1:
                  usuario.altera_usuario()
                #DELETA USUARIO
                case 2:
                  usuario.deleta_usuario()
                # TELEFONE
                case 3:
                  id_usuario = db_imprime_usuario(dados['login'])[0]
                  resposta = menu_telefone()
                  clear()
                  match resposta:
                    #CRIA TELEFONE
                    case 1:
                      inserir_telefone = ""
                      while inserir_telefone.strip() == "":
                        inserir_telefone = input("Insira o numero do telefone : ")
                      telefone = Telefone(id_usuario, inserir_telefone)
                      telefone.cria_telefone()
                    #IMPRIMIR TELEFONES
                    case 2: 
                      telefone = Telefone(id_usuario)
                      telefone.imprime_telefone()
                    # ALTERAR TELEFONE
                    case 3:
                      telefone = Telefone(id_usuario)
                      dict_telefone = telefone.imprime_telefone()
                      dados_alterar = menu_altera_telefone(dict_telefone)
                      clear()
                      telefone.altera_telefone(dados_alterar['id'], dados_alterar['novo_valor'])
                    #EXCLUIR TELEFONE
                    case 4:
                      telefone = Telefone(id_usuario)
                      dict_telefone = telefone.imprime_telefone()
                      id = menu_deleta_telefone(dict_telefone)
                      clear()
                      telefone.deleta_telefone(id)
                    case 0:
                      pass
            #vOLTAR
            case 0:
              break
      else:
        print("\033[31mUsuario ou senha inválidos!\033[m")

    #anonimo
    elif resposta == 3:
      cabecalho("Modo anônimo")
      usuario = Usuario('anonimo', 'anonimo', 'anonimo', 'anonimo')
      id_categoria = menu_cria_denuncia()
      clear()
      id_usuario = 1
      localizacao = menu_localizacao()
      clear()
      data = datetime.datetime.now()
      denuncia = Denuncia(id_usuario, id_categoria, localizacao['estado'], localizacao['cidade'], localizacao['rua'], localizacao['cep'], data)
      denuncia.cria_denuncia()
      time.sleep(5)
      
    elif resposta == 0:
      main()


if __name__ == "__main__":
  main()
