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
    ["S",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
]
fd=sys.stdin.fileno()
old=termios.tcgetattr(fd)
continuar=True

#jugador
jugadory=0
jugadorx=0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if(mapa[i][j]=="S"):
            jugadory=i
            jugadorx=j
direcion="derecha"
def mover():
    time.sleep(0.9)
    global jugadory, jugadorx,avansar
    global continuar,direcion
    teclado=""
    
    if select.select([sys.stdin],[],[], 0)[0]:
        teclado=sys.stdin.read(1)
        if(teclado=="."):
            continuar=False
    
    y=jugadory
    x=jugadorx
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
        jugadorx+=1
    elif(direcion=="izquierda" and jugadorx>0):
        jugadorx-=1
    elif(direcion=="arriba" and jugadory>0):
        jugadory-=1
    elif(direcion=="abajo" and jugadory < len(mapa[0])-1):
        jugadory+=1
    mapa[y][x] = "."
    mapa[jugadory][jugadorx] = "S"

def mostraMapa():
    global mapa
    for filas in mapa:
        sys.stdout.write("".join(filas)+"\r\n")

try:
    tty.setraw(fd)
    while continuar:
        os.system("clear")
        mostraMapa()  
        mover()
except Exception as e:
    print(e)
finally:
    termios.tcsetattr(fd,termios.TCSADRAIN,old)