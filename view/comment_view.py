# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/18 19:00
@Author  : linkey
@Email   : i@hello.faith
@File    : comment_view.py

"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "/..")))

import multiprocessing
import  time
from action import commentaction
from action import songaction
from util import getsinglesongallcomment_util
import datetime

def GetAllCommentOfAllSongOfSomeOne(step,coreTotal,listenerid):
    #获取歌所有歌曲id
    SongAction = songaction.SongAction()
    CommentAction = commentaction.CommentAction()
    ans, AllSongOfSomeone = SongAction.ShowAllSong(listenerid)

    i = 0

    while i < len(AllSongOfSomeone):
        if i % coreTotal == step:
            #获取要爬取的歌的
            songid = AllSongOfSomeone[i][0]
            #验证是否爬完
            finish = SongAction.GetFinish(songid)
            if finish == 1:
                print("进程",step,  '歌曲：',songid,"评论已经完全获取, 自动跳过")
                #time.sleep(0.5)
            elif finish == 0:
                #最新修改，直接建库,若已经含有该库会自动跳过
                CommentAction.CreatTable(songid)

                #直接爬，面向过程吧，
                ans = getsinglesongallcomment_util.main(songid,step)
                if ans == 0:
                    i = i - 1  #报错的话，退回重新获取
                    now = datetime.datetime.now()

                    print("进程",step,"getsinglesongallcomment_util模块出错, 后退一步     当前时间： ",now)
                    time.sleep(5)
                elif ans == 1:
                    SongAction.UpdateFinish(songid)            #爬完了标注一下
                    print("进程",step,"finish字段修改成功",  '歌曲：',songid,"评论已经完全获取")
                    time.sleep(3)

        i += 1


def poolProcess():
    print("输入听众的id")
    listenerid = input()

    coreTotal = multiprocessing.cpu_count()   #核的数量，也就是线程的个数
    workingcoreTotal = int(coreTotal/2) - 1               #可能我孤陋寡闻没见过 ，3/5/7/9核的机器
    workingcoreTotal = 1
    pool = multiprocessing.Pool(workingcoreTotal)
    for step in range(0,workingcoreTotal):    #step 线程排名 从 0 开始  暗含一个条件   step <  workingcoreTotal    等于都不行
        pool.apply_async(GetAllCommentOfAllSongOfSomeOne,args=(step,workingcoreTotal,listenerid))

    pool.close()
    pool.join()
    print('所有线程结束')






def main(command):
    if command == "5":
        poolProcess()