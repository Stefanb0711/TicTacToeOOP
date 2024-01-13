import pandas as pd
import numpy as  np

#pos = [1,2,3,4,5,6,7,8,9]


"""tic_tac_toe_bord = f"{pos[0]} | {pos[1]} | {pos[2]} \n"\
                        f"---------\n"\
                       f"{pos[3]} | {pos[4]} | {pos[5]} \n" \
                       f"---------\n" \
                        f"{pos[6]} | {pos[7]} | {pos[8]} \n "

tic_tac_toe_data = {
    "Zeile_1": [pos[0], pos[1], pos[2]],
    "Zeile_2": [pos[3], pos[4], pos[5]],
    "Zeile_3": [pos[6], pos[7], pos[8]]
}

df_tic_tac_toe = pd.DataFrame(tic_tac_toe_data)

df_tic_tac_toe = df_tic_tac_toe.reset_index(drop=True)

#df_tic_tac_toe.iloc[0].all()
"""

pos = np.array([[1,2,3], [4,5,6], [7,8,9]])

tic_tac_toe_bord = f"{pos[0][0]} | {pos[0][1]} | {pos[0][2]} \n"\
                        f"---------\n"\
                       f"{pos[1][0]} | {pos[1][1]} | {pos[1][2]} \n" \
                       f"---------\n" \
                        f"{pos[2][0]} | {pos[2][1]} | {pos[2][2]} \n "


spielfeld = f"{pos[0][0]} | {pos[0][1]} | {pos[0][2]} \n"\
                        f"---------\n"\
                       f"{pos[1][0]} | {pos[1][1]} | {pos[1][2]} \n" \
                       f"---------\n" \
                        f"{pos[2][0]} | {pos[2][1]} | {pos[2][2]} \n "


"""
for werte in range(3):
    print(pos[:, werte])

print("\n")

for werte in range(3):
    print(pos[werte])

print("\n")
"""


print("\n")


"""
for werte in range(3):
    print(pos[werte][werte])
    diagonal_werte = pos_bsp[werte][werte]
    diagonal_x = np.all(diagonal_werte == "X")
    diagonal_0 = np.all(diagonal_werte == "0")
    if diagonal_x:
        print("X hat gewonnen")
    elif diagonal_0:
        print("0 hat gewonnen")

for werte in range(3):
    parallel_werte = pos_bsp[:, werte]
    sind_alle_par_werte_gleich = np.all(parallel_werte == parallel_werte[0])
    if sind_alle_par_werte_gleich:
        if parallel_werte[0] == "X":
            print("X hat gewonnen")
            break
        else if parallel_werte[0] == "0":
            print("0 hat gewonnen")
            break


for werte in range(3):
    parallel_werte = pos_bsp[:, werte]
    ist_reihe_voll_x = np.all(parallel_werte == "X")
    ist_reihe_voll_0 = np.all(parallel_werte == "0")

    if ist_reihe_voll_x:
        print("X hat gewonnen")
        break

    elif ist_reihe_voll_0:
        print("0 hat gewonnen")
        break
"""



#are_all_first_values_equal = np.all(first_values == first_values[0])
#print(are_all_first_values_equal)


#Schauen ob alle werte im subarray gleich sind
"""sub_array = pos_bsp[1, :]

alle_gleich = np.all(sub_array == sub_array[1])

if alle_gleich:
    print("Alle gleich")
else:
    print("Alle nicht gleich")
"""


#Suchen nach einem bestimmten Wert
"""search_value = 7

indices = np.where(pos_bsp == search_value)
print(indices)"""

"""
search_value = "7"
pos_bsp[pos_bsp == search_value] = "X"

print(pos_bsp)
"""
pos_bsp = np.array([["X","2","3"], ["4","5","6"], ["7","8","X"]])

for wert in range(3):
    if not pos[wert][wert] == "X":
        break
    else:
        if wert == 2:
            print("X hat gewonnen")

for wert in range(3):
    if not pos[wert][wert] == "0":
        break
    else:
        if wert == 2:
            print("0 hat gewonnen")



"""
for wert in range(3):
    diagonal_werte = pos_bsp[wert][wert]


print(diagonal_werte)
diagonal_x = np.all(diagonal_werte == "X")
diagonal_0 = np.all(diagonal_werte == "0")
if diagonal_x:
    print("X hat gewonnen | Diagonale vollendet")

elif diagonal_0:
    print("0 hat gewonnen")
"""