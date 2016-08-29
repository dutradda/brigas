'''
Created on 17/06/2009

@author: everton
'''
import elementary

from Page import Page

class LobbyPage(Page):


    def __init__(self, parent_win, pager):
        Page.__init__(self, parent_win, pager)
            
        self.icon = elementary.Icon(parent_win)
        self.icon.file_set("images/icone.jpg")
        
        self.games_toolbar = elementary.Toolbar(parent_win)
        self.games_toolbar.item_add(self.icon, "Truco", None).select()
        self.games_toolbar.size_hint_align_set(-1,0)
        self.main_box.pack_end(self.games_toolbar)
        self.games_toolbar.show()
                        
        self.salas_list = elementary.List(parent_win)
        self.salas_list.size_hint_weight_set(1,1)
        self.salas_list.size_hint_align_set(-1,-1)
        self.main_box.pack_end(self.salas_list)
        self.salas_list.show()   
        
        self.add_room("Sala 01", 0, 4)
        self.add_room("Sala 02", 0, 4)
        self.add_room("Sala 03", 0, 4)

        self.salas_list.go()
            
        self.box_buttons = elementary.Box(parent_win)
        self.box_buttons.size_hint_align_set(0, 0)
        self.box_buttons.horizontal_set(True)
        self.main_box.pack_end(self.box_buttons)
        self.box_buttons.show()
        
        self.enter_button = elementary.Button(parent_win)
        self.enter_button.label_set("Entrar")
        self.enter_button.clicked = self.enter_button_click
        self.enter_button.size_hint_align_set(0, 0)
        self.box_buttons.pack_end(self.enter_button)
        self.enter_button.show()

        self.exit_button = elementary.Button(parent_win)
        self.exit_button.label_set("Sair do jogo")
        self.exit_button.clicked = self.exit_button_click
        self.exit_button.size_hint_align_set(0, 0)
        self.box_buttons.pack_end(self.exit_button)
        self.exit_button.show()

    def enter_button_click(self, obj, event, data):
        if(self.pager.data["selected_room"] != None):
            self.pager.content_promote(self.pager.data["GamePage"])

    def exit_button_click(self, obj, event, data):
        elementary.exit()
    
    def room_itemlist_click(self, obj, event, data):
        self.pager.data["selected_room"] = obj 

    def add_room(self, name, ocupped, available): 
        self.salas_list.item_append(name + " (" + ocupped.__str__() + "/" + available.__str__() + ")", None, None, self.room_itemlist_click)
    