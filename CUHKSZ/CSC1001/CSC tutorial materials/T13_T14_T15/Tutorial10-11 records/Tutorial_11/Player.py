from Board import Board

# Player
class Player(object):
    def __init__(self, take='X'):
        self.take=take
    
    def think(self, board):
        pass
        
    def move(self, board, action):
        board._move(action, self.take)


# Human Player
class HumanPlayer(Player):
    def __init__(self, take):
        super().__init__(take)
    
    def think(self, board):
        while True:
            action = input('Please input a num in 0-8:')
            if len(action)==1 and action in '012345678' and board.is_legal_action(int(action)):
                return int(action)


# AI Player
class AIPlayer(Player):
    def __init__(self, take):
        super().__init__(take)
    
    def think(self, board):
        print('AI is thinking ...')
        take = ['X','O'][self.take=='X']
        player = AIPlayer(take)     # imagined player
        val, action = self.minimax(board, player)
        return action
        
    # search the action with minimum moving steps for wining
    def minimax(self, board, player, depth=0) :
        if self.take == "O": 
            bestVal = -10
        else:
            bestVal = 10

        # when the game is over, return the depth of move (move steps) 
        if board.teminate() :
            if board.get_winner() == 0 :
                return -10 + depth, None
            elif board.get_winner() == 1 :
                return 10 - depth, None
            elif board.get_winner() == 2 :
                return 0, None
            
        # go through all legal actions and find out the best action with least moving steps to win
        for action in board.get_legal_actions() : 
            board._move(action, self.take)
            val, playeraction = player.minimax(board, self, depth+1) # switch to another player's next move
            board._unmove(action) # unmove back to last step when recursion is completed

            # compare val(best move from recursion) and bestVal(current best move)
            if self.take == "O" :
                if val > bestVal:
                    bestVal, bestAction = val, action
            else :
                if val < bestVal:
                    bestVal, bestAction = val, action
        
        return bestVal, bestAction

