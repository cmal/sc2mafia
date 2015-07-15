#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of sc2mafia.
#
# File: chat\client.py
# Description: Central file for all HRS GUI code.
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import socket
#socket通信客户端 example
def client():
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect(('127.0.0.1',5273))
    mysocket.send('hello')
    while 1:
        data=mysocket.recv(1024)
        if data:
           print data
        else:
            break
    mysocket.close()
client()

class Client:
  pass
