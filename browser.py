"""
It is the browser for HODL markup.
"""
import sc_get
import parser
from objects import *
from sc_net_api import *


class Malware(Exception):
    pass


class Page:
    def __init__(self, addr):
        self.addr = addr
        self.code = sc_get.get(addr.split('/')[0], '/'.join(addr.split('/')[1:]))
        if not parser.secure(self.code):
            raise Malware
        self.root = HODLmlRootWidget()

    def show(self):
        self.elements = []
        for line in self.code:
            exec(line)
        for e in self.elements:
            self.root.add_widget(e)
        return self.root

