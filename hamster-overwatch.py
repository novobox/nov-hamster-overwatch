#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time, datetime, thread

from popup.popup_tk import PopupTask
from hamstertools.hamster_task import HamsterCtrl

popup_timer_sec = 1000

hamster = HamsterCtrl()
p = PopupTask(hamster)

closing_hours = [
    {
        'hour': 12,
        'min' : 30,
        'sec' : 0
    },
    {
        'hour': 18,
        'min' : 00,
        'sec' : 0
    },
    ]


def get_next_closing_time():
    next_closing_time = datetime.datetime.now().replace(hour=23, minute=59, second=59) #midnight... guh
    now = datetime.datetime.now()
    for close in closing_hours:
        closetime = now.replace(hour=close['hour'], minute=close['min'], second=close['sec'])
        if closetime < next_closing_time and closetime > now:
            next_closing_time = closetime
    return next_closing_time

   
def pop():
    p.popup()
    time.sleep(popup_timer_sec)
    pop()

def countdown_autoclose():
    countdown_close = (get_next_closing_time()-datetime.datetime.now()).total_seconds()
    time.sleep(countdown_close)
    #auto_close


if __name__ == '__main__':
    #get time before auto close
    pop()
    

#plz use service or make a hamster plugin
#
## sample : SERVICE, DEAMON:
##
# import time
# from daemon import runner

# class App():
#         def __init__(self):
#             self.stdin_path = '/dev/null'
#             self.stdout_path = '/dev/tty'
#             self.stderr_path = '/dev/tty'
#             self.pidfile_path =  '/tmp/foo.pid'
#             self.pidfile_timeout = 5
#     def run(self):
#         while True:
#             print("Howdy!  Gig'em!  Whoop!")
#             time.sleep(10)

# app = App()
# daemon_runner = runner.DaemonRunner(app)
# daemon_runner.do_action()
