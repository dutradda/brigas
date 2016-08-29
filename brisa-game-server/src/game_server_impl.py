# coding=utf-8
#
# Brisa Game Server Implementation
#

# Para poder montar estrutura hierárquica de pastas
from os import walk

from brisa.core.reactors import GLib2Reactor
reactor = GLib2Reactor()

from brisa.core import log
from brisa.upnp.device import Device

import brisa_game_server
from brisa_game_server.services import GameManager


class GameServerDevice(object):
  """
  Classe do Servidor do BRiGaS
  """
  # Localização dos 'games'
  games_folder = brisa_game_server.__path__[0] + "/games"
  games_module_path = "brisa_game_server.games"

  # Construtor
  def __init__(self, server_name, listen_url):
    self._server_name = server_name
    self._listen_url = listen_url
    self._games = {}
    self.device = None

  def _create_device(self):
    """
    Cria 'device' padronizado
    """
    project_page = 'http://launchpad.net/brigas'
    self.device = Device('urn:ic-ufal-br:device:GameServer:1',
                         self._server_name,
                         force_listen_url=self._listen_url,
                         manufacturer='BRiGaS Team. UFAL students',
                         manufacturer_url=project_page,
                         model_description='An Opensource UPnP Game Server',
                         model_name = 'BRisa Game Server version 0.1',
                         model_number='0.1',
                         model_url=project_page,
                         serial_number='01'.rjust(7, '0'))

  def _add_games(self):
    """
    Adiciona 'games'
    """
    # Procura pelo primeiro caminho que termine na pasta 'games'
    for root, dirs, files in walk(self.games_folder):
        if root.endswith("games"):
          break

    for dir in dirs:
      try:
        # Importa módulo do 'game'
        module_path = "%s.%s" % (self.games_module_path, dir)
        __import__(module_path)
        game = eval("%s.%s()" % (module_path, eval(module_path).service_name))
        self._games[game.id] = game
        self.device.add_service(game)
      except Exception, e:
        msg = 'Error while importing %s game. The module '\
              'path used to load was: %s. Error: %s' % \
              (dir, self.games_folder, e)
        log.error(msg)

  def _add_services(self):
    """
    Adiciona servicos
    """
    self._add_games()
    self.device.add_service(GameManager(self._games))

  def start(self):
    """
    Inicializa os servicos
    """
    self._create_device()
    self._add_services()
    self.device.start()
    reactor.add_after_stop_func(self.device.stop)
    reactor.main()

