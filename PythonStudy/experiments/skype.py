# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

import Skype4Py

def connect():
    s = Skype4Py.Skype()
    s.Attach()
    return s

def disconnect(s):
    pass
def set_status(s, status):
    s.CurrentUserStatus=status

def set_online(s):
    set_status(s, Skype4Py.cusOnline)

def set_dnd(s):
    set_status(s, Skype4Py.cusDoNotDisturb)

if __name__ == '__main__':
    s = connect()
    if s.CurrentUserStatus == Skype4Py.cusOnline:
        set_dnd(s)
    if s.CurrentUserStatus == Skype4Py.cusDoNotDisturb:
        set_online(s)
    disconnect(s)