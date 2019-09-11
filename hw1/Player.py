from Game import Game

class Player:

    def __init__(self,x):
        self.x=x

    def move(self):
        g=Game(self.x)
        return g.logic()

if __name__ == "__main__":
        ip=input("Please choose 'R', 'P', 'S' or 'Q' to quit:")
        playersMove=Player(ip.lower())

        while not playersMove.move():
            ip=input("\nPlease enter a valid input! \n\nPlease choose 'R', 'P', 'S' or 'Q' to quit:")
            Player(ip.lower()).move()