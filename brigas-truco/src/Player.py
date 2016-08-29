'''
Created on 03/06/2009

@author: vitor
'''

from Card import Card
    
class Player(object):

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__cards = []
        self.__double = None
    
    def set_double(self, double):
        '''
        set up a double
                
        @param double: twosome of players
              
        @type  double: Double
        '''
            
        self.__double = double
        
    def get_double(self):
        '''
        get a double
          
        @param double: twosome of players
              
        @type  double: Double
         
        @rtype: Double
        '''
            
        return self.__double
    
    def get_id(self):
        '''
        get identifier
         
        @rtype: str
        '''
            
        return self.__id
              
    def set_cards(self, cards):
        '''
        Deliver cards in a array to avoid errors.
              
        @param cards: list of cards
            
        @type  cards: list
        '''
        
        self.__cards = cards    
        
    def get_cards(self):
        '''
        return list of cards
          
        @rtype cards: list
        '''
            
        return self.__cards          
        
    def play_card(self, card):
        '''
        Remove the Card and returns True if the card belongs to the player,
        False otherwise.
           
        @param card: playing card
              
        @type  card: Card
              
        @rtype: boolean
        '''
            
        if(card in self.__cards):
            self.__cards.remove(card)
            return True
        else:
            return False
                        
    def put_cards_away(self):
        '''
        reset the list of cards
        '''
            
        self.__cards = []        
        
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.__id == other.__id
        return NotImplemented
        
    def __str__(self):
        string = "name: " + self.__name + \
                       "ID: "+ self.__id.__str__() + " Cards:"
        for i in range(self.__cards.__len__()):
            string += self.__cards[i].__str__()+"; "
        return string
  
    def get_name(self):
        '''
        return the name of player
              
        @rtype: str
        '''
            
        return self.__name
            
    def have_cards(self):
        '''
        test if there are any cards
            
        @rtype: boolean
        '''
            
        if (self.__cards.__len__() == 0):
            return False
        else:
            True
    
    name = property(get_name,None,None,None)
    id = property(get_id, None, None, None)
    double = property(get_double, set_double, None, None)


