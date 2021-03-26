### ------------- Juego Memorice --------------- ###
import random as rd
### -------------- Definicion primer turno -------------- ###
def TurnOn():
    print()
    print("Score of each player: ")
    print(J1,": ",0)
    print(J2,": ",0)
    print()
    print(J1+" start playing!: ")
    return ''
    
### ------------- Definicion turno primer jugador ------------------- ###

def J1Turn(J1,Game_board_python1,Game_board_python2,J1score):
    print("To select your first card: ")
    print(Game_board)
    f1 = int(input(J1+", enter a number i, where i is row (horizontal) 0 or 1 on the board: "))
    c1 = int(input(J1+", enter a number j, where j is the column (vertical) from 0: "))
    print("To select your second card: ")
    f2 = int(input(J1+", enter a number i, where i is row (horizontal) 0 or 1 on the board: "))
    c2 = int(input(J1+", enter a number j, where j is the column (vertical) from 0: "))
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
                            print(J1," earn 1 point!")
                            J1score += 1
                            A = True
                            if len(J1cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:   
                                print(J1+", you keep playing! ")
                                return " "
                        else:
                            A = False
                            print("You were wrong")
                            return " "
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
                            print(J1," earn 1 point!")
                            J1score += 1
                            A = True
                            if len(J1cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:   
                                print(J1+", you keep playing! ")
                                return " "
                        else:
                            A = False
                            print("You were wrong")
                            return " "
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
                            print(J1," earn 1 point!")
                            J1score += 1
                            A = True
                            if len(J1cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:   
                                print(J1+", you keep playing! ")
                                return " "
                        else:
                            A = False
                            print("You were wrong")
                            return " "
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
                            print(J1," earn 1 point!")
                            J1score += 1
                            A = True
                            if len(J1cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:
                                print(J1+", you keep playing! ")
                                return " "
                        else:
                            A = False
                            print("You were wrong")
                            return " "
                else:
                    print("You must enter valid numbers!")
            else:
                print("You must enter valid numbers!")
        else:
            print("You must enter valid numbers!")
    else:
        print("You must enter valid numbers! ")
    return " "

### ------------- Definicion turno segundo jugador ------------------- ###

def J2Turn(J2,Game_board_python1,Game_board_python2,J2score):
    print("To select your first card: ")
    print(Game_board)
    f1 = int(input(J2+", enter a number i, where i is row (horizontal) 0 or 1 on the board: "))
    c1 = int(input(J2+", enter a number j, where j is the column (vertical) from 0: "))
    print("To select your second card: ")
    f2 = int(input(J2+", enter a number i, where i is row (horizontal) 0 or 1 on the board: "))
    c2 = int(input(J2+", enter a number j, where j is the column (vertical) from 0: "))
    J2cards = []
    if c1 <= Ncartas:
        if 0 <= f1 <= 1:
            if c2 <= Ncartas:
                if 0 <= f2 <= 1:
                    if f1 == 0 and f2 == 0:
                        card1 = Game_board_python1[c1]
                        card2 = Game_board_python1[c2]
                        if card1 == card2:
                            J2cards.append(card1)
                            Game_board_python1.pop(c1)
                            Game_board_python1.insert(c1," ")
                            Game_board_python1.pop(c2)
                            Game_board_python1.insert(c2," ")
                            file1.pop(c1)
                            file1.insert(c1," ")
                            file1.pop(c2)
                            file1.insert(c2," ")
                            print(J2," earn 1 point!")
                            J2score += 1
                            B = True
                            if len(J2cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:   
                                print(J2+", you keep playing! ")
                                return " "
                        else:
                            B = False
                            print("You were wrong")
                            return " "
                    elif f1 == 0 and f2 == 1:
                        card1 = Game_board_python1[c1]
                        card2 = Game_board_python2[c2]
                        if card1 == card2:
                            J2cards.append(card1)
                            Game_board_python1.pop(c1)
                            Game_board_python1.insert(c1," ")
                            Game_board_python2.pop(c2)
                            Game_board_python2.insert(c2," ")
                            file1.pop(c1)
                            file1.insert(c1," ")
                            file2.pop(c2)
                            file2.insert(c2," ")
                            print(J2," earn 1 point!")
                            J2score += 1
                            B = True
                            if len(J2cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:   
                                print(J2+", you keep playing! ")
                                return " "
                        else:
                            B = False
                            print("You were wrong")
                            return " "
                    elif f1 == 1 and f2 == 0:
                        card1 = Game_board_python2[c1]
                        card2 = Game_board_python1[c2]
                        if card1 == card2:
                            J2cards.append(card1)
                            Game_board_python2.pop(c1)
                            Game_board_python2.insert(c1," ")
                            Game_board_python1.pop(c2)
                            Game_board_python1.insert(c2," ")
                            file2.pop(c1)
                            file2.insert(c1," ")
                            file1.pop(c2)
                            file1.insert(c2," ")
                            print(J2," earn 1 point!")
                            J2score += 1
                            B = True
                            if len(J2cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:   
                                print(J2+", you keep playing! ")
                                return " "
                        else:
                            B = False
                            print("You were wrong")
                            return " "
                    elif f1 == 1 and f2 == 1:
                        card1 = Game_board_python2[c1]
                        card2 = Game_board_python2[c2]
                        if card1 == card2:
                            J2cards.append(card1)
                            Game_board_python2.pop(c1)
                            Game_board_python2.insert(c1," ")
                            Game_board_python2.pop(c2)
                            Game_board_python2.insert(c2," ")
                            file2.pop(c1)
                            file2.insert(c1," ")
                            file2.pop(c2)
                            file2.insert(c2," ")
                            print(J2," earn 1 point!")
                            J2score += 1
                            B = True
                            if len(J2cards) == Ncartas/2:
                                print("The game is over")
                                return " "
                            else:
                                print(J2+", you keep playing! ")
                                return " "
                        else:
                            B = False
                            print("You were wrong")
                            return " "
                else:
                    print("You must enter valid numbers!")
            else:
                print("You must enter valid numbers!")
        else:
            print("You must enter valid numbers!")
    else:
        print("You must enter valid numbers! ")
    return " "
            
                    

### ----------------- Tablero de la interfaz -------------------------- ###     

J1 = input("Enter the name of the first player:")
J2 = input("Enter the name of the second player: ")
Ncartas = int(input("Enter the number of pairs of cards you want to play with:"))
J1score = 0
J2score = 0
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

### ------------ bucle para partir y terminar el juego --------------- ###
A = True
while A:
    print(J1Turn(J1,Game_board_python1,Game_board_python2,J1score))
    print(J2Turn(J2,Game_board_python1,Game_board_python2,J2score))
    
### Note: At this point I did not know how to do the while, because I could not
# access the variables that I imposed in my J1Turn and J2Turn definitions.
# I no longer have time to review it.
#It is unfortunate that I could not achieve it, but I ask that you also take into 
# consideration my code and not only what is seen in the interface













