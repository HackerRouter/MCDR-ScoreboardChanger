# -*- coding: utf-8 -*-
import time


HelpMessage ='''------MCDR ScoreboardChanger------
*依赖于StatsHelper
定时自动更换右侧计分板
§a【格式说明】§r
!!sc -获取帮助信息
!!sc set [changeTrue/changeTime] [...] -设置changeTrue或changeTime的值
!!sc status -获取changeTrue值和changeTime值的信息
--------------------------------'''

#默认是否开启
changeTrue = 1
#默认换榜时间
changeTime = 10
#你想换的所有榜
scoreboards = ['used redstone 红石使用榜','used diamond_pickaxe 挖掘榜','custom time_since_rest 修仙榜','custom damage_taken 沙雕值','custom deaths 死亡榜','custom traded_with_villager py榜','custom sleep_in_bed 睡觉榜','custom aviate_one_cm 飞行榜']


def work(server, info):
  global changeTrue
  global changeTime
  if info.is_player == 1:
    if info.content.startswith('!!sc'):
      if info.content.startswith('!!sc set changeTrue '):
        changeTrue = int(info.content[20:])
        if changeTrue == 1:
          server.say('[SChanger]已开启自动换榜.')
        else:
          server.say('[SChanger]已关闭自动换榜,可能会滞后.若要开启请将该值设为1.')
      elif info.content.startswith('!!sc set changeTime '):
        changeTime = int(info.content[20:])
        server.say(str('[SChanger]已将定时更换时间改为' + changeTime + '秒'))
      else:
        server.say(HelpMessage)
    if info.content.startswith('!!sc status'):
      server.say(str('[SChanger]changeTime的值为' + changeTime))
      server.say(str('[SChanger]changeTrue的值为' + changeTrue))

def change(server, old):
  global changeTrue
  global changeTime
  while True:
    if changeTrue != 1:
      return False
    for i in scoreboards:
      server.execute(str('!!stats scoreboard ' + i))
      time.sleep( changeTime )
    

def on_load(server, old):
  server.add_help_message('!!sc', '自动更换计分板')
  while True:
    change(server, old)
# MCDaemon
def onServerInfo(server, info):
  if info.isPlayer == 1:
    work(server, info)


# MCDReforged
def on_info(server, info):
  if info.is_player:
    work(server, info)
