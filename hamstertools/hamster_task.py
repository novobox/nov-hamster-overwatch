#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class TrackActiv(object):
    active = 1

class TrackStandBy(object):
    active = 0

class HamsterCtrl(object):

    current_activity = ''
    start=TrackStandBy.active
    
    def _init_(self):
        self.start=TrackStandBy.active
        self.current_activity = ''

    def command_start_track(self, activity):
        os.system("hamster-cli start %s" % activity)
        
    def command_stop_track(self):
        os.system("hamster-cli stop")

    def start_track(self, requestactivity):
        if self.current_activity != requestactivity or self.start == TrackStandBy.active :
             self.current_activity = requestactivity
             #commands
             self.command_stop_track()
             self.command_start_track(requestactivity)
             print "Start new activity: %s" % self.current_activity
        else:
             print "Continue activity: %s" % self.current_activity
        self.start = TrackActiv.active

    def stop_track(self):
        print "StandBy tracking"   
        self.start=TrackStandBy.active
        self.command_stop_track()
