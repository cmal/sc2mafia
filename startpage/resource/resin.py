#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of Human Resource System of BQD Jinan Branch.
#
# File: resin.py
# Description: Resource (e.g. icons) loader.
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import wx
import os

import logging
log = logging.getLogger('resource')

class Resin:
    """Resource (e.g. icon) loader.

    Returns icons as `wx.Icon`s.

    """
    def getIcon(self, filename):
        """Returns an icon (*.ico) with the specified  filename from
        the archive as a `wx.Icon`.

        """
        if not filename.endswith(".ico"):
            filename = filename + ".ico"

        log.debug("Successfully got '%s'" % filename)
        return wx.Icon(os.path.join(homepath, 'res', filename), wx.BITMAP_TYPE_ICO)
