# coding=utf-8

#
#Definicao das classes "sala", "jogo", "ControlPoint do GameManager"
#Para este ultimo, sao implementados metodos que lidam com
# inscricao de eventos, conexao com servidor e trata acoes com
# "jogos" e "salas"
#

from brisa.upnp.control_point.control_point import ControlPoint
import time

game_manager = 'urn:ic-ufal-br:service:GameManager:1'


class Room(object):
  """
  Caracterizacao de uma classe para 'Sala'
  """
  def __init__(self, id, max_players, num_players):
    self.id = id
    self.max_players = max_players
    self.num_players = num_players


class Game(dict):
  """
  Caracterizacao de uma classe para 'Jogo'
  """
  def __init__(self, name):
    dict.__init__(self)
    self.name = name


class GameManagerCP(ControlPoint):
  """
  'ControlPoint' do 'GameManager', que herda do 'ControlPoint' do BRisa
  """
  def __init__(self):
    ControlPoint.__init__(self)
    self._initial_subscribes()
    self.servers = {}
    self.start_search(600)
    self.uuid = ''
    self.my_server = None
    self.my_game = None
    self.my_room = None
    self._game_manager = None
    self.games = {}
    self._events = {}
    self._events['RoomUpdate'] = []

  def __del__(self):
    self.leave_server()

  def _initial_subscribes(self):
    """
    Inscreve eventos de inclusao e remocao de 'devices'
               [callbacks locais]
    """
    self.subscribe('new_device_event', self.on_new_device)
    self.subscribe('removed_device_event', self.on_remove_device)

  def event_subscribe(self, event, callback):
    """
    Inscreve evento com callback associada
    
    @param event: evento que esta' a ser inscrito
    @param callback: callback que esta' a ser associada a dado evento
       
    @type  event: str
    @type  callback: function
    """
    try:
      self._events[event].append(callback)
    except:
      raise Exception('Event don\'t exist')

  def _exec_cb(self, event, *args, **kwargs):
    """
    Executa callback dos eventos inscritos
    
    @param event: evento que esta' a ser executado
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                                
    @type  event: str
    @type  *args: tuple
    @type  **kwargs: dict
    """
    #
    #def typeArgLists(*args, **kwargs):
    #    print 'args:', type(args)
    #    print 'kwargs:', type(kwargs)
    #
    #funcao teste que guiou os types acima especificados
    #
    try:
      for cb in self._events[event]:
        cb(args, kwargs)
    except:
      raise Exception('Event don\'t exist')

  def on_new_device(self, dev):
    """
    Callback para o evento de inclusao de novo 'device'

    @param dev: novo 'device' a ser incluido
   
    @type  dev: Device [brisa.upnp.base_device]
    """
    if 'GameServer' in dev.device_type:
      print 'New game server found'
      try:
        self.servers[dev.friendly_name]
        print 'This server already exist'
      except:
      	self.servers[dev.friendly_name] = dev

  def on_remove_device(self, udn):
    """
    Callback para o evento de exclusao de 'device'
    
    @param udn: identificador de 'device'
    
    @type  udn: str
    """
    for dev in self.servers.values():
        if dev.udn == udn:
          if self.my_server and self.my_server.udn == udn:
            print 'My server gone'
            self.my_server = None
          else:
            print 'A game server is gone'
          try:
            self.servers.pop(dev.friendly_name)
          except Exception, e:
            print e.message

  def _has_server(self):
    """
    Testa se conectado a algum servidor
   
    @rtype:  boolean
    """
    if self.my_server is None:
      return False
    else:
      return True

  def _has_game(self):
    """
    Testa se encontrou algum 'jogo' disponível
        
    @rtype: boolean
    """
    if self.my_game is None:
      return False
    else:
      return True

  def _get_available_games(self):
    """
    Pesquisa por algum 'jogo' disponivel
       
    @return: games
    @rtype:  list
    """
    games = self._game_manager.GetAvailableGames()['Games']
    for game_name in games.split(':'):
      self.games[game_name] = Game(game_name)
    return self.games

  def _get_available_rooms(self, name='', value=''):
    """
    Pesquisa por 'sala' disponivel.
    Pode ser desconsiderado algum dos dois parametros.
    
    @param name:  nome da 'sala'
    @param value: identificador da sala
   
    @type  name:  str
    @type  value: int
   
    @rtype: boolean, NoneType
    """
    if self.my_game is None:
      return None
    time.sleep(1)
    dict_rooms = \
      self._game_manager.GetAvailableRooms(Game=self.my_game.name)
    if dict_rooms['RoomsID'] == '-1':
      return False
    rooms_id = dict_rooms['RoomsID'].split(':')
    max_players = dict_rooms['MaxPlayers'].split(':')
    num_players = dict_rooms['NumPlayers'].split(':')
    rooms = []
    if not rooms_id[0] == '':
      rooms = [Room(int(rooms_id[i]),
                    int(max_players[i]), int(num_players[i]))
                                       for i in range(len(rooms_id))]
    self.my_game.clear()
    for room in rooms:
      self.my_game[room.id] = room
    print 'Rooms Updated'
    return True

  def leave_server(self):
    """
    Sai do servidor
    """
    if self.my_server:
      self._game_manager.GoodBye(UUID=self.uuid)
      self.my_room = None
      self.my_game = None
      self._game_manager = None
      self.my_server = None
      print 'Leaving Server'

  def choose_server(self, dev_name):
    """
    Seleciona servidor por nome do 'device'
    
    @param dev_name: nome do 'device' para selecionar servidor
    
    @type  dev_name: str
      
    @return: games
    @rtype: boolean, list
    """
    self.leave_server()
    try:
      self.my_server = self.servers[dev_name]
    except Exception, e:
      print e.message
      return False
    self._game_manager = self.my_server.services[game_manager]
    self._game_manager.event_subscribe(self.event_host,
                                    lambda x, y, z: x, None,
                                    True, lambda x, y, z: x)
    self._game_manager.subscribe_for_variable("RoomUpdate",
                                           self._get_available_rooms)
    self.uuid = self._game_manager.GetUUID()['UUID']
    return self._get_available_games()

  def choose_game(self, game_name):
    """
    Seleciona 'jogo' com 'sala' disponível
    
    @param game_name: nome do jogo a ser escolhido
        
    @type  game_name: str
     
    @return: my_game
    @rtype: boolean, list
    """
    if not self.my_server:
      return False
    try:
      self.my_game = Game(game_name)
      if self._get_available_rooms():
        return self.my_game
    except Exception, e:
      raise e

  def join_room(self, room_id):
    """
    Entra na 'sala'
    
    @param room_id: identificador da sala
       
    @type  room_id: int
       
    @rtype: boolean, Room, int
    """
    if not self.my_server or not self.my_game:
      return False
    try:
      response = self._game_manager.JoinRoom(UUID=self.uuid,
                                              Game=self.my_game.name,
                                              RoomID=room_id)['Return']
      if response == '1':
        self.my_room = self.my_game[room_id]
        return self.my_room
      else:
        return int(response)
    except Exception, e:
      raise e

  def leave_room(self):
    """
    Sai da 'sala'
       
    @rtype: boolean, int
    """
    if not self.my_server or not self.my_game or not self.my_room:
      return False
    try:
      response = self._game_manager.LeaveRoom(UUID=self.uuid,
                                             Game=self.my_game.name,
                                             RoomID=self.my_room.id)['Return']
      if response == '1':
        self.my_room = None
        return True
      else:
        return int(response)
    except Exception, e:
      raise e

  def create_room(self, max_players):
    """
    Cria 'sala'
    
    @param max_players: numero maximo de jogadores
      
    @type  max_players: int
   
    @rtype: boolean, Room, int
    """
    if not self.my_server or self.my_game is None:
      return False
    try:
      room_id = int(self._game_manager.CreateRoom(UUID=self.uuid,
                                       Game=self.my_game.name,
                                       MaxPlayers=max_players)['RoomID'])
      if room_id >= 0:
        self.my_room = Room(room_id, max_players, 1)
        return self.my_room
      else:
        return room_id
    except Exception, e:
        raise e


