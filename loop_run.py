#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


while True:
    from datetime import datetime
    today = datetime.today()
    print(today)
    print()

    from main import run
    run()

    print('\n\n' + '-' * 20 + '\n\n')

    # Every 12 hours
    from datetime import timedelta
    today = datetime.today()
    timeout_date = today + timedelta(hours=12)

    while today <= timeout_date:
        def str_timedelta(td):
            mm, ss = divmod(td.seconds, 60)
            hh, mm = divmod(mm, 60)
            return "%d:%02d:%02d" % (hh, mm, ss)

        left = timeout_date - today
        left = str_timedelta(left)

        print('\r' * 50, end='')
        print('До следующего запуска осталось {}'.format(left), end='')

        import sys
        sys.stdout.flush()

        # Delay 1 seconds
        import time
        time.sleep(1)

        today = datetime.today()

    print('\r' * 50, end='')
    print('\n')
