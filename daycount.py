# -*- coding: utf-8 -*-
import datetime

startday = datetime.datetime.strptime('2018-11-09', '%Y-%m-%d')

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!day'):
      now = datetime.datetime.now()
      output = now - startday
      server.say('今天是这个服务器开服的第' + str(output.days) + '天')