import tty
import termios
import sys
import random
import os,time,select
mapa = [
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
]
fd=sys.stdin.fileno()
old=termios.tcgetattr(fd)
continuar=True
putos=0
# manzana
manzanax=0
manzanay=0
def colocar_manzana():
    manzanay=random.randint(0,len(mapa)-1)
    manzanax=random.randint(0,len(mapa[0])-1)
    if(mapa[manzanay][manzanax]=="."):
        mapa[manzanay][manzanax]="#"

#jugador y su movimiendo
jugadory=0
jugadorx=0
for i in range(len(mapa)-1):
    for j in range(len(mapa[i])-1):
        if(mapa[i][j]=="S"):
            jugadory=i
            jugadorx=j
direcion="derecha"
def mover():
    time.sleep(0.5)
    global jugadory, jugadorx,avansar
    global continuar,direcion,putos
    teclado=""
    
    if select.select([sys.stdin],[],[], 0)[0]:
        teclado=sys.stdin.read(1)
        if(teclado=="."):
            continuar=False
    # Guardamos la posición vieja para borrarla luego
    viejo_y = jugadory
    viejo_x = jugadorx
    # Calcular la nueva posición tentativa
    nuevo_y = jugadory
    nuevo_x = jugadorx
    match teclado:
        case "w":
            if(jugadory>0):
                direcion="arriba"
        case "s":
            if(jugadory < len(mapa) - 1):
                direcion="abajo"
        case "a":
            if(jugadorx>0):
                direcion="izquierda"
        case ("d"):
            if(jugadorx <len(mapa[0])-1):
                direcion="derecha"
    if(direcion=="derecha"and jugadorx < len(mapa[0])-1):
        nuevo_x+=1
    elif(direcion=="izquierda" and jugadorx>0):
        nuevo_x-=1
    elif(direcion=="arriba" and jugadory>0):
        nuevo_y-=1
    elif(direcion=="abajo" and jugadory < len(mapa)-1):
        nuevo_y+=1
    if(mapa[nuevo_y][nuevo_x]=="#"):
        putos+=1
        colocar_manzana()
    jugadorx=nuevo_x
    jugadory=nuevo_y
    mapa[viejo_y][viejo_x] = "."
    mapa[jugadory][jugadorx] = "S"

def mostraputos():
    global putos
    sys.stdout.write(f"putos {putos}"+"\r\n")
def mostraMapa():
    global mapa
    for filas in mapa:
        sys.stdout.write("".join(filas)+"\r\n")
colocar_manzana()
try:
    tty.setraw(fd)
    while continuar:
        os.system("clear")
        mostraputos()
        mostraMapa()  
        mover()
except Exception as e:
    print(e)
finally:
    termios.tcsetattr(fd,termios.TCSADRAIN,old)