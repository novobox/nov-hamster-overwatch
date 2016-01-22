#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time

from popup.popup_tk import PopupTask
from hamstertools.hamster_task import HamsterCtrl

hamster = HamsterCtrl()
p = PopupTask(hamster)

def pop():
    p.popup()
    time.sleep(1000)
    pop()
    
if __name__ == '__main__':
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
