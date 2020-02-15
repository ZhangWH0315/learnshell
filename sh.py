# -*-coding:utf-8-*-


import time

idx = 0
while idx < 5:
    now_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now_time)))
    time.sleep(1)
    idx += 1
