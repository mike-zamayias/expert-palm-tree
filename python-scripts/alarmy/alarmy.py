#!/usr/bin/env python3
from time import sleep
from datetime import datetime
from os import system as run

run('clear')

alarm = 'Navy Seal Commander explains why wake up at 4am.mp4'
alarm_time = [5, 45]
print(f'Alarm time:\t{alarm_time[0]:02d}:{alarm_time[1]:02d}')

while True:
    current_time = [datetime.now().hour, datetime.now().minute]
    print(f'\rCurrent time:\t{current_time[0]:02d}:{current_time[1]:02d}', end='\r')
    if current_time == alarm_time:
        break
    else:
        sleep(1)

run(f'vlc {alarm}')
