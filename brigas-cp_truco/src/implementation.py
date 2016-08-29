# coding=utf-8

'''
Definição da classe "Control Point do Truco"
São implementados métodos relacionados as ações existentes no jogo truco

@author: Galetu, claro com a contribuição óbvia do Punk
'''

from brisa_game_server.control_points.game_manager import GameManagerCP

truco_service = 'urn:ic-ufal-br:service:Truco:1'

class Player(object):
  """
  Modelagem de 'Jogador'
  """
  def __init__(self):
    self.cards = []
    self.opponents = None
    self.my_double = None
    
class OtherPlayer(object):
  """
  Modelagem alternativa de 'Jogador'
  """
  def __init__(self, id):
    self.id = id
    self.cards = []

class TrucoCP(GameManagerCP):
  """
  'ControlPoint' do jogo de 'Truco', que herda do
    'ControlPoint' de 'GameManager'  
  """
  def __init__(self):
    GameManagerCP.__init__(self)
    self._truco = None
    self._events['MatchStarted'] = []
    self._events['HandStarted'] = []
    self._events['TurnStarted'] = []
    self._events['CardPlayed'] = []
    self._events['TrucoAsked'] = []
    self._events['TrucoAccepted'] = []
    self._events['GaveUp'] = []
    self._events['ElevenHand'] = []
    self._events['IronHand'] = []
    self._events['MatchFinished'] = []
    self._events['TurnFinished'] = []
    self._events['HandFinished'] = []
    self._events['MyTurn'] = []
    self.player = Player()
    self.other_players = None
    self._who_played = None

  def choose_game(self, game_name):
    """
    Entra no 'jogo' a partir do nome deste,
      e inscreve eventos e callbacks a estes associadas
    
    @param game_name: nome do 'jogo'
     
    @type  game_name: str
    """
    GameManagerCP.choose_game(self, game_name)
    self._truco = self.my_server.services[truco_service]
    self._truco.subscribe_for_variable("MatchStarted",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("HandStarted",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("TurnStarted",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("CardPlayed",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("TrucoAsked",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("TrucoAccepted",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("GaveUp",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("ElevenHand",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("IronHand",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("MatchFinished",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("TurnFinished",
                                           self._variable_event_cb)
    self._truco.subscribe_for_variable("HandFinished",
                                           self._variable_event_cb)

  def _variable_event_cb(self, name, value):
    """
    Analisa e executa callback de evento pelo nome passado,
      e utiliza a parte do valor passado correspondente
    
    @param name:  nome do evento
    @param value: parametros a serem analisados, separados por ':'
       
    @type  name:  str
    @type  value: str
    """
    if name == 'MatchStarted':
      values = value.split(':')
      for i in range(values.size()):
        if values[i] == self.player.id:
          self.other_players =(OtherPlayer(values[(i+2)%4],
                               OtherPlayer(values[(i-1)%4]]),
                               OtherPlayer(values[(i+1)%4]))
          self.player._my_double = self.other_players[0]
          self.player._my_opponents = (self.other_players[1],
                                       self.other_players[2])
          self._exec_cb('MatchStarted')
          break
            
    elif name == 'HandStarted':
      values = value.split(':')
      for i in range(values.size()):
        if values[i] == self.player.id:
          vira_id = values[0]
          self.player.cards = (values[i+1], values[i+2], values[i+3])
          self._exec_cb('HandStarted', vira_id, self.player.cards)
          break
      
    elif name == 'TurnStarted':
      if value == self.player.id:
        self._exec_cb('TurnStarted', self.player)
      else:
        for other_player in other_players:
          if value == self.other_player.id:
            self._exec_cb('TurnStarted', self.other_player)
            break
      
    elif name == 'CardPlayed':
      values = value.split(':')
      for other_player in self.other_players:
        if values[0] == self.other_player.id:
          self.other_player.cards.append(values[1])
          self._exec_cb('CardPlayed', self.other_player)
          break
        
    elif name == 'TrucoAsked':
      for other_player in self.other_players:
        if value == self.other_player.id:
          self._exec_cb('TrucoAsked', self.other_player)
          break
       
    elif name == 'TrucoAccepted':
      values = value.split(':')
      for other_player in self.other_players:
        if values[0] == self.other_player.id:
          value_truco = values[1]
          self._exec_cb('TrucoAccepted', self.other_player, value_truco)
          break
    
    elif name == 'GaveUp': # Desiste ou nao aceita truco
      for other_player in other_players:
        if value == self.other_player.id:
          self._exec_cb('GaveUp', self.other_player)
          break
        
    elif name == 'ElevenHand':
      values = value.split(':')
      if values[0] == self.player.id:
        cards_double = (values[5], values[6], values[7])
        self._exec_cb('ElevenHand', self.player, cards_double)
        self._exec_cb('ElevenHand', self.player.my_double, self.player.cards)
      elif values[4] == self.player.id:
        cards_double = (values[1], values[2], values[3])
        self._exec_cb('ElevenHand', self.player, cards_double)
        self._exec_cb('ElevenHand', self.player.my_double, self.player.cards)
        
    elif name == 'IronHand':
      #todo
          
    elif name == 'MatchFinished':
      #todo
                
    elif name == 'TurnFinished':
      #todo
          
    elif name == 'HandFinished':
      #todo

  def throw_card(self, card_id):
    """
    Joga carta correspondente ao seu identificador
    
    @param card_id: identificador da carta
  
    @type  card_id: int
    """
    self._truco.ThrowCard(UUID=self.uuid,
                          RoomID=self.my_room.id,
                          CardID=card_id)

  def give_up(self):
    """
    Declara desistencia
    """
    self._truco.GiveUpOfHand(UUID=self.uuid,
                             RoomID=self.my_room.id)

  def accept_iron_hand(self):
    """
    Aceita Mao de Ferro
    """
    self._truco.AcceptIronHand(UUID=self.uuid,
                               RoomID=self.my_room.id)

  def accept_eleven_hand(self):
    """
    Aceita Mao de Onze
    """
    self._truco.AcceptElevenHand(UUID=self.uuid,
                                 RoomID=self.my_room.id)

  def truco(self):
    """
    Pede truco
    """
    self._truco.Truco(UUID=self.uuid, RoomID=self.my_room.id)

  def accept_truco(self):
    """
    Aceita truco
    """
    self._truco.AcceptTruco(UUID=self.uuid, RoomID=self.my_room.id)




