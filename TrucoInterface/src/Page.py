'''
Created on 17/06/2009

@author: everton
'''
import elementary

class Page(object):

    def register(self, name):
        self.pager.content_push(self.main_box)
        self.pager.data[name] = self.main_box
        
    def __init__(self, parent_win, pager):
        self.pager = pager
                
        self.main_box = elementary.Box(parent_win)
        self.main_box.size_hint_weight_set(1, 1)
        