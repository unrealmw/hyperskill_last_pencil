"""Simple game - Pencils. It is playing with bot. Jack is always bot.
Who takes the last pencil lost this game."""

import random


class Pencils:

    moves = []  # moves list
    player = "John"    # players names
    bot = "Jack"

    def __init__(self,  pencils):
        
        """initiating class with number of pencils"""
        
        self.pencils_number = pencils

    def pencils_printer(self):
        
        """Printing pencils buy their class number"""
        
        print("|" * self.pencils_number)

    @staticmethod
    def input_pencils():
        
        """This method check number of pencils. Number must be integer and real!"""
        
        print("How many pencils would you like to use:")
        while True:
            pencils = input()
            if not pencils.isdigit() or "-" in pencils:
                print("The number of pencils should be numeric")
            elif pencils.isdigit():
                if int(pencils) <= 0:
                    print("The number of pencils should be positive")
                    continue
                else:
                    break
        return int(pencils)

    def first_move(self):
        
        """Gives user to choose who will go first John - player or Jack - bot."""
        
        print(f"Who will be the first ({self.player}, {self.bot}):")
        while True:
            name = input()
            if name == self.player:
                self.moves.append(self.player)
                break
            elif name == self.bot:
                self.moves.append(self.bot)
                break
            else:
                print(f"Choose between 'John' and 'Jack'")

    def turn_to_move(self):
        
        """Gets from moves list players name, then takes a by player and after that writes 
        opponents name to moves list"""
        
        if self.moves[-1] == self.player:
            print(f"{self.player}'s turn:")
            self.players_move()
            self.moves.append(self.bot)
        else:
            print(f"{self.bot}'s turn:")
            self.bots_move()
            self.moves.append(self.player)

    def players_move(self):
        
        """Makes move by player. Takes input and checks it, it must be numeric from 1 to 3."""
        
        while True:
            try:
                num = int(input())
                if num > 3 or num <= 0:
                    print("Possible values: '1', '2' or '3'")
                    continue
                elif num > self.pencils_number:
                    print("Too many pencils were taken")
                    continue
                else:
                    self.pencils_number -= num
                    break
            except ValueError:
                print("Possible values: '1', '2' or '3'")
                continue

    def bots_move(self):
        
        """Makes move by bot according to winning strategy."""
        
        if self.pencils_number % 4 == 0:
            print("3")
            self.pencils_number -= 3
        elif self.pencils_number % 4 == 3:
            print("2")
            self.pencils_number -= 2
        elif self.pencils_number % 4 == 2:
            print("1")
            self.pencils_number -= 1
        elif self.pencils_number % 4 == 1 and self.pencils_number != 1:
            bot_move = random.randint(1, 3)
            print(bot_move)
            self.pencils_number -= bot_move
        elif self.pencils_number == 1:
            print("1")
            self.pencils_number -= 1

    def print_winner(self):
        
        """Prints winners name"""
        
        print(self.moves[-1], "won!")


def main():
    pencil_number = Pencils.input_pencils()
    game = Pencils(pencil_number)
    game.first_move()
    while game.pencils_number > 0:
        game.pencils_printer()
        game.turn_to_move()
    game.print_winner()


if __name__ == '__main__':
    main()

