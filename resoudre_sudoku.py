from typing import List

def grille_valide(board: List[List[str]]) -> bool:
    """
    Cette fonction vérifie si une grille de Sudoku est valide en vérifiant les lignes, les colonnes
    et les sous-grilles 3x3 pour s'assurer qu'elles contiennent uniquement des chiffres de 1 à 9.
    """
    # Vérifier les lignes
    for i in range(len(board)):
        lst = [] 
        for j in range(len(board)):
            if board[i][j] != "." :
                if board[i][j] not in lst :
                    lst.append(board[i][j])
                else :
                    return False

    # Vérifier les colonnes
    for i in range(len(board)):
        lst = [] 
        for j in range(len(board)):
            if board[j][i] != "." :
                if board[j][i] not in lst :
                    lst.append(board[j][i])
                else :
                    return False 

    # Vérifier les sous-grilles 3x3
    for a in range (0,9,3): # Décaler la colonne
        
        for b in range(0,9,3): # Décaler la ligne
            lst=[] # Réinitialiser la liste
            for c in range(a,a+3): # Indexer les lignes
                for d in range(b,b+3): # Indexer les colonnes
                    if board[c][d] != ".": 
                        if board[c][d] not in lst:
                            lst.append(board[c][d])
                        else:
                            return False 

    # Si toutes les vérifications ont réussi, la grille est valide
    return True



def solveSudoku(board: List[List[str]]) -> List[List[str]]:
    # Trouver une case vide
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                # Essayer chaque nombre possible dans cette case
                for k in range(1, 10):
                    board[i][j] = str(k)
                    if grille_valide(board):
                        if solveSudoku(board):
                            return True # on peut le remplace par board pour voir le resultat 
                # Aucun nombre n'a fonctionné, donc on doit revenir en arrière
                board[i][j] = "."
                return False 
    
    # Vérifier si la grille est valide avant de la retourner
    if grille_valide(board):
        return True
    else:
        return False






if __name__ == "__main__":
    # Ecrire vos tests ici ! Vous pouvez utiliser les plateaux fournis pour éviter de les réécrire

    board_easy = [
        [".", ".", ".", "3", ".", "2", ".", ".", "."],
        [".", ".", ".", "8", "1", ".", ".", "4", "2"],
        [".", "9", ".", ".", ".", ".", "3", ".", "."],
        ["3", ".", "7", "6", "9", "8", "1", "2", "."],
        ["1", ".", "6", "2", ".", "5", "4", "7", "9"],
        ["5", ".", "9", ".", "4", ".", ".", ".", "."],
        [".", "1", ".", ".", ".", "6", ".", "9", "3"],
        [".", "6", "4", ".", ".", ".", "2", "5", "."],
        [".", ".", "2", ".", "8", ".", ".", ".", "."]
    ]


    board_medium_1 = [
        [".", ".", "4", ".", "1", ".", ".", ".", "3"],
        [".", ".", "7", ".", ".", ".", "9", ".", "5"],
        [".", "1", "3", ".", ".", "8", "4", ".", "."],
        [".", ".", ".", "8", "6", "5", ".", "3", "2"],
        [".", ".", "2", "3", ".", ".", ".", ".", "8"],
        [".", ".", "8", ".", ".", "9", ".", "6", "."],
        [".", "4", ".", ".", ".", "6", "8", "7", "1"],
        [".", ".", ".", ".", ".", "1", ".", ".", "."],
        ["8", ".", "1", ".", "4", ".", ".", ".", "."]
    ]

    board_medium_2 = [
        [".", ".", "4", "6", ".", ".", ".", "3", "."],
        [".", "5", ".", "8", "3", "1", ".", ".", "9"],
        [".", "1", "3", ".", ".", ".", ".", "2", "7"],
        ["1", "9", "6", "2", ".", ".", ".", ".", "3"],
        [".", "4", ".", ".", "9", ".", ".", ".", "."],
        [".", "3", ".", ".", "5", "7", ".", ".", "."],
        [".", ".", ".", ".", ".", "5", "9", ".", "2"],
        ["5", "6", ".", "9", ".", "8", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "1", ".", "."],
    ]

    board_hard = [
        ["9", ".", ".", ".", ".", ".", ".", ".", "3"],
        [".", ".", "8", "7", ".", ".", ".", ".", "."],
        [".", "6", ".", ".", "4", ".", "2", "9", "."],
        [".", "9", ".", ".", "2", ".", "5", "4", "."],
        [".", ".", ".", ".", ".", ".", ".", "1", "."],
        ["6", ".", ".", ".", ".", "9", ".", ".", "."],
        [".", "5", ".", ".", ".", ".", ".", ".", "1"],
        ["7", ".", ".", "4", ".", ".", "3", "5", "."],
        [".", ".", ".", ".", "3", ".", ".", ".", "6"]
    ]

    # print(solveSudoku(board_easy))
    
    assert solveSudoku(board_easy) == True 
    print("board_easy validée ! ✔")

    assert solveSudoku(board_medium_1) == True
    print("board_medium_1 ! ✔")

    assert solveSudoku(board_medium_2) == True
    print("board_medium_2 validée ! ✔")

    assert solveSudoku(board_hard) == True 
    print("board_hard validée ! ✔")
   