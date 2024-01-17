import numpy as np


#pos = np.array([[1,2,3], [4,5,6], [7,8,9]])
pos = np.array([["1","2","3"], ["4","5","6"], ["7","8","9"]])

class TicTacToe:
    def __init__(self):
        self.spieler_x_eingabe = ""
        self.spieler_0_eingabe = ""
        self.spielstand_x = 0
        self.spielstand_0 = 0
        self.spiel_zu_ende = False
        self.gewonnen_x = False
        self.gewonnen_0 = False
        self.pos = np.array([["1","2","3"], ["4","5","6"], ["7","8","9"]])


    def checken_sieg(self):
        for zeile in self.pos:
            alle_x = np.all(zeile == "X")
            alle_0 = np.all(zeile == "0")
            if alle_x == True:
                print("X hat gewonnen")
                self.gewonnen_x = True
                self.spiel_zu_ende = True
                break

            elif alle_0 == True:
                print("0 hat gewonnen")
                self.spiel_zu_ende = True

                break

        # Vertikal checken
        for werte in range(3):
            parallel_werte = self.pos[:, werte]
            ist_reihe_voll_x = np.all(parallel_werte == "X")
            ist_reihe_voll_0 = np.all(parallel_werte == "0")

            if ist_reihe_voll_x:
                print("X hat gewonnen")
                self.spiel_zu_ende = True
                break

            elif ist_reihe_voll_0:
                print("0 hat gewonnen")
                self.spiel_zu_ende = True

                break

        # Diagonal checken
        for wert in range(3):
            if not self.pos[wert][wert] == "X":
                break
            else:
                if wert == 2:
                    print("X hat gewonnen")
                    break

        for wert in range(3):
            if not self.pos[wert][wert] == "0":
                break
            else:
                if wert == 2:
                    print("0 hat gewonnen")

    def display_board(self):
        tic_tac_toe_bord = f"{pos[0][0]} | {pos[0][1]} | {pos[0][2]} \n" \
                           f"---------\n" \
                           f"{pos[1][0]} | {pos[1][1]} | {pos[1][2]} \n" \
                           f"---------\n" \
                           f"{pos[2][0]} | {pos[2][1]} | {pos[2][2]} \n "
        print(tic_tac_toe_bord)


    def spielstand(self):
        if self.gewonnen_x:
            self.spielstand_x += 1
            print(f"Spielstand: \n X = {self.spielstand_x}\n Y = {self.spielstand_0}")
        elif self.gewonnen_0:
            self.spielstand_0 += 1
            print(f"Spielstand: \n X = {self.spielstand_x}\n Y = {self.spielstand_0}")







def display_board():
    tic_tac_toe_bord = f"{pos[0][0]} | {pos[0][1]} | {pos[0][2]} \n" \
                       f"---------\n" \
                       f"{pos[1][0]} | {pos[1][1]} | {pos[1][2]} \n" \
                       f"---------\n" \
                       f"{pos[2][0]} | {pos[2][1]} | {pos[2][2]} \n "
    print(tic_tac_toe_bord)





spiel_zu_ende = False

while not spiel_zu_ende:
    spieler_x_eingabe = ""
    spieler_0_eingabe = ""

    spieler_x_eingabe = input("Spieler X: Geben Sie eine Zahl von 1 - 9 ein: ")


    if not spieler_x_eingabe.isdigit():
        print("Der eingegebene Wert ist nicht gültig. Versuchen Sie es nochmal")
        continue
    elif int(spieler_x_eingabe) > 9 or int(spieler_x_eingabe) < 1:
        print("Der eingegebene Wert ist nicht gültig")
        continue





    spieler_x_position = np.where(pos == spieler_x_eingabe)

    if pos[spieler_x_position] == "X" or pos[spieler_x_position] == "0":
        print("Dieses Feld ist nicht mehr zur Eingabe verfügbar. Versuchen Sie es mit einem anderen")
        continue


    pos[spieler_x_position] = "X"
    display_board()

    #Horizontal checken
    for zeile in pos:
        alle_x = np.all(zeile == "X")
        alle_0 = np.all(zeile == "0")
        if alle_x == True:
            print("X hat gewonnen")
            spiel_zu_ende = True
            break

        elif alle_0 == True:
            print("0 hat gewonnen")
            spiel_zu_ende = True

            break

    #Vertikal checken
    for werte in range(3):
        parallel_werte = pos[:, werte]
        ist_reihe_voll_x = np.all(parallel_werte == "X")
        ist_reihe_voll_0 = np.all(parallel_werte == "0")

        if ist_reihe_voll_x:
            print("X hat gewonnen")
            spiel_zu_ende = True

            break

        elif ist_reihe_voll_0:
            print("0 hat gewonnen")
            spiel_zu_ende = True

            break

    #Diagonal checken
    for wert in range(3):
        if not pos[wert][wert] == "X":
            break
        else:
            if wert == 2:
                print("X hat gewonnen")
                break

    for wert in range(3):
        if not pos[wert][wert] == "0":
            break
        else:
            if wert == 2:
                print("0 hat gewonnen")

    spieler_0_eingabe = input("Spieler 0: Geben Sie eine Zahl von 1 - 9 ein: ")

    if not spieler_x_eingabe.isdigit():
        print("Der eingegebene Wert ist nicht gültig. Versuchen Sie es nochmal")
        continue
    elif int(spieler_x_eingabe) > 9 or int(spieler_x_eingabe) < 1:
        print("Der eingegebene Wert ist nicht gültig")
        continue

    spieler_0_position = np.where(pos == spieler_0_eingabe)
    pos[spieler_0_position] = "0"
    display_board()

    # Horizontal checken
    for zeile in pos:
        alle_x = np.all(zeile == "X")
        alle_0 = np.all(zeile == "0")
        if alle_x:
            print("X hat gewonnen | Reihe vollendet")
            spiel_zu_ende = True

            break

        elif alle_0:
            print("0 hat gewonnen")
            spiel_zu_ende = True

            break

    # Vertikal checken
    for werte in range(3):
        parallel_werte = pos[:, werte]
        ist_reihe_voll_x = np.all(parallel_werte == "X")
        ist_reihe_voll_0 = np.all(parallel_werte == "0")

        if ist_reihe_voll_x:
            print("X hat gewonnen | Spalte vollendet")
            spiel_zu_ende = True

            break

        elif ist_reihe_voll_0:
            print("0 hat gewonnen")
            spiel_zu_ende = True
            break

    """for werte in range(3):
        print(pos[werte][werte])
        diagonal_werte = pos[werte][werte]
        diagonal_x = np.all(diagonal_werte == "X")
        diagonal_0 = np.all(diagonal_werte == "0")
        if diagonal_x:
            print("X hat gewonnen | Diagonale vollendet")
            spiel_zu_ende = True
            break
        elif diagonal_0:
            print("0 hat gewonnen")
            spiel_zu_ende = True
            break"""
    # Diagonal checken
    for wert in range(3):
        if not pos[wert][wert] == "X":
            break
        else:
            if wert == 2:
                print("X hat gewonnen")
                break

    for wert in range(3):
        if not pos[wert][wert] == "0":
            break
        else:
            if wert == 2:
                print("0 hat gewonnen")
                break







