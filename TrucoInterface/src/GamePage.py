'''
Created on 17/06/2009

@author: everton
'''
import elementary

from Page import Page

class GamePage(Page):


    def __init__(self, parent_win, pager):
        Page.__init__(self, parent_win, pager)        
        
        # Top box
        self.top_box = elementary.Box(parent_win)
        self.top_box.size_hint_weight_set(1, 1)        
        self.top_box.show()
        
        icon = elementary.Icon(parent_win)
        icon.file_set("images/carta virada.png")
        icon.scale_set(0, 0)
        icon.show()
        self.player_top = elementary.Button(parent_win)
        self.player_top.icon_set(icon)
        self.player_top.size_hint_align_set(0, 0)        
        self.player_top.show()
        self.top_label = elementary.Label(parent_win)
        self.top_label.label_set("Jogador top")
        self.top_label.show()
        
        self.top_box.pack_end(self.player_top)
        self.top_box.pack_end(self.top_label)
        
        
        # Middle box
        self.middle_box = elementary.Box(parent_win)
        self.middle_box.horizontal_set(True)
        parent_win.resize_object_add(self.middle_box)
        self.middle_box.size_hint_weight_set(1, 1)
        self.middle_box.show()
                
        self.left_box = elementary.Box(parent_win)
        self.left_box.size_hint_align_set(0.25,-1)
        self.left_box.size_hint_weight_set(1,1)
        self.left_box.show()
        icon = elementary.Icon(parent_win)
        icon.file_set("images/carta virada.png")
        icon.scale_set(0, 0)
        icon.show()
        self.player_left = elementary.Button(parent_win)
        self.player_left.icon_set(icon)
        self.player_left.show()
        self.left_label = elementary.Label(parent_win)
        self.left_label.label_set("Jogador left")
        self.left_label.show()
        self.left_box.pack_end(self.player_left)
        self.left_box.pack_end(self.left_label)

        self.right_box = elementary.Box(parent_win)
        self.right_box.size_hint_align_set(0.75,-1)
        self.right_box.size_hint_weight_set(1,1)
        self.right_box.show()
        icon = elementary.Icon(parent_win)
        icon.file_set("images/carta virada.png")
        icon.scale_set(0, 0)
        icon.show()
        self.player_right = elementary.Button(parent_win)
        self.player_right.icon_set(icon)
        self.player_right.show()
        self.right_label = elementary.Label(parent_win)
        self.right_label.label_set("Jogador right")
        self.right_label.show()
        self.right_box.pack_end(self.player_right)
        self.right_box.pack_end(self.right_label)

        self.middle_box.pack_end(self.left_box)
        self.middle_box.pack_end(self.right_box)
        
        # Bottom box
        self.bottom_box = elementary.Box(parent_win)
        self.bottom_box.size_hint_weight_set(1, 1)
        self.bottom_box.show()

        icon = elementary.Icon(parent_win)
        icon.file_set("images/carta virada.png")
        icon.scale_set(0, 0)
        icon.show()
        self.player_bottom = elementary.Button(parent_win)
        self.player_bottom.icon_set(icon)
        self.player_bottom.show()
        self.bottom_label = elementary.Label(parent_win)
        self.bottom_label.label_set("Jogador voce")
        self.bottom_label.show()
        self.bottom_box.pack_end(self.player_bottom)
        self.bottom_box.pack_end(self.bottom_label)
        
# ------------------------------------------------------------------------
        self.mycards_box = elementary.Box(parent_win)
        self.mycards_box.size_hint_weight_set(1, 1)
        self.mycards_box.show()

        self.hover = elementary.Hover(parent_win)
        self.hover.style_set("popout")
        
        self.mycards_button = elementary.Button(parent_win)
        self.mycards_button.label_set("Minhas cartas")
        self.mycards_button.clicked = (self.hover_bt_click, self.hover)
        self.mycards_button.show()
#        self.bottom_box.pack_end(self.mycards_button)

        self.hover.parent_set(parent_win)
        self.hover.target_set(self.mycards_button)
        
        self.mycards_button2 = elementary.Button(parent_win)
        self.mycards_button2.label_set("Jogar a carta...")
        self.mycards_button2.show()
        self.hover.content_set("middle", self.mycards_button2)

        # Carta 1
        icon = elementary.Icon(parent_win)
        icon.file_set("images/as.png")
        icon.scale_set(0, 0)
        icon.show()
        self.mycard1 = elementary.Button(parent_win)
        self.mycard1.icon_set(icon)
        self.mycard1.show()
        self.mycards_box.pack_end(self.mycard1)
        
        #Carta 2
        icon = elementary.Icon(parent_win)
        icon.file_set("images/as.png")
        icon.scale_set(0, 0)
        icon.show()        
        self.mycard2 = elementary.Button(parent_win)
        self.mycard2.icon_set(icon)
        self.mycard2.show()
        self.mycards_box.pack_end(self.mycard2)
        
        # Carta 3
        icon = elementary.Icon(parent_win)
        icon.file_set("images/as.png")
        icon.scale_set(0, 0)
        icon.show()
        self.mycard3 = elementary.Button(parent_win)
        self.mycard3.icon_set(icon)
        self.mycard3.show()
        self.mycards_box.pack_end(self.mycard3)

        self.hover.content_set("top", self.mycards_box)
        
#--------------------------------------------------------------------------------------        
        self.buttons_box = elementary.Box(parent_win)
        self.buttons_box.horizontal_set(True)
        self.buttons_box.size_hint_align_set(0,1)
        self.buttons_box.size_hint_weight_set(1,1)
        self.buttons_box.show()
        
        self.send_button = elementary.Button(parent_win)
        self.send_button.label_set("Enviar mensagem")
        self.send_button.clicked = self.send_button_click
        self.send_button.show()

        self.exit_button = elementary.Button(parent_win)
        self.exit_button.label_set("Sair da sala")
        self.exit_button.clicked = self.exit_button_click
        self.exit_button.show()

        self.buttons_box.pack_end(self.mycards_button)
        self.buttons_box.pack_end(self.send_button)
        self.buttons_box.pack_end(self.exit_button)

        self.main_box.pack_end(self.top_box)
        self.main_box.pack_end(self.middle_box)
        self.main_box.pack_end(self.bottom_box)
        self.main_box.pack_end(self.buttons_box)

    def hover_bt_click(self, obj, event, data):
        data.show()
    
    def exit_button_click(self, obj, event, data):
        self.pager.content_promote(self.pager.data["LobbyPage"])

    def send_button_click(self, obj, event, data):
        print "enviou mensagem"
        