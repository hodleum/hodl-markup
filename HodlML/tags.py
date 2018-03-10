'''
 HodlML  Copyright (C) 2018 HODL - The Cryptocurrency
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions;
'''
import HODL_Memory, drawing
class img:
    size = '' # normal/big/small
    url  = '' # hodl://e23edbuiqei7347yiqwuhqiudgg/image.png
    x = 0
    y = 0
    def Draw(self, x, y):
        return drawing.draw(HODL_Memory.get(self.url), self.size, x, y, type='img')
    def ChangePOS(self, x, y):
        return drawing.redraw(HODL_Memory.get(self.url), self.size, x, y, type='img')
class header:
    size  = ''
    text  = ''
    font  = 'Arial'
    color = 'black'
    def Draw(self, x, y):
        return drawing.draw(self.text, self.size, x, y, type='text', font=self.font, color=self.color)
    def ChangePOS(self, x, y):
        return drawing.redraw(self.text, self.size, x, y, type='text', font=self.font, color=self.color)