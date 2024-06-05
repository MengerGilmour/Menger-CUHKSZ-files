class Board(object):
    def __init__(self):
        self._board = ['-' for i in range(9)]
        self._history = [] 
        
    # move pieces
    def _move(self, action, take):
        if self._board[action] == '-':
            self._board[action] = take          
            self._history.append((action, take)) 
            
    # unmove pieces
    def _unmove(self, action):
        self._board[action] = '-'     
        self._history.pop()
        
    # Get all legal action in next step, you can move on those positions marked with '-'
    def get_legal_actions(self):
        actions = []
        for i in range(9):
            if self._board[i] == '-':
                actions.append(i)
        return actions
        
    # Check current move is legal or not 
    def is_legal_action(self, action):
        return self._board[action] == '-'
        
    # Check whether game is over
    def teminate(self):
        board = self._board
        lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
        
        if ['X']*3 in lines or ['O']*3 in lines or '-' not in board:
            return True 
        else:
            return False
            
    # Check which player is winner
    def get_winner(self):
        board = self._board
        lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
        
        if ['X']*3 in lines:
            return 0 
        elif ['O']*3 in lines:
            return 1 
        else:
            return 2
            
    # print chessboard
    def print_b(self):
        board = self._board
        for i in range(len(board)):
            print(board[i], end='')
            if (i+1)%3 == 0:
                print()
    
    # print the history of every move during the game
    def print_history(self):
        print(self._history)


