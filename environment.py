WIN  =  512
LOSE =  -WIN

#self.board environment class
class Board(object):
    """ Game Environment Class"""
    
    def __init__(self, board=[]):
        """ Initialize the environment variables """
        # Generate a newself.board if the passedself.board is empty
        if len(board) == 0:
            self.board = [[' ' for row in range(6)] for column in range(7)]

        # Set newself.board as oldself.board
        else:
            self.board = self.board

        self.width = 7
        self.height = 6

    def __str__(self):
        """ Return the board"""
        string = ''
        # Print Column numbers
        string += "\ 1 2 3 4 5 6 7\n"

        # 0-5 (6 Rows)
        for row in range(6):
            # Print Row number
            string += str(row+1) + ' '
            # 0-6 (7 Columns)
            for column in range(7):
                # Print Square at index [Column][Row]
                string += self.board[column][row] + ' '
            # New line
            string += '\n'
        return string

    def legal_moves(self):
        """ Get the empty spaces """
        return self.get_columns(' ')

    def leaf(self):
        """ Is theself.board full or has someone won the game """
        if self.full():
            return True
        if self.winner() != None:
            return True
        return False

    def full(self):
        for column in range(self.width):
            if self.board[column][0] == ' ':
                return False
        return True

    def X_won(self):
        """ Did player X win """
        return self.winner() == 'X'

    def O_won(self):
        """ Did player O win """
        return self.winner() == 'O'

    def tied(self):
        """ Is the game a tie? """
        return self.leaf() == True and self.winner() is None

    def score(self, one, two, three, four, man):
        o_man = get_opponent(man)
        score = 0
        if(one != o_man and two != o_man and three != o_man and four != o_man):
                    count = 0
                    if one == man:
                        count += 1
                    if two == man:
                        count += 1
                    if three == man:
                        count += 1
                    if four == man:
                        count += 1
                  
                    if count == 4:
                        score += WIN
                    elif count == 3:
                        score += 50
                    elif count == 2:
                        score += 10
                    elif count == 1:
                        score += 1
        return score

    def evaluate(self, man):
        o_man = get_opponent(man)
        score = 0
        for column in range(self.width):
            for row in range(self.height):
                # Horizonatal - evaluation
                try:
                    t_score = self.score(self.board[column][row], self.board[column+1][row], self.board[column+2][row], self.board[column+3][row], man)
                    if t_score >= WIN:
                        return WIN
                    score += t_score
                    t_score = self.score(self.board[column][row], self.board[column+1][row], self.board[column+2][row], self.board[column+3][row], o_man)
                    if t_score >= WIN:
                        return LOSE
                    score -= t_score
                except:
                    pass
                # Vertical | evaluation
                try:
                    t_score = self.score(self.board[column][row], self.board[column][row+1], self.board[column][row+2], self.board[column][row+3], man)
                    if t_score >= WIN:
                        return WIN
                    score += t_score
                    t_score = self.score(self.board[column][row], self.board[column][row+1], self.board[column][row+2], self.board[column][row+3], o_man)
                    if t_score >= WIN:
                        return LOSE
                    score -= t_score
                except:
                    pass
                # Diagonal \ evaluation
                try:
                    t_score = self.score(self.board[column][row], self.board[column+1][row+1], self.board[column+2][row+2], self.board[column+3][row+3], man)
                    if t_score >= WIN:
                        return WIN
                    score += t_score
                    t_score = self.score(self.board[column][row], self.board[column+1][row+1], self.board[column+2][row+2], self.board[column+3][row+3], o_man)
                    if t_score >= WIN:
                        return LOSE
                    score -= t_score

                except:
                    pass
                # Diagonal / evaluation
                try:
                    t_score = self.score(self.board[column][row], self.board[column-1][row+1], self.board[column-2][row+2], self.board[column-3][row+3], man)
                    if t_score >= WIN:
                        return WIN
                    score += t_score
                    t_score = self.score(self.board[column][row], self.board[column-1][row+1], self.board[column-2][row+2], self.board[column-3][row+3], o_man)
                    if t_score >= WIN:
                        return LOSE
                    score -= t_score
                except:
                    pass
        if man == 'O':
            score += 16
        else:
            score -= 16
        return score
                
    def winner(self):
        """ Get the winner of the board """
        score = self.evaluate('X')
        if score >= WIN:
            return 'X'
        elif score <= LOSE:
            return 'O'
        else:
            return None

    def get_columns(self, player):
        """ Get a list of all squares taken by a certain player """
        return [column for column in range(self.width) if self.board[column][0] == player]

    def move(self, column, player, delete=False):
        """ Move player to position """
        # Get Row to play at
        for row in range(self.height):
            if self.board[column][row] != ' ':
                if not(delete):
                    row -= 1
                break

        # Set Square at index [column-1][row-1] to passed Square value
        #print("Column: ",column+1," Row: ",row+1)
        self.board[column][row] = player

def get_opponent(player):
    """ Gives us the opponent of player """
    if player == 'O':
        return 'X'
    else:
        return 'O'
