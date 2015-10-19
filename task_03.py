#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mortgage."""

import decimal


NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the amount of your principal? '))
YEARS = int(raw_input('For how many years is the loan being borrowed? '))
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

if QUALIFIED[:1].lower() in ['y', 'n']:
    if 1 <= YEARS <= 30:
        if PRINCIPAL <= 199999:
            if 1 <= YEARS <= 15:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0363')
                else:
                    RATE = decimal.Decimal('.0465')

            if 16 <= YEARS <= 20:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0404')
                else:
                    RATE = decimal.Decimal('.0498')

            if 21 <= YEARS <= 30:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0577')
                else:
                    RATE = decimal.Decimal('.0639')

        elif 200000 <= PRINCIPAL <= 999999:
            if 1 <= YEARS <= 15:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0302')
                else:
                    RATE = decimal.Decimal('.0398')

            if 16 <= YEARS <= 20:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0327')
                else:
                    RATE = decimal.Decimal('.0408')

            if 21 <= YEARS <= 30:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0466')
                else:
                    RATE = 'None'

        elif PRINCIPAL >= 1000000:
            if 1 <= YEARS <= 15:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0205')
                else:
                    RATE = 'None'

            if 16 <= YEARS <= 20:
                if QUALIFIED[0].lower() == 'y':
                    RATE = decimal.Decimal('.0262')
                else:
                    RATE = 'None'

            if 21 <= YEARS <= 30:
                RATE = 'None'

        if RATE != 'None':
            N = 12
            AMORT = PRINCIPAL * ((1 + RATE / N)**(N*YEARS))
            REPORT = """
            Loan Report for: {}
            -----------------------------------------
            Principal:              ${:,}
            Duration:               {}yrs
            Pre-qualified?:         {}

            Total:                  ${:,}

            """.format(NAME.title(), PRINCIPAL, YEARS, QUALIFIED.title(),
                       int(round(AMORT)))
            print REPORT
        else:
            print 'There is no available rate.'
    else:
        print 'You must enter a duration between 1 and 30 years.'
else:
    print 'For Pre-Qualified, you must enter Yes or No.'
