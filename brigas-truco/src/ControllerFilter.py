'''
Created on 18/06/2009

@author: Vitor Normande
'''

from Card import Card
from Dealer import Dealer
from Double import Double
from Player import Player

class ControllerFilter(object):
    '''
    Filter of controller
    '''
    
    def _args_to_string(self, *args):
        '''
        Transform args into unique string
              
        @param *args: list of arguments
                 
        @type  *args: tuple
            
        @rtype: str
        '''
            
        list = [self._room_id]
        for arg in args:
            list += [arg]
            
        return  ':'.join(str(arg) for arg in list)
    
    def __init__(self, room_id):
        self._room_id = room_id
        pass
    #
    #All the methods transform its arguments into string using the method _args_to_string 
    #
   
    def match_started(self,player1, player2, player3, player4):
        return self._args_to_string(player1.id,
                                           player2.id,
                                    player3.id,
                                    player4.id)
    
    def hand_started(self, card_vira,player1, player2, player3, player4):
        player1_cards = player1.get_cards()
        player2_cards = player2.get_cards()
        player3_cards = player3.get_cards()
        player4_cards = player4.get_cards()
        
        return self._args_to_string(card_vira.card_id,
                                    player1.id, 
                                    player1_cards[0].card_id,
                                    player1_cards[1].card_id, 
                                    player1_cards[2].card_id,
                                    player2.id, 
                                    player2_cards[0].card_id,
                                    player2_cards[1].card_id, 
                                    player2_cards[2].card_id,
                                    player3.id, 
                                    player3_cards[0].card_id,
                                    player3_cards[1].card_id, 
                                    player3_cards[2].card_id,
                                    player4.id, 
                                    player4_cards[0].card_id,
                                    player4_cards[1].card_id, 
                                    player4_cards[2].card_id)
        
    def turn_started(self, player):
        return self._args_to_string(player.id)

    def card_played(self, player_id, card_id):
        return self._args_to_string(player_id, card_id)

    def truco_asked(self, player_id):
        return self._args_to_string(player_id)

    def truco_accepted(self, player_id, truco_value):
        return self._args_to_string(player_id, truco_value)

    def gave_up(self, player_id):
        return self._args_to_string(player_id)
    
    def eleven_hand(self, player1, player2):
        player1_cards = player1.get_cards()
        player2_cards = player2.get_cards()
                
        return self._args_to_string(player1.id,
                                    player1_cards[0].card_id,
                                    player1_cards[1].card_id,
                                    player1_cards[2].card_id,
                                    player2.id,
                                    player2_cards[0].card_id, 
                                    player2_cards[1].card_id,
                                    player2_cards[2].card_id)
        
    def iron_hand(self, player1, player2, player3, player4):
        player1_cards = player1.get_cards()
        player2_cards = player2.get_cards()
        player3_cards = player3.get_cards()
        player4_cards = player4.get_cards()
        
        return self._args_to_string(player1.id,
                                    player1_cards[0].card_id,
                                    player1_cards[1].card_id,
                                    player1_cards[2].card_id,
                                    player2.id,
                                    player2_cards[0].card_id, 
                                    player2_cards[1].card_id,
                                    player2_cards[2].card_id,
                                    player3.id,
                                    player3_cards[0].card_id,
                                    player3_cards[1].card_id,
                                    player3_cards[2].card_id,
                                    player4.id,
                                    player4_cards[0].card_id, 
                                    player4_cards[1].card_id,
                                    player4_cards[2].card_id)
    
    def match_finished(self, double):
        return self._args_to_string(double.player1.id, double.player2.id)
        
    def turn_finished(self, player):
        '''
        Can return a draw. If so, returns a 'None'.
        '''
                
        if(player is None):
            return self._args_to_string('None')
        else:
            return self._args_to_string(player.id)
        
    def hand_finished(self, double, truco_value):
        '''
        Can return a draw. If so, returns 'None', 'None' e 0.
        '''
         
        if(double is None):
            return self._args_to_string('None', 'None', 0)
        else:
            return self._args_to_string(double.player1.id,
                                        double.player2.id,
                                        truco_value)
        
#player = Player('x0x0', 'vitor')
#
#double = Double(player, player)
#
#card = Card(1)
#card2 = Card(2)
#card3 = Card(3)
#player.set_cards([card,card2,card3])
#filter1 = ControllerFilter(1)
#
#print "match_started " + filter1.match_started(player, player, player, player, player)
#
#print "hand_started " + filter1.hand_started(card, player, player, player, player)
#
#print "turn_started " + filter1.turn_started(player)
#
#print "card_player " + filter1.card_played('x0x0', 1)
#
#print "truco_asked " + filter1.truco_asked('x0x0')
#
#print "truco_accepted " + filter1.truco_accepted('x0x0', 3)
#
#print "gave_up " + filter1.gave_up('x0x0')
#
#print "eleven_hand " + filter1.eleven_hand(player, player)
#
#print "iron_hand " + filter1.iron_hand(player, player, player, player)
#
#print "match_finished " + filter1.match_finished(double)
#
#print "turn_finished " + filter1.turn_finished(player) 
#
#print "hand_finished " + filter1.hand_finished(double, 3)

