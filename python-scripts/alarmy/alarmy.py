#!/usr/bin/env python
from datetime import datetime as dt
from time import sleep
from random import choice
from os import system, listdir


def now_time():
    return f'{dt.now().hour:02d}:{dt.now().minute:02d}'


def alarm():
    alarm_time = str(input('Enter when the alarm should go off:\t'))
    print(f'Alarm set for:\t{alarm_time}')
    while True:
        if now_time() != alarm_time:
            print(f'\rCurrent time:\t{now_time()}', end='\r')
            sleep(1)
        else:
            #   os.system(f'vlc "How to get people to DO WHAT YOU WANT _ Ryan Serhant Vlog #54.mp4"')
            print(f'vlc "{media()}"')
            system(f'vlc "{media()}"')


def media():
    media_files = [
        item for item in listdir()
        if 'mp4' in item or 'mkv' in item
    ]
    return choice(media_files)


alarm()
