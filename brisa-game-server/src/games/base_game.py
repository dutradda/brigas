# coding=utf-8

#
#Classes base para "salas" e "jogos"
#


class BaseRoom(object):
  """
  Classe correspondente a 'sala' base
  """
  def __init__(self, game, id, max_players):
    self.id = id
    self.max_players = max_players
    self.players = []
    self._game = game
    self.match_started = False

  def add_player(self, player_uuid):
    """
    Adiciona jogadores na 'sala'
   
    @param player_uuid: identificador unico de jogador
     
    @type  player_uuid: str
    """
    if self.match_started:
      return False
    self.players.append(player_uuid)
    if len(self.players) == self.max_players:
      self.match_started = True
      self._game.start_new_match(self)
    return True

  def remove_player(self, player_uuid):
    """
    Remove jogador da 'sala'
       
    @param player_uuid: identificador unico de jogador
     
    @type  player_uuid: str
    """
    if not self.match_started:
      try:
        self.players.remove(player_uuid)
      except:
        return False
      if len(self.players) == 0:
        self._game.remove_room(self.id)
      return True


class BaseGame(object):
  """
  Classe base de 'jogos'
  """
  def __init__(self):
    self.rooms = {}
    self._room_counter = 0

  def start_new_match(self, room):
    """
    Inicia nova partida
    
    @param room: identificador de 'room'
   
    @type  room: str
    """
    pass

  def add_room(self, uuid, max_players):
    """
    Adiciona jogador em 'sala'
     
    @param uuid: identificador de jogador
    @param max_players: numero maximo de jogadores
 
    @type  uuid: str
    @type  max_players: int
    """
    pass

  def remove_room(self, room_id):
    """
    Remove 'sala'
  
    @param room_id: identificador da 'room'
        
    @type  room_id: int
    """
    self.rooms.pop(room_id)

