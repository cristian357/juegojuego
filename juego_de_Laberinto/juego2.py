import os
import time
pantalla = [
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
    ["#","S",".",".","#",".",".",".",".",".","#",".",".","#"],
    ["#",".","#",".","#",".","#","#","#",".","#",".","#","#"],
    ["#",".","#",".",".",".","#","2",".",".","#",".","1","#"],
    ["#",".","#","#","#",".","#",".","#","#","#","#",".","#"],
    ["#",".",".",".","#",".",".",".","#",".",".",".",".","#"],
    ["#","#","#",".","#","#","#",".","#",".","#","#",".","#"],
    ["#",".",".",".",".",".","#",".","#",".",".","#",".","#"],
    ["#",".","#","#","#",".","#",".","#","#",".","#",".","#"],
    ["#",".","#",".",".",".",".",".",".","#",".",".",".","#"],
    ["#",".","#",".","#","#","#","#",".","#","#","#",".","#"],
    ["#",".",".",".",".",".",".",".",".",".",".",".","E","#"],
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
]
moverenemigo=1
devolver1=True
devolver2=True

# ubicasion de enemigo 1 y 2 y jugador
enemigo1y=0
enemigo1X=0

enemigo2y=0
enemigo2X=0

jugadory=0
jugadorx=0
# ubicasion de la meta
metay=0
metax=0
for i in range(len(pantalla)):
    for j in range(len(pantalla[i])):
        if(pantalla[i][j]=="1"):
            enemigo1y=i
            enemigo1X=j
        elif(pantalla[i][j]=="2"):
            enemigo2y=i
            enemigo2X=j
        elif(pantalla[i][j]=="S"):
            jugadory=i
            jugadorx=j
        elif(pantalla[i][j]=="E"):
            metay=i
            metax=j



def mostraPantalla():
    for i in range(len(pantalla)):
        for j in range(len(pantalla[i])):
            print(pantalla[i][j],end="")
        print("")
def limpiarPantalla():
    os.system("clear")
def mover_enemigo():
    global moverenemigo,enemigo1y,enemigo1X,enemigo2y,enemigo2X,devolver1,devolver2
    if(moverenemigo==1):
        y1=enemigo1y
        x1=enemigo1X
        if(devolver1):
            enemigo1y+=1
        else:
            enemigo1y-=1
        if(pantalla[enemigo1y+1][enemigo1X]=="E"):
            devolver1=False
        elif(pantalla[enemigo1y-1][enemigo1X]=="#"):
            devolver1=True
        pantalla[y1][x1]="."
        pantalla[enemigo1y][enemigo1X]="1"
        moverenemigo+=1
    elif(moverenemigo==2):
        y2=enemigo2y
        x2=enemigo2X
        if(devolver2):
            enemigo2y+=1
        else:
            enemigo2y-=1
        if(pantalla[enemigo2y+1][enemigo2X]=="#"):
            devolver2=False
        elif(pantalla[enemigo2y-1][enemigo2X]=="#"):
            devolver2=True
        pantalla[y2][x2]="."
        pantalla[enemigo2y][enemigo2X]="2"
        moverenemigo-=1
def colision_enemigo():
    global jugadorx,jugadory
    if(pantalla[jugadory][jugadorx]=="1"or pantalla[jugadory+1][jugadorx]=="1" or pantalla[jugadory-1][jugadorx]=="1" or pantalla[jugadory][jugadorx+1]=="1" or pantalla[jugadory][jugadorx-1]=="1"
        or pantalla[jugadory][jugadorx]=="2"or pantalla[jugadory+1][jugadorx]=="2" or pantalla[jugadory-1][jugadorx]=="2" or pantalla[jugadory][jugadorx+1]=="2" or pantalla[jugadory][jugadorx-1]=="2"):
        return True
def peder():
    print("¡Has perdido!")
def movimiento_judor():
    move=0
    try:
        move=int(input("↑ = 1 ↓ = 2 ← = 3 → = 4 "))
        if(move<1 or move>4):
            print("movimiento no valido")
            time.sleep(3)
        else:
            return move
    except:
        print("movimiento no valido")
        time.sleep(3)
    
def movimiento_valido(movimiento):
    global jugadorx,jugadory
    match movimiento:
        case 1:
            if(pantalla[jugadory-1][jugadorx]=="." or pantalla[jugadory-1][jugadorx]=="E"):
                return True
            else:
                print("Te estrellaste contra una pared")
                time.sleep(3)
                return False
        case 2:
            if(pantalla[jugadory+1][jugadorx]=="." or pantalla[jugadory+1][jugadorx]=="E"):
                return True
            else:
                print("Te estrellaste contra una pared")
                time.sleep(3)
                return False
        case 3:
            if(pantalla[jugadory][jugadorx-1]=="." or pantalla[jugadory][jugadorx-1]=="E"):
                return True
            else:
                print("Te estrellaste contra una pared")
                time.sleep(3)
                return False
        case 4:
            if(pantalla[jugadory][jugadorx+1]=="."or pantalla[jugadory][jugadorx+1]=="E"):
                return True
            else:
                print("Te estrellaste contra una pared")
                time.sleep(3)
                return False
def mover_jugador(movimiento):
    global jugadorx,jugadory
    y=jugadory
    x=jugadorx
    match movimiento:
        case 1:
            jugadory-=1
            pantalla[jugadory][jugadorx]="S"
            pantalla[y][x]="."
        case 2:
            jugadory+=1
            pantalla[jugadory][jugadorx]="S"
            pantalla[y][x]="."
        case 3:
            jugadorx-=1
            pantalla[jugadory][jugadorx]="S"
            pantalla[y][x]="."
        case 4:
            jugadorx+=1
            pantalla[jugadory][jugadorx]="S"
            pantalla[y][x]="."
def validar_meta():
    global jugadorx,jugadory ,metay,metax
    if(metay==jugadory and metax==jugadorx):
        return True
    else:
        return False
def gana():
    print("¡Ganaste la partida!")
while True:
    limpiarPantalla()
    mostraPantalla()
    mover_enemigo()
    if(colision_enemigo()):
        peder()
        break
    movimiento=movimiento_judor()
    print(movimiento)
    if movimiento_valido(movimiento):
        mover_jugador(movimiento)
        if(validar_meta()):
            gana()
            break