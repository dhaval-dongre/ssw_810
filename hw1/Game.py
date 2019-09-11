from random import choice

class Game:

    def __init__(self, x):
        self.playersMove=x

    def computeMove(self):
        return choice(['r', 'p', 's'])

    def logic(self):
        computer=self.computeMove()
        if self.playersMove not in ['r','p','s','q']:
            return False
        if self.playersMove == computer:
                print("Tie!")
        elif self.playersMove == "r":
            if computer == "p":
                print("You lose! Computer has Paper!")
            else:
                print("You win! Computer has Scissors!")
        elif self.playersMove == "p":
            if computer == "s":
                print("You lose! Computer has Scissors!")
            else:
                print("You win! Computer has Rock!")
        elif self.playersMove == "s":
            if computer == "r":
                print("You lose! Computer has Rock!")
            else:
                print("You win! Computer has Paper!")
        elif self.playersMove=='q':
            print("Exiting game!")
            SystemExit()        
        return True    

