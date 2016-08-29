# coding=utf-8

#
#Implementação do "GameManager" [utiliza XML]
#

import os
from uuid import uuid4

from brisa.upnp.device.service import Service

from brisa_game_server.services.xmls import xml_path

service_name = 'GameManager'
service_type = 'urn:ic-ufal-br:service:GameManager:1'
scpd_xml_path = os.path.join(xml_path, 'game-manager-scpd.xml')


class GameManager(Service):
  """
  Classe correspondente ao 'GameManager'
  """
  
  def __init__(self, games):
    Service.__init__(self, service_name, service_type, '', scpd_xml_path)
    self._games = games
    self._players = []
    self._room_update = 0

  def _check_uuid(self, uuid):
    """
    Constata validade de UUID
      
    @param uuid: identificador de jogador
  
    @type  uuid: str
       
    @rtype: boolean
    """
    if uuid in self._players:
      for game in self._games.values():
        for room in game.rooms.values():
          if uuid in room.players:
            return False
      return True
    else:
      return False

  def soap_GetUUID(self, *args, **kwargs):
    """
    Obtem UUID unica (para jogador)
        
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                               
    @type  *args: tuple
    @type  **kwargs: dict
     
    @return: {'UUID' : uuid}
    @rtype:  dict
    """
    uuid = str(uuid4())
    for i in range(len(self._players)):
      if self._players[i] == uuid:
        uuid = str(uuid4())
        i -= 1
    self._players.append(uuid)
    return {'UUID' : uuid}

  def soap_GetAvailableGames(self, *args, **kwargs):
    """
    Obtem lista de jogos disponíveis
      
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                            
    @type  *args: tuple
    @type  **kwargs: dict
     
    @return: {'Games' : games}
    @rtype:  dict
    """
    games = ':'.join(self._games.keys())
    return {'Games' : games}

  def soap_GetAvailableRooms(self, *args, **kwargs):
    """
    Obtem salas disponíveis
       
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                            
    @type  *args: tuple
    @type  **kwargs: dict
     
    @rtype: dict
    """
    try:
      game = self._games[kwargs['Game']]
      rooms = []
      for room in game.rooms.values():
        if not room.match_started:
          rooms.append(room)
      rooms_id = ':'.join([str(room.id) for room in rooms])
      max_players = ':'.join([str((room.max_players)) for room in rooms])
      num_players = ':'.join([str(len(room.players)) for room in rooms])
      return {'RoomsID' : rooms_id,
              'MaxPlayers' : max_players,
              'NumPlayers' : num_players}
    except Exception, e:
      print e.message
      return {'RoomsID' : '-1', 'MaxPlayers' : '-1', 'NumPlayers' : '-1'}

  def soap_CreateRoom(self, *args, **kwargs):
    """
    Cria 'sala'
    
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                            
    @type  *args: tuple
    @type  **kwargs: dict
     
    @return: {'RoomID' : room_id}
    @rtype:  dict
    """
    uuid = kwargs['UUID']
    if self._check_uuid(uuid):
      try:
        game = self._games[kwargs['Game']]
        max_players = int(kwargs['MaxPlayers'])
        room_id = game.add_room(uuid, max_players)
        self._room_update += 1
        self.set_state_variable('RoomUpdate', self._room_update)
        return {'RoomID' : room_id}
      except Exception, e:
        print e.message
        return {'RoomID' : -2}
    else:
      return {'RoomID' : -3}

  def soap_JoinRoom(self, *args, **kwargs):
    """
    Entra em 'sala'
        
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                            
    @type  *args: tuple
    @type  **kwargs: dict
     
    @return: {'Return' : room_update}
    @rtype:  dict
    """
    try:
      game = self._games[kwargs['Game']]
      room_id = int(kwargs['RoomID'])
      uuid = kwargs['UUID']
      if self._check_uuid(uuid):
        try:
          if game.rooms[room_id].add_player(uuid):
            self._room_update += 1
            self.set_state_variable('RoomUpdate', self._room_update)
            return {'Return' : 1}
          else:
            return {'Return' : 0}
        except Exception, e:
          print e.message
          return {'Return' : -1}
      else:
        return {'Return' : -2}
    except Exception, e:
      print e.message
      return {'Return' : -3}

  def soap_LeaveRoom(self, *args, **kwargs):
    """
    Sai da 'sala'
  
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                            
    @type  *args: tuple
    @type  **kwargs: dict
     
    @return: {'Return' : room_update}
    @rtype:  dict
    """
    try:
      game = self._games[kwargs['Game']]
      room_id = int(kwargs['RoomID'])
      uuid = kwargs['UUID']
      try:
        if game.rooms[room_id].remove_player(uuid):
          self._room_update += 1
          self.set_state_variable('RoomUpdate', str(self._room_update))
          return {'Return' : 1}
        else:
          return {'Return' : 0}
      except Exception, e:
        print e.message
        return {'Return' : -1}
    except Exception, e:
      print e.message
      return {'Return' : -2}

  def soap_GoodBye(self, *args, **kwargs):
    """
    Finaliza servico
       
    @param *args: lista de argumentos, com tamanho varia'vel
    @param **kwargs: lista de argumentos que utilizam palavras chave,
                        com tamanho variavel
                                            
    @type  *args: tuple
    @type  **kwargs: dict
     
    @return: {'Return' : value}
    @rtype:  dict
    """
    uuid = kwargs['UUID']
    try:
      self._players.remove(uuid)
      return {'Return' : 1}
    except Exception, e:
      print e.message
      return {'Return' : 0}
      
