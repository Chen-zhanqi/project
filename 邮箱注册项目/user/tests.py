# from django.test import TestCase

# Create your tests here.


import datetime
import time


if __name__ == '__main__':

    today = datetime.datetime.now()
    # timetuple() 将datetime转换为元组形式
    print(today.timetuple())
    # 将元组形式时间转换为时间戳
    print(time.mktime(today.timetuple()))

    prie_time = today + datetime.timedelta(days=7)
    print(time.mktime(prie_time.timetuple()))
