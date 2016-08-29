'''
Created on 09/06/2009

@author: everton
'''
import elementary

from Pager import Pager

class BrigasApp:
    
    def __init__(self, titulo, w = 800, h = 480):
        elementary.init()

        self.win = elementary.Window("janela", elementary.ELM_WIN_BASIC)
        self.win.destroy = (self.on_destroy, (self, "obj", "event", "data"))
        self.win.title_set(titulo)
        self.win.autodel_set(True)
        self.win.alpha_set(True)
        self.win.resize(w, h)
        self.win.show()
                
        self.background = elementary.Background(self.win)
        self.background.size_hint_weight_set(1, 1)
        self.background.file_set("images/angelina1.jpg")
        self.win.resize_object_add(self.background)
        self.background.show()

        self.pager = Pager(self.win)
        
    def shutdown(self):
        elementary.shutdown()

    def run(self):        
        elementary.run()

    def on_destroy(self, obj, event, data):
        elementary.exit()

    def on_games_toolbar_clicked(self, obj, event, data):
        print "toolbar clicada"        
        