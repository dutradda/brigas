
import os
from uuid import uuid4
    
from brisa.upnp.device.service import Service

from brisa_game_server.games import BaseGame
from brisa_game_server.games import BaseRoom

from Controller import Controller
    
service_name = 'Truco'
service_type = 'urn:ic-ufal-br:service:Truco:1'
scpd_xml_path = os.path.join(os.path.dirname(__file__), 'truco-scpd.xml')
        
class TrucoRoom(BaseRoom):
    '''
    Room of truco game
    '''
    
    def __init__(self, truco, id, max_players=4):
        BaseRoom.__init__(self, truco, id, max_players)
        self.truco_players = {}
        self.truco_player_counter = 0
        self.controller = None

   
class Truco(BaseGame, Service):
    '''
    service of truco game
    '''
    
    def __init__(self):
        Service.__init__(self, service_name, service_type, '', scpd_xml_path)
        BaseGame.__init__(self)
  
    def add_room(self, uuid, max_players=4):
        '''
        add room
               
        @param uuid: room identifier
        @param max_players: maximum number of players
          
        @type uuid: int
        @type max_players: int
         
        @return: number of rooms
        @rtype: int
        '''
            
        self.rooms[self._room_counter] = \
          TrucoRoom(self, self._room_counter, max_players)
        self.rooms[self._room_counter].add_player(uuid)
        self._room_counter += 1
        return self._room_counter - 1

    def match_started_cb(self, str):
        '''
        set-up callback of MatchStarded
                
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('MatchStarted', str)
    
    def hand_started_cb(self, str):
        '''
        set-up callback of HandStarted
         
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('HandStarted', str)
    
    def turn_started_cb(self, str):
        '''
        set-up callback of TurnStarded
         
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('TurnStarted', str)

    def card_played_cb(self, str):
        '''
        set-up callback of CardPlayed
          
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('CardPlayed', str)

    def truco_asked_cb(self, str):
        '''
        set-up callback of TrucoAsked
          
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('TrucoAsked', str)

    def truco_accepted_cb(self, str):
        '''
        set-up callback of TrucoAccept
         
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('TrucoAccepted', str)

    def gave_up_cb(self, str):
        '''
        set-up callback of GaveUp
              
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('GaveUp', str)

    def eleven_hand_cb(self, str):
        '''
        set-up callback of ElevenHand
          
        @param str: parameters of callback
            
        @type  str: list
        '''
            
        self.set_state_variable('ElevenHand', str)

    def iron_hand_cb(self, str):
        '''
        set-up callback of IronHand
            
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('IronHand', str)

    def match_finished_cb(self, str):
        '''
        set-up callback of MatchFinished
               
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('MatchFinished', str)

    def turn_finished_cb(self, str):
        '''
        set-up callback of TurnFinished
                
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('TurnFinished', str)

    def hand_finished_cb(self, str):
        '''
        set-up callback of HandFinished
               
        @param str: parameters of callback
             
        @type  str: list
        '''
            
        self.set_state_variable('HandFinished', str)

    def start_new_match(self, room):
        '''
        subscribes callbacks and begins a new match
            
        @param room: room of truco
             
        @type  room: TrucoRoom
        '''
            
        room.controller = Controller(room.id, room.players)
        room.controller.event_subscribe('match_started', self.match_started_cb)
        room.controller.event_subscribe('hand_started', self.hand_started_cb)
        room.controller.event_subscribe('turn_started', self.turn_started_cb)
        room.controller.event_subscribe('card_played', self.card_played_cb)
        room.controller.event_subscribe('truco_asked', self.truco_asked_cb)
        room.controller.event_subscribe('truco_accepted', self.truco_accepted_cb)
        room.controller.event_subscribe('gave_up', self.gave_up_cb)
        room.controller.event_subscribe('eleven_hand', self.eleven_hand_cb)
        room.controller.event_subscribe('iron_hand', self.iron_hand_cb)
        room.controller.event_subscribe('match_finished', self.match_finished_cb)
        room.controller.event_subscribe('turn_finished', self.turn_finished_cb)
        room.controller.event_subscribe('hand_finished', self.hand_finished_cb)
        room.controller.start_match()

    def _check_player(self, uuid, room_id):
        '''
        verify if the player's in the room
             
        @param uuid: player identifier
        @param room_id: room identifier
                
        @type uuid: str
        @type room_id: int
        '''
            
        if rooms.has_key(room_id) and rooms[room_id].match_started:
            for room in self.rooms.values():
                if uuid in room.players:
                    return False
            return True
        else:
            return False
    
    def soap_throw_card(self, *args, **kwargs):
        '''
        throw a card on the table
              
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  *args: tuple
        @type  **kwargs: dict
        '''
            
        uuid = kwargs['UUID']
        room_id = int(kwargs['RoomID'])
        card_id = int(kwargs['CardID'])
        if self._check_player(uuid, room_id):
            truco_player = self.rooms[room_id].truco_players[uuid]
            controller = self.rooms[room_id].controller
            return {'PlayAnswer' : controller.throw_card(truco_player, card_id)}

    def soap_give_up_of_hand(self, *args, **kwargs):
        '''
        give up of the hand
            
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  *args: tuple
        @type  **kwargs: dict
        '''
            
        uuid = kwargs['UUID']
        room_id = int(kwargs['RoomID'])
        if self._check_player(uuid, room_id):
            truco_player = self.rooms[room_id].truco_players[uuid]
            controller = self.rooms[room_id].controller
            return {'PlayAnswer' : controller.give_up_of_hand(truco_player)}

    def soap_accept_iron_hand(self, *args, **kwargs):
        '''
        accept iron hand
               
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  *args: tuple
        @type  **kwargs: dict
        '''
            
        uuid = kwargs['UUID']
        room_id = int(kwargs['RoomID'])
        if self._check_player(uuid, room_id):
            truco_player = self.rooms[room_id].truco_players[uuid]
            controller = self.rooms[room_id].controller
            return {'PlayAnswer' : controller.accept_iron_hand(truco_player)}

    def soap_accept_eleven_hand(self, *args, **kwargs):
        '''
        accept eleven hand
             
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  *args: tuple
        @type  **kwargs: dict
        '''
            
        uuid = kwargs['UUID']
        room_id = int(kwargs['RoomID'])
        if self._check_player(uuid, room_id):
            truco_player = self.rooms[room_id].truco_players[uuid]
            controller = self.rooms[room_id].controller
            return {'PlayAnswer' : controller.accept_eleven_hand(truco_player)}

    def soap_truco(self, *args, **kwargs):
        '''
        ask for truco
          
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  *args: tuple
        @type  **kwargs: dict
        '''
            
        uuid = kwargs['UUID']
        room_id = int(kwargs['RoomID'])
        if self._check_player(uuid, room_id):
            truco_player = self.rooms[room_id].truco_players[uuid]
            controller = self.rooms[room_id].controller
            return {'PlayAnswer' : controller.truco(truco_player)}

    def soap_accept_truco(self, *args, **kwargs):
        '''
        accept a truco
         
        @param *args: list of arguments
        @param **kwargs: list of arguments with keywords
        
        @type  *args: tuple
        @type  **kwargs: dict
        '''
            
        uuid = kwargs['UUID']
        room_id = int(kwargs['RoomID'])
        if self._check_player(uuid, room_id):
            truco_player = self.rooms[room_id].truco_players[uuid]
            controller = self.rooms[room_id].controller
            return {'PlayAnswer' : controller.accept_truco(truco_player)}

