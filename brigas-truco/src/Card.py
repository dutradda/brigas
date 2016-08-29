'''
Created on 01/06/2009

@author: vitor
'''

import random
   

#Create an array with the 40 card's IDs

'''

'''        
class Card(object):
    
    def __init__(self, card_id):
        self.__card_id = card_id
        
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.__card_id == other.__card_id
        return NotImplemented
         
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.__card_id > other.__card_id
        return NotImplemented
    
    def __str__(self):
        return ("("+ self.__card_id.__str__() + ")" +
                          self.card_id_for_number_str().__str__() +
                     " de " + self.card_id_for_nipe_str().__str__())
    
    def get_card_id(self):
        '''
        Obtain card identifier
        '''
               
        return self.__card_id
    
    def card_id_for_number(self):
        '''
        Take Rank of a card, without its Suit
          
        @return: rank of card
        @rtype:  int
        '''
            
        if(self.__card_id < 11):
            return self.__card_id
        elif((self.__card_id % 10) == 0):
            return 10
        else:
            return self.__card_id % 10
    
    def card_id_for_nipe_number(self):
        '''
        Take Suit of a card, without its Rank
          
        @return: suit of card
        @rtype:  int
        '''
            
        return int(round((self.__card_id-1)/10))
               
    def card_id_for_number_str(self):
        '''
        We start counting from 1, so the X is used to skip
                                   the first element, zero
                                                                                
        @return: string of rank
        @rtype:  str
        '''
        
        array = ["X","4","5","6","7","Q","J","K","A","2","3"]
        number = self.card_id_for_number()
        return array[number]
             
    def card_id_for_nipe_str(self):
        '''
        String corresponding to suit of card
           
        @return: string of suit
        @rtype:  str
        '''
            
        array = ["Ouros","Espadas","Copas","Paus"]
        return array[self.card_id_for_nipe_number()]
    
    card_id = property(get_card_id,None,None,None)
    

