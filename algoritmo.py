'''
Sprint 02- Computer Science
=== Algoritmo em Python - Funcionamento do Eletroposto ===

* USO DE DADOS SIMULADOS! *

'''
from pip._internal.utils import subprocess

'''
--- P E D T V A ---
P = Plugue conectado ao veículo;
E = Parada de emergência não acionada;
D = Porta do carregador fechada;
T = Proteção térmica Ok - temperatura normal;
V = Tensão da rede presente;
A = Autorização do sistema (Usuário/ site / RFID).
'''

# == DADOS SIMULADOS ================

plugue_conectado = True
porta_carregador_fechada = True

parada_emergencia = False


temperatura_normal = True
tensao_rede = True

acesso_email = True
acesso_senha = True

# ===== condições físicas ==============

seg_fisica = plugue_conectado and porta_carregador_fechada
if seg_fisica:
    print("Segurança física: Status = OK. ")
else:
    print("Segurança física: Status = FALHA. ")

# ===== parada de emergência ==============

if not parada_emergencia:
    print("Parada de emergência: NÃO ACIONADA 🔹.")
else:
    print("Parada de emergência: ACIONADA 🔺.")

# ===== acesso do usuário ==============

login = acesso_email and acesso_senha
if login:
    print("Login: Correto - Liberado")
else:
    print("Login: Incorreto - Tente novamente.")

# ===== condições elétricas ==============

carga = temperatura_normal and tensao_rede
if carga:
    print("Carga: Status = Liberado para carregar. ")
else:
    print("Carga: Status = Bloqueado para carregar! ")

# ======== saidas ==============
import subprocess

saida_final = login and carga and not parada_emergencia and seg_fisica

if saida_final:
    print("🟢 == > Pronto / Carregado") # led verde
else:
    print("🔴 == > Bloqueado / Falha") # led vermelha
    subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])



