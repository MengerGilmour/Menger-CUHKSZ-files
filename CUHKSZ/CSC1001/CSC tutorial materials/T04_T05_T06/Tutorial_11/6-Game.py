from Board import Board
from Player import *

# Game
class Game(object):
    def __init__(self):
        self.board = Board()
        self.current_player = None
        
    # Generate player
    def mk_player(self, p, take='X'): # p in [0,1]
        if p==0:
            return HumanPlayer(take)
        else:
            return AIPlayer(take)
            
    # Switch player
    def switch_player(self, player1, player2):
        if self.current_player is None:
            return player1
        else:
            return [player1, player2][self.current_player == player1]
            
    # Print winner
    def print_winner(self, winner): # winner in [0,1,2]
        print(['Winner is player1','Winner is player2','Draw'][winner])

    # Run the game
    def run(self):
        ps = input("Please select two player's type:\n\t0.Human\n\t1.AI\nSuch as:0 0\n")
        p1, p2 = [int(p) for p in ps.split(' ')]
        player1, player2 = self.mk_player(p1, 'X'), self.mk_player(p2, 'O') 
        
        print('\nGame start!\n')
        self.board.print_b() 
        while True:
            self.current_player = self.switch_player(player1, player2)            
            action = self.current_player.think(self.board)           
            self.current_player.move(self.board, action)

            #After player determines the move action, print the board
            self.board.print_b() 

            # After every move, check whether the game is over, if yes, get the winner and terminate the game 
            if self.board.teminate(): 
                winner = self.board.get_winner() 
                break
        
        self.print_winner(winner)
        print('Game over!')
        
        self.board.print_history()
    
    
def main():
    game = Game()
    game.run()

main()
