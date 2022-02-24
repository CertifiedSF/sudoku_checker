#badSudoku = [[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
#workingSudoku = [[1,4,7,9,3,6,5,8,2],[2,5,8,1,4,7,6,9,3],[3,6,9,2,5,8,1,7,4],[7,1,4,6,9,3,2,5,8],[8,2,5,7,1,4,3,6,9],[9,3,6,8,2,5,4,1,7],[4,7,1,3,6,9,8,2,5],[5,8,2,4,7,1,9,3,6],[6,9,3,5,8,2,7,4,1]]
#   These were used for testing

def rivinOikeellisuus(matriisi: list):  # Checks the ROWS.
    for i in matriisi:
        vali = []
        for j in i:
            if j not in vali:
                vali.append(j)
            else:
                return False
    return True

def sarakkeenOikeellisuus(matriisi: list):  # Checks the COLUMNS.
    for i in matriisi:
        vali = []
        for j in range(0,9):
            if i[j] not in vali:
                vali.append(i[j])
            else:
                return False
    return True

def osaOikeellisuus(matriisi: list):    # Checks the 3x3 SQUARES.
    kaikki_ruudut = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            ruutu = []
            for k in range(i,i+3):
                for l in range(j,j+3):
                    ruutu.append(matriisi[k][l])
            kaikki_ruudut.append(ruutu)
    for i in kaikki_ruudut:
        nrot = []
        for j in range(1,9):
            if i[j] not in nrot:
                nrot.append(i[j])
            else:
                return False
    return True

def sudokuOikeellisuus(matriisi: list):     # Checks all at once.
    if rivinOikeellisuus(matriisi) and sarakkeenOikeellisuus(matriisi) and osaOikeellisuus(matriisi):
        print("Sudoku on laillinen.")
    else:
        print("Sudoku on laiton.")

def tulostaSudoku(matriisi: list):      # Prints the sudoku
    for i in matriisi:
        print(i)

#   Here you pick a .txt file with a sudoku by writing it's name.
print("toimivaSudoku.txt, riviJaSarakeSudoku.txt, huonoSudoku.txt")     # Just pre-existing ones for testing
tiedostoNimi = input("Anna tiedoston nimi: ")
with open(tiedostoNimi) as sudoku:
    strMatriisi = []
    for rivi in sudoku:
        strMatriisi.append(rivi.strip().split(","))
    sudokuMatriisi = []
    for i in strMatriisi:
        sudokuMatriisi.append(list(map(int, i)))

        #   Shows the sudoku and what parts of it are acceptable.
    tulostaSudoku(sudokuMatriisi)
    print("Rivin oikeellisuus: ", rivinOikeellisuus(sudokuMatriisi))
    print("Sarakkeen oikeellisuus: ", sarakkeenOikeellisuus(sudokuMatriisi))
    print("3x3 ruutujen oikeellisuus: ", osaOikeellisuus(sudokuMatriisi))
    sudokuOikeellisuus(sudokuMatriisi)
