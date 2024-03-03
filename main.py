from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for row in board:

        print(
                f'''
+-------+-------+-------+
|       |       |       |
|   {row[0]}   |   {row[1]}   |   {row[2]}   |
|       |       |       |''',
                end='',
        )
    
    print(
'''
+-------+-------+-------+'''
)
            


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    try:
        field = int(input('Introduce el número de la casilla que deseas marcar: '))
    except ValueError:
        print("Ese no es un número válido.")
        enter_move(board)

    if field < 1 or field > 9:
        print("El número debe estar entre 1 y 9.")
        enter_move(board)


    list_of_free_fields = make_list_of_free_fields(board)
    dictionary_of_free_fields = {}

    for i in range(len(list_of_free_fields)):
        row, col = list_of_free_fields[i]
        dictionary_of_free_fields[board[row][col]] = list_of_free_fields[i]
        
    if field not in dictionary_of_free_fields.keys():
        print("Esta casilla ya ha sido ocupada.")
        enter_move(board)
    else:
        row, col =  dictionary_of_free_fields[field]
        board[row][col] = 'O'

    display_board(board)


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_of_free_fields = []

    for row in board:
        for field in row:
            if isinstance(field, int):
                list_of_free_fields.append((board.index(row), row.index(field)))

    return list_of_free_fields

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    
    for i in range(len(board)):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
        
        if i == 0 and board[i][i] == sign and board[i + 1][i + 1] == sign and  \
            board[i + 2][i + 2] == sign:
            return True
        
        if i == 0 and board[i][i + 2] == sign and board[i + 1][i + 1] == sign and \
            board[i + 2][i] == sign:
            return True

def check_victory(board):
    if victory_for(board, 'X'):
        print('Has perdido este juego. Lo siento.')
        return True

    if victory_for(board, 'O'):
        print('¡Felicitaciones! Has ganado el juego.')
        return True

    if not victory_for(board, 'X') and not victory_for(board, 'O') and \
        len(make_list_of_free_fields(board)) == 0:
        print('El juego ha terminado en empate.')
        return True
    
    return False

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    list_of_free_fields = make_list_of_free_fields(board)

    field_to_fill = randrange(len(list_of_free_fields))

    row, col = list_of_free_fields[field_to_fill]

    board[row][col] = 'X'

    display_board(board)

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]



display_board(board)

while True:
    enter_move(board)

    if check_victory(board): break

    draw_move(board)

    if check_victory(board): break
