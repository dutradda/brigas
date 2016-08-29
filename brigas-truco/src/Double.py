'''
Created on 03/06/2009

@author: vitor
'''
from Player import Player

class Double(object):
    '''
    Twosome of players
    '''

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        
        self.__player1.set_double(self)
        self.__player2.set_double(self)
        
        #This is the current match points acquired
        self.__score = 0
        self.__total_score = 0
             
    def __str__(self):
        return "Player 1:" + self.__player1.__str__() + \
                       "\n Player2:" + self.__player2.__str__() + \
                       "\n Pontuacao: " +  self.__score.__str__() + \
                       "; Partidas: " + self.__total_score.__str__()
    
    def add_points_to_score(self, points_to_add):
        '''
        Add points to score
          
        @param points_to_add: points
             
        @type  points_to_add: int
        '''
            
        self.__score  += points_to_add
    
    def add_match_to_total_score(self):
        '''
        Add match to score
        '''
            
        self.__total_score += 1
        
    def get_score(self):
        '''
        View score
             
        @return: score
        @rtype:  int
        '''
            
        return self.__score
    
    def restart_score(self):
        '''
        Restart score
        '''
            
        self.__score = 0
        
    def get_player1(self):
        '''
        Get player number one
         
        @return: player1
        @rtype:  Player
        '''
            
        return self.__player1
    
    def get_player2(self):
        '''
        Get player number two
          
        @return: player2
        @rtype:  Player
        '''
            
        return self.__player2

    def get_other_player(self, player):
        '''
        In case this double has this player,
        it will return the opposite player.
        If it doesnt have this player, it will return None.
                
        @param player: player to compare
               
        @type  player: Player
          
        @return: player
        @rtype:  Player, NoneType
        '''
            
        if(player == self.__player1):
            return self.__player2
        elif(player == self.__player2):
            return self.__player1
        else:
            return None
    
    def player_belongs(self, player):
        '''
        Checks if the player belongs to the double.
        In might be done by id or the class player
         
        @param player: player to compare
               
        @type  player: Player
          
        @rtype:  boolean
        '''
        
        if isinstance(player, Player):
            if(self.__player1 == player):
                return True
            elif(self.__player2 == player):
                return True
            else:
                False
        else:
            if(self.__player1.id == player):
                return True
            elif(self.__player2.id == player):
                return True
            else:
                False

    def get_player(self, player_id):
        '''
        Get the player by its id.
        
        @param player: player identifier
               
        @type  player: str
             
        @return: player
        @rtype: Player, NoneType
        '''
    
        if(self.__player1.id == player_id):
            return self.__player1
        elif(self.__player2.id == player_id):
            return self.__player1
        else:
            None
    
    score = property(get_score, None, None, None)
    player1 = property(get_player1, None, None, None)
    player2 = property(get_player2, None, None, None)
    
#player1 = Player(1, "antonio")
#player2 = Player(2, "antonioMaria")
#
#double = Double(player1, player2)
#
#print player2.get_double()
