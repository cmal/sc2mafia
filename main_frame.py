#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of sc2mafia.
#
# File: main_frame.py
# Description: Main file -- application entry point.
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
#
# Copyright (C) 2015-2016 Yu Zhao.
#
#==============================================================================

import __builtin__
import logging
import os.path
import sys
import wx
import crashonipy # ipython 调试环境
from startpage.window import StartpageWindow



# The next line deals with a known path problem in wxPython
abs_path = os.path.dirname(sys.argv[0])
__builtin__.__dict__['homepath'] = os.path.abspath(abs_path)
__builtin__.__dict__['_'] = lambda x: x  # TODO: later, include locales

# Set up loggers programmatically (we want to hard-code the file location
# based on `homepath`, which we can't do with a configuration file)
for name in ['application', 'window', 'resource']:
    logger = logging.getLogger(name)
    filehandler = logging.FileHandler(os.path.join(homepath, 'sc2mafia.log'))
    formatter = logging.Formatter(
            '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)

# Now set this file's specific logger
log = logging.getLogger('application')


class Sc2mafiaApp(wx.App):
    """Application class for the sc2mafia application."""

    def OnInit(self):
        self.frame = StartpageWindow(None, -1, u"sc2mafia",
                wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)

        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        log.debug('Initialized')

        # OnInit must return a boolean
        return True

if __name__ == "__main__":  # if called as a script, and not as a module
    app = Sc2mafiaApp(0)

    # Pop the first argument, which is the program itself
    sys.argv.pop(0)

    # If there are any system arguments left
    if len(sys.argv):
        pass

    # Start up the application -- if we do this before app.OpenFile, the
    # HumanResourceWindow object is deleted and we get a memory access error
    app.MainLoop()

    log.debug('Finished main loop -- exiting.')
