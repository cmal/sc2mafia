#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of sc2mafia.
#
# File: config.py
# Description: Reader for the config file.
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import ConfigParser

class Config:
    """Read/write the config file.
    """
    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser.RawConfigParser()
        self.read()
        
    def read(self):
        self.config.read(self.filename)

    def get(self, *args, **kwargs):
        return self.config.get(*args, **kwargs)
        
    def set(self, section, option, value):
        self.config.set(section, option, value)
        self.save()

    def save(self):
        with open(self.filename, 'wb') as configfile:
            self.config.write(configfile)
