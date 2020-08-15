import sys as _py
import os as _os
def path(self) :
    return _py.path(self)[2]
def init(self) :
    _os.system("start "+path(self)) # Windows
