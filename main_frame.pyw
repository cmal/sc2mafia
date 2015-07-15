#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of sc2mafia.
#
# File: main_frame.pyw
# Description: Main file -- application entry point (without console window).
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
#
# Copyright (C) 2015-2016 Yu Zhao.
#
#==============================================================================

import sys
import imp

if __name__ == '__main__':
    # just load 'main_frame.py', except without the console window popping up
    sys.modules['notmain'] = sys.modules['__main__']
    sys.modules['__main__'] = imp.load_source(
            '__main__', 'main_frame.py', open('main_frame.py'))
