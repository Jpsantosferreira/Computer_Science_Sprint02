# LOGICA E (and)

verifica_email = True
verifica_senha= True

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Loga certo ai carai...")