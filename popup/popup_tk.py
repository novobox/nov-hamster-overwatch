#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from Tkinter import *

class PopupTask(object):

    def __init__(self, hamster):
        #plz use interface
        self._hamster = hamster
    
    def fexit(self):
        self.fenetre.destroy()

    def command_exit(self):
        sys.exit(1)
        
    def command_stop_tracking(self):
        self._hamster.stop_track()
        self.fexit()

    def command_start_tracking(self):
        self._hamster.start_track(self.ent.get())
        self.fexit()

    def popup(self):

        self.fenetre = Tk()
        self.fenetre.title("Im watching you")
            
        label = Label(self.fenetre, text="Hamster Overwatch v0.1")
        label.pack()

        # bouton de sortie
        bouton=Button(self.fenetre, text="Stop Tracking", command=self.command_stop_tracking)
        bouton.pack()

        valtaskname = StringVar()
        valtaskname.set(self._hamster.current_activity)
        self.ent = Entry(self.fenetre, textvariable=valtaskname, width=10)
        self.ent.pack()
        
            # bouton de sortie
        bouton=Button(self.fenetre, text="Start Tracking", command=self.command_start_tracking)
        bouton.pack()

        bouton=Button(self.fenetre, text="Arreter (exit program)", command=self.command_exit)
        bouton.pack()

        self.fenetre.mainloop()
