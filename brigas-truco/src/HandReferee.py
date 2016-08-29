'''
Created on 04/06/2009

@author: Vitor Normande
'''
from Double import Double
from Player import Player

class HandReferee(object):
    '''
    This class encapsulates the logic for a hand.
    That is,its sets the double which won the hand.
    So as to get the winners of a hand
    you have to get the winner from each card.
    Every turn you ask the Match Referee whether its over,
    and get back the winner double.
    '''
        
    def __init__(self):
        '''
        Constructor
        '''
           
        self.__doubles_list = []
        self.__winner = None
    
    def restart(self):
        '''
        Restart the HandReferee,
         it has to be done when the hand is over
        '''
            
        self.__doubles_list = []
        self.__winner = None
           
    def put_winners(self, winner):
        '''
        Set the winner of a turn. It must be a Double.
        
        @param winner: winner of a turn

        @type  winner: Double
        '''
             
        self.__doubles_list += [winner]
        
    def has_it_ended(self):
        '''
        Are we done? Lets assess if its over.
        
        @rtype: boolean
        '''
            
        if(self.__doubles_list.__len__() == 1):
            return False
        elif(self.__doubles_list.__len__() == 2):
            if(self.__doubles_list[1] == None):
                if(self.__doubles_list[0] == None):
                    return False
                else:
                    self.__winner = self.__doubles_list[0]
                    return True
            else:
                if(self.__doubles_list[0] == None):
                    self.__winner = self.__doubles_list[1]
                    return True
                elif(self.__doubles_list[0] == self.__doubles_list[1]):
                    self.__winner = self.__doubles_list[0]
                    return True
                else:
                    return False
        elif(self.__doubles_list.__len__() == 3):
            if(self.__doubles_list[2] == None):
                if(self.__doubles_list[0] == None):
                    self.__winner = None
                    return True
                else:
                    self.__winner = self.__doubles_list[0]
                    return True
            else: 
                self.__winner = self.__doubles_list[2]
                return True
        else:
            print "Deu maior do que podia aki!!!!!!!!excessao" 

    def who_is_the_winner(self):
        '''
        Get the winner, if its over of course.
        
        @return: winner twosome
        @rtype:  Double
        '''
            
        return self.__winner

#match = HandReferee()
#
#players_list = []
#doubles_list = []
#
#players_list += [Player(players_list.__len__(), "Joao Buracao1")]
#players_list += [Player(players_list.__len__(), "Joao Mereque1")]
#        
#doubles_list += [Double(players_list[0], players_list[1])]
#        
#players_list += [Player(players_list.__len__(), "Tiririca2")]
#players_list += [Player(players_list.__len__(), "Alcino2")]
#
#doubles_list += [Double(players_list[2], players_list[3])]
#
#match.put_winners(None)
#match.put_winners(None)
#match.put_winners(None)
#
#print match.has_it_ended()
#print match.who_is_the_winner()
