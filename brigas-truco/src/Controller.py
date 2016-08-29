'''
Created on 03/06/2009
Last modified on 09/06/2009, 00:12
@author: Vitor Normande (Vulgo Harry Potter)
'''

import random

from Card import Card
from Dealer import Dealer
from Double import Double
from Player import Player
from TurnReferee import TurnReferee
from HandReferee import HandReferee
from ControllerFilter import ControllerFilter

class Controller(object):
    '''
    This is the controller class.
    
    The list of class Controll methods to raise are:
    match_started - void
    hand_started - (Card) vira, 4x( (int)Players ids, (Card) cards)
    turn_started - (Player) returns the player is going to start
    card_played - (int) player ID, (int) card number
    truco_asked - (Double) double who yelled truco
    truco_accepted - (int) value of current truco
    gave_up - (Double) who gave up
    eleven_hand - player1 id, player1 cards, player2 id, player2 cards
    iron_hand - the four players ids and cards,
                            following the sequence of players and doubles
    match_finished - (Double)returns the double who wins the match
    turn_finished -  (Player) won the turn
    hand_finished - (Double) double whos won the hand,
                                                      (int) points gained
    '''
    
    def __init__(self, id, players):
        '''
        Reveive a list of Players and start the game controller.
               
        @param id: identifier
        @param players: list of Players
                
        @type id: str
        @type players: list
        '''
        
        self._id = id
        self._players_id = players
        self.__players_list = []
        self.__doubles_list = []
        
        self.__players_list += [Player(self._players_id[0], "Joao Buracao")]
        self.__players_list += [Player(self._players_id[1], "Tiririca")]
        
        self.__players_list += [Player(self._players_id[2], "Joao Mereque")]
        self.__players_list += [Player(self._players_id[3], "Alcino")]
        
#        self.__players_list += [Player(self.__players_list.__len__(),
#                                                      "Joao Buracao")]
#        self.__players_list += [Player(self.__players_list.__len__(),
#                                                      "Joao Mereque")]
#        
        self.__doubles_list += [Double(self.__players_list[0],
                                                self.__players_list[2])]
#        
#        self.__players_list += [Player(self.__players_list.__len__(),
#                                                          "Tiririca")]
#        self.__players_list += [Player(self.__players_list.__len__(),
#                                                            "Alcino")]
#        
        self.__doubles_list+= [Double(self.__players_list[1],
                                                self.__players_list[3])]
       
        self.__dealer = Dealer()
        self.__vira = None
        
        self.__truco_value = 1
        
        self.__truco_was_asked_last_time_by = None
        self.__truco_was_asked = False
        
        self._eleven_hand = None
        
        self._iron_hand = False
        self._iron_hand_response = None
        
        self.__give_up_was_asked = None
        
        self.__who_started_the_hand = None
        self.__who_won_last_round = None
        self.__turn_of_player = None
        
        self._controller_filter = ControllerFilter(id)
        self.__turn_referee = TurnReferee()
        self.__hand_referee = HandReferee()

        self._callbacks = {'match_started': [], 'hand_started': [], 
                           'turn_started': [], 'card_played' : [], 
                           'truco_asked' : [], 'truco_accepted' : [],
                           'gave_up' : [], 'eleven_hand' : [],
                           'iron_hand' : [], 'match_finished': [], 
                           'turn_finished' : [], 'hand_finished' : []}

    def event_subscribe(self, event, callback):
      '''
      Subscribe events
      
      @param event: event
      @param callback: function callback
      
      @type  event: str
      @type  callback: function
      '''
          
      try:
        self._callbacks[event].append(callback)
      except:
        raise Exception('Event don\'t exist')

    def _exec_cb(self, event, *args, **kwargs):
        '''
        Execute callback of event
               
        @param event: event
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  event: str
        @type  *args: tuple
        @type  **kwargs: dict
        '''
        
     # try:
        str1 =  'self._controller_filter.'+ event + '(*args)'
        str2 = eval('self._controller_filter.'+ event + '(*args)')
        print str1 + ' dah ' + str2  
        for cb in self._callbacks[event]:
          cb(str2)
        
     #   raise Exception('Event don\'t exist: ' + event)

    def __str__(self):
        str = "Duplas: \n    " + self.__doubles_list[0].__str__() + \
                         "\n    " + self.__doubles_list[1].__str__() + "\n"
        str += "Turno: " + self.__turn_referee.__str__() + "\n"
        str += "Vez: " + self.__turn_of_player.name + "\n"
        str += "Mesa: "
        for player in self.__players_list:
            str += player.name + ", "
        return str
    
    def switch_turn_of_players(self, player):
        '''
        Get a player and return the next player in order.
        
        @param player: player identifier
             
        @type  player: str
             
        @return: next player
        @rtype: Player
        '''
        if(player == self.__players_list[3]):
            return self.__players_list[0]
        else:
            return self.__players_list[self.__players_list.index(player)+1]
        
    def start_match(self): 
        '''
        Start a match
        '''
        
        self.__who_won_last_round = self.__who_started_the_hand = \
                                 self.__players_list[random.randint(0,3)]
        self._exec_cb('match_started', self.__players_list[0],
                                         self.__players_list[1],
                                       self.__players_list[2],
                                       self.__players_list[3])
        self.start_hand()
        
    def start_eleven_hand(self):
        '''
        Starts eleven hand.
        '''
        player1 = self._eleven_hand.player1
        player2 = self._eleven_hand.player2
        
        self._exec_cb('eleven_hand',player1, player2)
    
    def start_iron_hand(self):
        '''
        Starts iron hand.
        '''
        
        player1 = self.__doubles_list[0].player1
        player2 = self.__doubles_list[0].player2
        player3 = self.__doubles_list[1].player1
        player4 = self.__doubles_list[1].player2
        
        self._exec_cb('iron_hand',player1, player2, player3, player4)
                          
    def start_hand(self):
        '''
        Start a hand
        '''
         
        self.__dealer.clean_table_and_restart()
        
        #Give the cards to players
        for player in self.__players_list:
            player.set_cards( [self.__dealer.get_card(),
                              self.__dealer.get_card(),
                              self.__dealer.get_card()])
        
        #Lets define who will start the hand, keep in mind
          #  it will be the one after who started last hand
        self.__who_won_last_round = self.__who_started_the_hand = \
                       self.switch_turn_of_players(self.__who_started_the_hand)
        self.__vira = self.__dealer.get_vira()
        
        self.__turn_referee.define_manilha(self.__vira)
        
        #Checks if eleven_hand is activated,
             #  if so, interrupts the initialization.
        if(self._eleven_hand is not None):
            self.start_eleven_hand()
            return
        elif(self._iron_hand):
            self.start_iron_hand()
            return
                
        self._exec_cb('hand_started', self.__vira, self.__players_list[0],
                                                   self.__players_list[1],
                                                   self.__players_list[2],
                                                   self.__players_list[3])
        
        self.start_turn()

    
    def start_turn(self):
        '''
        Start a turn
        '''
        
        self.__turn_of_player = self.__who_won_last_round
        self._exec_cb('turn_started', self.__who_won_last_round)
        
    def finish_match(self, double):
        '''
        Ends a match
               
        @param double: double of players
               
        @type  double: Double
        '''
        
        print "A partida acabou e quem ganhou foi a dupla: " + \
                                                       double.__str__()
        double.add_match_to_total_score()
        
        self._exec_cb('match_finished', double)

        self.__doubles_list[0].restart_score()
        self.__doubles_list[1].restart_score()
       
        self._eleven_hand = None
        
        self._iron_hand = False
        self._iron_hand_response = None
        
        self.start_match()
        
    def finish_hand(self, double):
        '''
        Ends a hand
            
        @param double: double of players
               
        @type  double: Double
        '''
        
        if(double is not None):
            print "The hand is over and the double: " + double.__str__() + \
                      " gained " + self.__truco_value.__str__() + " points"
            double.add_points_to_score(self.__truco_value)
            self._exec_cb('hand_finished', double, self.__truco_value)
        else:
            print "the hand is over and it was a draw"
            self._exec_cb('hand_finished', None, self.__truco_value)
        
        self.__hand_referee.restart()
        
        self.__truco_was_asked = False
        self.__truco_was_asked_last_time_by = None
                
        self.__truco_value = 1
                
        if(double.score >= 12):
            self.finish_match(double)
            return
        elif(double.score == 11):
            if(self._eleven_hand is not None):
                self._eleven_hand = None
                self._iron_hand = True
            else:
                self._eleven_hand = double
        
        self.start_hand()
        
    def finish_turn(self, winner):
        '''
        Ends a turn setting a winner(a player). 
        
        @param winner: player who wins the turn
                
        @type  winner: Player
        '''
        if(winner != None):
            print winner.__str__() + " ganhou o turno"
            self.__who_won_last_round = winner
        else:
            print "Empatou o turno"
        
        self.__turn_referee.restart()
        
        if(winner != None):
            self.__hand_referee.put_winners(winner.get_double())
        else:
            self.__hand_referee.put_winners(None)
        
        self._exec_cb('turn_finished', winner)
        
        if(self.__hand_referee.has_it_ended()):
            self.finish_hand(self.__hand_referee.who_is_the_winner())
        else:
            self.start_turn()
        
    def accept_truco(self, player_id):
        '''
        Accept Truco
           
        @param player_id: player identifier
             
        @type  player_id: str
           
        @rtype: int
        '''
            
        if(self.__truco_was_asked):
            if not self.__truco_was_asked_last_time_by.player_belongs(player_id):
                if(self.__truco_value == 1):
                    self.__truco_value = 3
                else:
                    self.__truco_value +=3
                    
                self.__truco_was_asked = False      
                print "truco aumentado para " + self.__truco_value.__str__()

                self._exec_cb('truco_accepted', player_id ,self.__truco_value)
                return 1
            else:
                print "cara n eh da dupla que precisa responder"
                return 2
        else:
            print "Ninguem pediu truco"
            return 3
        
    
    def truco(self, player_id):
        '''
        Requery Truco
          
        @param player_id: player identifier
             
        @type  player_id: str
           
        @rtype: int
        '''
            
        if(self.__truco_was_asked):
            print "Alguem jah pediu truco"
            return 2
        elif(self.__truco_value == 12):
            print "truco estah no maximo"
            return 3
        elif(self._iron_hand):
            print "tah em mao de ferro"
            return 4
            
        else:
            
            double_of_player = None
            
            for double in self.__doubles_list:
                if(double.player_belongs(player_id)):
                    double_of_player = double
            if(self.__truco_was_asked_last_time_by == None):
                self.__truco_was_asked_last_time_by = double_of_player
                self.__truco_was_asked = True
                self._exec_cb('truco_asked', player_id)
                return 1
            elif(self.__truco_was_asked_last_time_by == double_of_player):
                print "Sua dupla jah pediu truco a ultima vez"
                return 5
            else:
                self.__truco_was_asked_last_time_by = double_of_player
                self.__truco_was_asked = True
                self._exec_cb('truco_asked', player_id)
                return 1
        
    def accept_eleven_hand(self, player_id):
        '''
        Accept eleven hand
             
        @param player_id: player identifier
            
        @type  player_id: str
          
        @rtype: int
        '''
            
        if((self._eleven_hand is not None) and
            self._eleven_hand.player_belongs(player_id)):
            #That continue the initialization of a turn, stopped when 
            #the eleven hand was activated
            self._exec_cb('hand_started', self.__vira, self.__players_list[0],
                                                       self.__players_list[1],
                                                       self.__players_list[2],
                                                       self.__players_list[3])
            self.start_turn()
            return 1
        
        print "Vc n tem que aceitar nenhuma mao de onze"
        return 2           
        
    def accept_iron_hand(self, player_id):
        '''
        Accept iron hand
               
        @param player_id: player identifier
            
        @type  player_id: str
          
        @rtype: int
        '''
            
        if(self._iron_hand):
            double_to_check = None
            for double in self.__doubles_list:
                if(double.player_belongs(player_id)):
                    double_to_check = double
            
            if(self._iron_hand_response is None):
                self._iron_hand_response = double
                return 1
            elif(self._iron_hand_response.player_belongs(double_to_check)):
                print "a dupla jah aceitoou o iron hand..."
                return 2
            else:
                self._iron_hand_response = None
                #That continue the initialization of a turn, stopped when 
                #the iron hand was activated
                self._exec_cb('hand_started', self.__vira,
                                              self.__players_list[0],
                                              self.__players_list[1],
                                              self.__players_list[2],
                                              self.__players_list[3])
                self.start_turn()
                return 1
                
        else: 
             print "Vc n tem que aceitar nenhuma mao de ferro"
             return 3           
        
    def give_up_of_hand(self, player_id):
        '''
        Quit hand
             
        @param player_id: player identifier
             
        @type  player_id: str
           
        @rtype: int(1)
        '''
        
        winner_double = None
        for double in self.__doubles_list:
            if(double.player_belongs(player_id)):
                self.__truco_was_asked = double
                print double.get_player(player_id).name, " pediu pa desistir"
                self._exec_cb('gave_up', player_id)
            else:
                winner_double = double
        
        
        self.finish_hand(winner_double)
        return 1       
                
    def throw_card(self, player_id, card_id):
        '''
        Throw a card
        Returns 1 if its allrit
                2 if it wasnt the players turn.
                3 if it the card doesnt belong to the player.
        
        @param player_id: player identifier
        @param card_id:   card identifier
               
        @type  player_id: str
        @type  card_id:   int
           
        @rtype: int
        '''
        
        card_thrown = Card(card_id)
        if(self._eleven_hand is not None):
            print "ta na mao de onze"
        elif(self._iron_hand):
            print "tah na mao de ferro"
        elif(self.__truco_was_asked):
            print "!Truco!"
        else:
            #
            if(self.__turn_of_player.id != player_id):
                print "nao eh a sua vez de jogar"
                return 2     
                
            else:
                if(not self.__turn_of_player.play_card(card_thrown)):
                    print "carta nao tah no jogador"
                    return 3
                else:
                    self.__turn_referee.put_card((card_thrown,
                                                  self.__turn_of_player))

                    self._exec_cb('card_played', player_id, card_id)
                    
                    #Check if the turn is over...
                    if(self.__turn_referee.has_it_ended()):
                        self.finish_turn(self.__turn_referee.who_is_the_winner())
                    else:
                        self.__turn_of_player = \
                               self.switch_turn_of_players(self.__turn_of_player)
        return 1

#c = Controller(1,['x1','x2','x3','x4'])
#c.start_match()
