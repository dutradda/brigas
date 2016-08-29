'''
Created on 01/06/2009

@author: vitor
'''
import random
from Card import Card

class Dealer(object):
    '''
    Dealer ("banca") controls giving and shuffling cards
    '''
    
    def __init__(self):
        self.__cards_deck = []
        self.__stack_counter = 0
        for i in range(1,41):
            self.__cards_deck += [ i ]

    def fisher_yatters_shuffling(self):
        '''
        Algorithm Fisher-Yatters Shuffling
        '''
                
        n = self.__cards_deck.__len__()
        while (n>0):
            n -= 1
            k = random.randint(1,4000)%40#0 <= k < n.
            tmp = self.__cards_deck[k]
            self.__cards_deck[k] = self.__cards_deck[n]
            self.__cards_deck[n] = tmp
    
    def get_card(self):
        '''
        Get a card
             
        @rtype: Card
        '''             
        
        card = Card(self.__cards_deck[ self.__stack_counter ])
        self.__stack_counter += 1
        return card
              
    def __str__(self):
        return self.__cards_deck.__str__()
              
    def get_vira(self):
        '''
        Get the card Vira
              
        @rtype: Card
        '''
        
        return Card(self.__cards_deck[self.__cards_deck.__len__()-1])
    
    def clean_table_and_restart(self):
        '''
        Restart table
        '''
            
        self.__stack_counter = 0
        self.fisher_yatters_shuffling()






