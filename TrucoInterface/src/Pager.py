'''
Created on 17/06/2009

@author: everton
'''
import elementary

from LobbyPage import LobbyPage
from GamePage import GamePage

class Pager:

    def __init__(self, parent_win):       
        self.pager = elementary.Pager(parent_win)
        parent_win.resize_object_add(self.pager)
        self.pager.size_hint_weight_set(1,1)
        self.pager.show()
        
        self.data = dict()
        
        self.lobby_page = LobbyPage(parent_win, self.pager)
        self.game_page = GamePage(parent_win, self.pager)

        self.game_page.register("GamePage")
        self.lobby_page.register("LobbyPage")
        
