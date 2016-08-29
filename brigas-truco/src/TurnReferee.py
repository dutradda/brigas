'''
Created on 04/06/2009

@author: Vitor Normande
'''
from Card import Card
from Player import Player

class TurnReferee(object):
    '''
    This class represents a controller for "arbitra" the table
      when players are really playing. Pay attention to its cycle,
    you need to send the cards the players are throwing on the table.
      It will put the cards in order while you are registering them.
    Use the has_it_ended method to check if the card hit the top.
    Afterwards, ask the controller who won the turn in question,
    and dont forget to restart it.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__cards_in_table = []
        self.__manilha = 0
        
        self._vira = None
       
    def restart(self):
        '''
        reset the table cards
        '''
            
        self.__cards_in_table = []
        
    def define_manilha(self, card):
        '''
        Put the "vira" inside. And we will define the manilha...
             
        @param card: vira to calculate the manilha
             
        @type  card: Card
        '''
          
        self._vira = card
        self.__manilha = card.card_id_for_number()+1
        if self.__manilha > 10:
            self.__manilha = 1
        
    def __str__(self):
        string = "Vira: " + self._vira.__str__()
       
        for tupla in self.__cards_in_table:
            string += "\n    Jogador: " + tupla[1].name
            string += "; Carta: " + tupla[0].__str__()
        return string
        
    def put_card(self, card_dictionary):
        '''
        Deliver tuple with the card and the respective player.
        In this order.
             
        @param card_dictionary: 'list' of cards
         
        @type  card_dictionary: dict
        '''
                
        if(self.__cards_in_table.__len__() == 0):
            self.__cards_in_table +=[card_dictionary]
        else:
            card_to_add_number = card_dictionary[0].card_id_for_number()
            card_to_add_nipe_number = card_dictionary[0].card_id_for_nipe_number()
            
            card_in_top_of_deck_number = \
                                  self.__cards_in_table[0][0].card_id_for_number()
            card_in_top_of_deck_nipe_number = \
                             self.__cards_in_table[0][0].card_id_for_nipe_number()
            
            if(card_to_add_number == self.__manilha):
                card_to_add_number = 11
            if(card_in_top_of_deck_number == self.__manilha):
                card_in_top_of_deck_number = 11
                
            if(card_to_add_number == card_in_top_of_deck_number):
                if(card_to_add_number == 11):
                    if(card_to_add_nipe_number > card_in_top_of_deck_nipe_number):
                        self.__cards_in_table = [card_dictionary] + \
                                                self.__cards_in_table
                    else:
                        self.__cards_in_table +=[card_dictionary]
                else:
                    self.__cards_in_table = [card_dictionary] + \
                                            self.__cards_in_table
            elif(card_to_add_number > card_in_top_of_deck_number):
                self.__cards_in_table = [card_dictionary] + \
                                        self.__cards_in_table
            else:
                self.__cards_in_table +=[card_dictionary]
            
    def has_it_ended(self):
        '''
        ask for end of turn
            
        @rtype: boolean
        '''
            
        if(self.__cards_in_table.__len__() == 4):
            return True
                       
    def who_is_the_winner(self):
        '''
        Return the PLAYER who won the turn. None if none did.
               
        @rtype: Player
        '''
             
        if(self.__cards_in_table[0][0].card_id_for_number() ==
                                 self.__cards_in_table[1][0].card_id_for_number()):
            if(self.__cards_in_table[0][0].card_id_for_number() == self.__manilha):
                return self.__cards_in_table[0][1]
            else:
                return None
        else:
            return self.__cards_in_table[0][1]
                        
#            
#turn = TurnReferee()
#turn.define_manilha(Card(1))
#turn.put_card((Card(3),Player(1, "Jose Inacio")))
#turn.put_card((Card(1),Player(1, "Jose Inaciaozinho")))
#turn.put_card((Card(11),Player(1, "Jose Inaciaozinhoionhoooo")))
#turn.put_card((Card(23),Player(1, "Joseph")))
#print turn
#if(turn.has_it_ended()):
#    print "Vencedor:   "+turn.who_is_the_winner().__str__()
#

