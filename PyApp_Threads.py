# -*- coding: utf-8 -*-
"""
Program Thread_tutorial

Created on Tue Apr 19 22:46:00 2023

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""


import os
from time import time, sleep
from multiprocessing import Process, Queue
from queue import Empty

import str_common as strc


def selfdoc():
    print(
        ''' 
        === Any tests threads & process on Python ==============================  
               
        q = Queue()      #--- Очередь для процессов

        #--- процессы p0,p1,p2,p3 создаются и запускаются из главного приложения'
        
        #--- их можно поместить в список pp для удобства
        
        #--- потом запустить в цикле списка pp
        
        #--- Также запускаем 2 потока    stop = Stop()  и  alarm = Clock()   
        
        #--- Поток stop отработав свое выдает "0" и главный цикл потоков завершается
        
        #--- В конце завершить процессы с пом join, ибо они демоны

        Самодокументируемый текст прораммы не требует подробных комментариев

        =======================================================================
        '''
    )

def print_word(word, slp, cnt):
    global COUNT
    COUNT = 0
    for i in range(cnt):
        print(f'Fn[0]: Hello, {word} !!!, [{COUNT}]')
        COUNT += 1
        sleep(slp)

def print2_word(word, slp, cnt):
    global COUNT
    COUNT = 1000
    for i in range(cnt):
        print(f'Fn[1]: Hello, {word} !!!, [{COUNT}]')
        COUNT -= 1
        sleep(slp)

def Stop():
    maxcnt = 0
    for i in os.walk('E:\\'):
        maxcnt += 1
        if(maxcnt > 20):
            yield "0"
        else:
            yield i[0]

def Proc(lim, slp):
    global COUNT
    COUNT = lim
    for i in range(COUNT):
        print(f'Fn[*** Process ***]: [{COUNT}]')
        COUNT -= 1
        sleep(slp)

def QueueInProcess(lim, slp, q: Queue=None):
    global COUNT
    COUNT = lim
    for i in range(COUNT):
        print(f'Fn[***qqq***]: [{COUNT}]')
        q.put(COUNT)
        COUNT -= 1
        sleep(slp)
    print("QueryInProcess: Ended!!!")


def Clock():
    time0 = round(time())
    T = 2
    while(True):
        if((round(time()) - time0) % T == 0):
            yield f'*** Alarm: {T} sec ***'
        else:
            yield False

def main():

    print()

    strc.titleprogram("Set of methods with threads and process",
                      "Any tests multithreading & multiprocessing",
                      "ln.starmark@gmail.com")

    selfdoc()

    #--- Очередь для процессов
    q = Queue()

    strc.zagolovok("Процессы создаются и запускаются из главного приложения")

    p0 = Process(target=print_word, args=('bob',1,20), daemon=True)
    p1 = Process(target=print2_word, args=('alice',2,30), daemon=True)
    p2 = Process(target=Proc, args=(30, 1), daemon=True)
    p3 = Process(target=QueueInProcess, args=(30, 1, q), daemon=True)
    #--- поместить в список для удобства
    pp = [p0,p1,p2,p3]

    for p in pp:
        p.start()
        sleep(0.11)

    strc.zagolovok("Потоки создаются и запускаются из главного приложения")

    #--- переменные-функции для потоков в прилохении main()
    stop = Stop()
    alarm = Clock()

    while(True):
        stp = next(stop)
        a = next(alarm)

        if(stp == "0"):
            #--- в этом цикле будет выход,
            #--- а ост. процессы завершат p*.join()
            break
            
        else:
            if (a):
                print(a)
            sleep(1)

            print(stp)

            try:
                val = q.get()
                print(f"From q -> {val}")
            except Empty as Err:
                print(Err)

    strc.zagolovok("Не забыть завершить процессы, ибо они демоны")

    for p in pp:
        p.join()


if __name__ == '__main__':
    main()

