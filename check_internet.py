import os
import time
import socket

SERVIDOR_REMOTO = "www.google.com"
def is_connected():
  try:
    # ver se podemos resolver o nome do host -- nos diz se há
    # uma resposta de DNS
    host = socket.gethostbyname( SERVIDOR_REMOTO)
    # conecta ao host -- nos informa se o host está realmente
    # alcançavel
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     print("[X] Internet Desconectada \r",end="")
     pass
  return False

# print(esta_conectado())