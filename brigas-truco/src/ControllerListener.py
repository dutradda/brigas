'''
Created on 02/06/2009

@author: Vitor Normande
'''
from Controller import Controller

# This Python file uses the following encoding: utf-8

class ControllerListener(object):
    '''
    This is the listener for the game's controller.
    '''

    def __init__(self):
        self.__controller = Controller()

    def player_throw_card(self, player_id, card):
        '''
        throw - card thrown by the player
              
        @param player_id: player identifier
        @param card: card thrown
               
        @type  player_id: str
        @type  card: int
        '''
        
        self.__controller.throw_card(player_id, card)

    def player_asks_truco(self, player_id):
        '''
        asks for Truco
         
        @param player_id: asking player
                
        @type  player_id: str
        '''
            
        self.__controller.truco(player_id)

    def player_accepts_truco(self, player_id):
        '''
        accept Truco
           
        @param player_id: player who accept
            
        @type  player_id: str
        '''
            
        self.__controller.accept_truco(player_id)
    
    def player_give_up(self, player_id):
        '''
        quit the game
          
        @param player_id: dropout player
               
        @type  player_id: str
        '''
            
        self.__controller.give_up_of_hand(player_id)

