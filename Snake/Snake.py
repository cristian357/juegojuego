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
    else:
        colocar_manzana()

#jugador y su movimiendo
jugadory=0
jugadorx=0
serpiente=[[0,0]]
direcion="derecha"
def mover():
    time.sleep(0.3)
    global jugadory, jugadorx,avansar,serpiente
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
    '''''
    lo que ase nuevacabesa es segun adonde se estam moviendo el jugador en ves de moder la cola
    una por uno lo que ago es eliminar la ultima s y le agrgo al inicio una s esto da la isucion
    de que se esta moviendo 
    '''''
    nuevo_y = jugadory
    nuevo_x = jugadorx
    nuevacabesa=[nuevo_y,nuevo_x]
    serpiente.insert(0,nuevacabesa)
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
    else: 
        continuar=False

    if(mapa[nuevo_y][nuevo_x]=="#"):
        putos+=1
        colocar_manzana()
    else:
        '''''
        el como funsiona esto es en la siguiente manera es que sino  se comio la manzana 
        elimina la cola es desir la oltima s 
        '''''
        cola_viejo=serpiente.pop()
        mapa[cola_viejo[0]][cola_viejo[1]] = "."
        # para python 0 y 1 funsiona algo pare sido a i y j pero el motor lo tra duse y le asina el valor que le correponde
    jugadorx=nuevo_x
    jugadory=nuevo_y
    mapa[viejo_y][viejo_x] = "."
    for bloque in serpiente:
        mapa[bloque[0]][bloque[1]] = "S"
    if(mapa[nuevo_y][nuevo_x]=="S"):
        print("temordiste la cola")
        continuar=False




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
        os.system("clear")
        mostraputos()
        mostraMapa()  
        if(not continuar):
            sys.stdout.write("\r\n¡CHOCASTE CONTRA LA PARED! Juego terminado.\r\n")
except Exception as e:
    print(e)
finally:
    termios.tcsetattr(fd,termios.TCSADRAIN,old)