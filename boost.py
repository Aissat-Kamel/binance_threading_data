import threading


def boost(callback, assets, interval, depth):
    thread_list = []
    for i in range(len(assets)):
        th = threading.Thread(target = callback, args = (assets[i], interval, depth))
        thread_list.append(th)
        th.start()
    for thrd in thread_list:
        thrd.join()
