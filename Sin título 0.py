### ------------- Juego Memorice --------------- ###
import numpy
from sympy.abc import x

Ncartas = int(input("Ingrese la cantidad de pares de cartas con las que desea jugar: "))
#J1 = input("Ingrese el nombre del primer jugador: ")
#J2 = input("Ingrese el nombre del segundo jugador: ")
J1score = 0
J2score = 0
list1 = list(range(1,Ncartas+1))
list2 = list(range(1,Ncartas+1))

Game_board = numpy.array([list1,list2])

check = numpy.zeros((2,Ncartas))
checklist = check.tolist()

for i in list1):
    for j in (list2):
        checklist.incert(j,E)
        

#print(Game_board)
print()
print(checklist)
print()
print()



