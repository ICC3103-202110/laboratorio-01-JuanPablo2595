### ------------- Juego Memorice --------------- ###
import numpy as np
import random as rd
### -------------- Definicion primer turno -------------- ###
def TurnOn():
    print()
    print("Puntaje de cada jugador: ")
    print(J1,": ",0)
    print(J2,": ",0)
    print()
    print(J1+" comienza jugando!: ")
    return ''
    
### ------------- Definicion turno primer jugador ------------------- ###

def J1Turn(J1,Game_board_python1,Game_board_python2):
    print("Para seleccionar tu primer carta: ")
    f1 = int(input(J1+", ingresa un numero i, donde i es la fila(horizontal) 0 o 1 del tablero: "))
    c1 = int(input(J1+", ingresa un numero j, donde j es la columna(vertical) desde 0: "))
    print("Para seleccionar tu segunda carta: ")
    f2 = int(input(J1+", ingresa un numero i, donde i es la fila(horizontal) 0 o 1 del tablero: "))
    c2 = int(input(J1+", ingresa un numero j, donde j es la columna(vertical) desde 0: "))
    J1cards = []
    if c1 <= Ncartas:
        if 0 <= f1 <= 1:
            if c2 <= Ncartas:
                if 0 <= f2 <= 1:
                    if f1 == 0 and f2 == 0:
                        card1 = Game_board_python1[c1]
                        card2 = Game_board_python1[c2]
                        if card1 == card2:
                            J1cards.append(card1)
                            Game_board_python1.pop(c1)
                            Game_board_python1.insert(c1," ")
                            Game_board_python1.pop(c2)
                            Game_board_python1.insert(c2," ")
                            file1.pop(c1)
                            file1.insert(c1," ")
                            file1.pop(c2)
                            file1.insert(c2," ")
                            print(J1," gana 1 punto!")
                        else:
                            print("Te equivocaste")
                    elif f1 == 0 and f2 == 1:
                        card1 = Game_board_python1[c1]
                        card2 = Game_board_python2[c2]
                        if card1 == card2:
                            J1cards.append(card1)
                            Game_board_python1.pop(c1)
                            Game_board_python1.insert(c1," ")
                            Game_board_python2.pop(c2)
                            Game_board_python2.insert(c2," ")
                            file1.pop(c1)
                            file1.insert(c1," ")
                            file2.pop(c2)
                            file2.insert(c2," ")
                            print(J1," gana 1 punto!")
                        else:
                            print("Te equivocaste")
                    elif f1 == 1 and f2 == 0:
                        card1 = Game_board_python2[c1]
                        card2 = Game_board_python1[c2]
                        if card1 == card2:
                            J1cards.append(card1)
                            Game_board_python2.pop(c1)
                            Game_board_python2.insert(c1," ")
                            Game_board_python1.pop(c2)
                            Game_board_python1.insert(c2," ")
                            file2.pop(c1)
                            file2.insert(c1," ")
                            file1.pop(c2)
                            file1.insert(c2," ")
                            print(J1," gana 1 punto!")
                        else:
                            print("Te equivocaste")
                    elif f1 == 1 and f2 == 1:
                        card1 = Game_board_python2[c1]
                        card2 = Game_board_python2[c2]
                        if card1 == card2:
                            J1cards.append(card1)
                            Game_board_python2.pop(c1)
                            Game_board_python2.insert(c1," ")
                            Game_board_python2.pop(c2)
                            Game_board_python2.insert(c2," ")
                            file2.pop(c1)
                            file2.insert(c1," ")
                            file2.pop(c2)
                            file2.insert(c2," ")
                            print(J1," gana 1 punto!")
                        else:
                            print("Te equivocaste")
                else:
                    print("Debes ingresar un numero valido!(0 o 1)")
            else:
                print("Debes ingresar un numero menor o igual a ",Ncartas)
        else:
            print("Debes ingresar un numero valido!(0 o 1)")
    else:
        print("Debes ingresar un numero menor o igual a ",Ncartas)
    return " "
            
                    

### ----------------- Tablero de la interfaz -------------------------- ###     

J1 = input("Ingrese el nombre del primer jugador: ")
J2 = input("Ingrese el nombre del segundo jugador: ")
Ncartas = int(input("Ingrese la cantidad de pares de cartas con las que desea jugar: "))

file1 = []
file2 = []
Game_board = []
for i in range(Ncartas):
    file1.append("*")
    file2.append("*")
    if i == Ncartas-1:
        break
Game_board.append(file1)
Game_board.append(file2)

### ------------ Tablero python ----------------- ###
Game_board_python1 = list(range(1,Ncartas+1))
Game_board_python2 = list(range(1,Ncartas+1))
rand_tablero1 = rd.shuffle(Game_board_python1)
rand_tablero2 = rd.shuffle(Game_board_python2)


print(Game_board)
print(Game_board_python1)
print(Game_board_python2)
print(TurnOn())
print(J1Turn(J1,Game_board_python1,Game_board_python2))