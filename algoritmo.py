'''
Sprint 02- Computer Science
=== Algoritmo em Python - Funcionamento do Eletroposto ===

* USO DE DADOS SIMULADOS! *

'''
import sys

'''
=== C P / Pk M / T S V / E === 
C - Cartão RFID 
P - Plugue conectado
Pk - Modo parking
M - Motor desligado
T - Temperatura normal
S - Sistema em normalidade
V - Tensão em normalidade
E - Modo de emergência 
'''

# OBS: A função login vai ser adicionada aqui para
# diferenciar os paineis de controle entre cliente e administrador!

# == DADOS SIMULADOS ================

cartao_RFID = True
plugue_conectado = True
modo_parking = True
motor_desligado = True

temperatura_normal = True
sistema_normal = True
tensao_normal = True

modo_emergencia = False

# porcentagem da bateria ---
bateria = 40

'''
====== login - acesso ======
Teremos dois tipos de usuários desse sistema:
- cliente (user)
- administrador (admin) 
" nesse caso, o cliente só terá acesso a certas partes do sistema, que serão exibidas para o mesmo.
já o administrador terá acesso a tudo isso, já que é ele que irá tomar as medidas necessárias em 
caso de qualquer disturbio ou problema. "

'''
''' 
Condições físicas: é um mecanismo de segurança.
- liberação de acesso ao carregador (cartão RFID); 
- plugue conectado seria algum veículo conectado ao carregador; 
- modo parking seria o carro em modo de estacionamento, ou seja, com "freio de mão" puxado 
para evitar acidentes com a movimentação repentina do veículo;
- motor desligado é mais uma segurança para evitar acidentes, além de ser o recomendado ao carregar um carro elétrico.
'''

'''
Condições elétricas: a segurança da elétrica e do sistema.
- temperatura precisa estar em normalidade para evitar superaquecimento e outros acidentes;
- tensão precisa estar presente e em normalidade para o sistema como um todo funcionar;
- sistema em normalidade significa que tudo está pronto para funcionar.
'''

'''
Modo de emergência: é um mecanismo de segurança presente no eletroposto (fisicamente) para 
evitar acidentes que o sistema não possa impedir ou resolver, como um incêndio, por exemplo.
'''
# ====== condições físicas ======
cond_fisica = cartao_RFID and plugue_conectado and modo_parking and motor_desligado

# ====== condições elétricas ======
cond_eletricas = temperatura_normal and sistema_normal and tensao_normal

# ====== modo de emergência ======
parada_sistema = modo_emergencia

# ====== Sistema OK ======
saida_final = cond_fisica and cond_eletricas and not parada_sistema

'''
saida final verifica se o sistema está ok e pronto para uso do carregador.
'''
# ====== login ======
login = input("Digite seu login: ")
if login == "user":
    print("bem-vindo, user")
elif login == "admin":
    print("bem-vindo, admin")
else:
    print("login inexistente")

# ====== carregando - status(bateria) ======
carregando = bateria

# ====== login - saidas  ======
'''
Nas saídas, temos o case do user, que seria a interface do usuário (simplificada).
E também temos o case do admin, que é a interface do administrador.
'''

import subprocess

match login:
    case "user":
        # verificação do RFID do cliente...
        if cartao_RFID:
            print("RFID autorizado --- Liberado para uso ✔️")
            subprocess.run(['afplay', '/System/Library/Sounds/Funk.aiff'])
        else:
            print("RFID inexistente --- Bloqueado para uso ❕")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])
            sys.exit()

        # aqui verifica se o modo de emergência foi acionado...
        if not parada_sistema:
            print("Modo de emergência --- NÃO ACIONADO 🟢")
        else:
            print("Modo de emergência --- ACIONADO 🔺")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])
            sys.exit()

        # e aqui a saida final, se está tudo na normalidade ou não...
        if saida_final:
            print("Sistema em normalidade = Liberado para uso 🟢")
            subprocess.run(['afplay', '/System/Library/Sounds/Hero.aiff'])
        else:
            print("Sistema fora de normalidade --- Notificando a administração. Desculpas pelo transtorno 😔")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])
            sys.exit()

        # status da bateria --- para o cliente
        if carregando < 100 and saida_final:
            print(f"Carregando --- Bateria em {bateria} % 🔹")
            subprocess.run(['afplay', '/System/Library/Sounds/Funk.aiff'])
        elif carregando == 100 and saida_final:
            print(f"{bateria} % --- Bateria Carregada 🟢")
            subprocess.run(['afplay', '/System/Library/Sounds/Hero.aiff'])
        else:
            print("Ocorreu algum erro com o carregamento. Notificando a administração! -- desculpe pelo transtorno 😔")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])

    case "admin":
        # mostra pro admin os status das condições físicas do eletroposto...
        if cond_fisica:
            print("Condições físicas --- STATUS = OK ✅")
            subprocess.run(['afplay', '/System/Library/Sounds/Hero.aiff'])
        else:
            print("Condições físicas --- STATUS = FALHA 🔸️")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])

        # aqui mostra os status das condições elétricas...
        if cond_eletricas:
            print("Condições elétricas --- STATUS = OK ✅")
            subprocess.run(['afplay', '/System/Library/Sounds/Hero.aiff'])
        else:
            print("Condições elétricas --- STATUS = FALHA ❗️️")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])

        # aqui mostra se o modo de emergência foi acionado ou não...
        if not parada_sistema:
            print("Modo de emergência --- NÃO ACIONADO 🔹")
        else:
            print("Modo de emergência --- ACIONADO 🔸")


        # e aqui a saída final e os status da bateria...
        if saida_final:
            print("O sistema está em perfeito funcionamento --- ☑️")
            subprocess.run(['afplay', '/System/Library/Sounds/Hero.aiff'])
        else:
            print("Existe algo de errado com o sistema --- ❗️")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])

        if bateria < 100:
            print(f"Nível de carregamento --- STATUS: {bateria} % ==> carregando 📶")
            subprocess.run(['afplay', '/System/Library/Sounds/Funk.aiff'])
        elif bateria == 100:
            print(f"Nível de carregamento --- STATUS: {bateria} % ==> completo ☑️")
            subprocess.run(['afplay', '/System/Library/Sounds/Hero.aiff'])
        else:
            print("Ocorreu um erro com o carregamento do veículo --- STATUS: FALHA ❌")
            subprocess.run(['afplay', '/System/Library/Sounds/Basso.aiff'])

















