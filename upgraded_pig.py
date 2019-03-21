#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A classic game of Pig"""

import random
import time

def addPlayers(players):
    for num in range(players):
        name = 'player' + str(num+1)
        player_list.append(name)

        
class Dice:
    
    def roll_dice(self):
        return random.randint(1, 6)
    
    def add_score(self, turntotal):
        self.score += turntotal

        
class Player(Dice):
    
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return '%s has a total score of %s.' %(self.name, str(self.score))

class Computer(Player):
    
    def __init__(self, name, score=0):
        Player.__init__(self, name, score=score)

    def action(self, turn_total):
        print 'The turn total is %d.'%turn_total
        if turn_total <= 25:
            if 100 - self.score >= turn_total:
                return 'r'
            else:
                return 'h'
        else:
            return 'h'
    
class Game():
    
    def runGame(self):
        winner = True

        while winner:
            for players in object_player:
                choice = 'r'
                turn_total = 0
                print(players)

                while choice != 'h':
                    die = Dice()
                    face_number = die.roll_dice()

                    if face_number == 1:
                        print '%s rolled a 1 and lost the turn.' %players.name
                        turn_total = 0
                        break
            
                    elif 1 < face_number < 6:
                        turn_total += face_number
                        print '%s rolled a %d, and the turn total is %d.'%(players.name, face_number, turn_total)
                        if players.name == 'computer':
                            choice = players.action(turn_total)
                        else:
                            choice = raw_input("Enter 'r' to roll or 'h' to hold: ")
                    
                players.add_score(turn_total)
        
                print players, '\n'

                if players.score >= 100:
                    print '%s has won the game with a score of %d' %(players.name, players.score)
                    winner = False
                    break

        
if __name__ == '__main__':
    num = int(raw_input('Please enter number of players: '))
    player_list = []
    object_player = []
    addPlayers(num)
    game = Game()
    
    for items in player_list:
        players = Player(items)
        object_player.append(players)
        
    if num >= 2:
        game.runGame()
        
    else:
        computer = Computer('computer')
        object_player.append(computer)
        game.runGame()

            
        








            
            
