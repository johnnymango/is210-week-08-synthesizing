#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm Clock."""


DAY = raw_input('What day is it? ')

TIME = int(raw_input('What time is it? '))

MYTEST = (DAY[:3].lower() == 'sat' or DAY[:3].lower() == 'sun') or TIME <= 600

SNOOZE = 'Beep! Beep! Beep! Beep! Beep!' if not MYTEST else True

print SNOOZE