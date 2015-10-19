#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Room Paint Selection."""


BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"? ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or '
                       '"Cumulus Nimbus"? ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color, "Basic White" or '
                              '"White"? ')
    if ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input('Which highlight color, "Off White" or '
                              '"Paper White"? ')
elif BASE == 'Manatee':
    ACCENT = raw_input('Which accent color, "Platinum Mist" or '
                       '"Spartan Mist"? ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight color, "Bone White" or '
                              '"Just White"? ')
    if ACCENT == 'Spartan Mist':
        HIGHLIGHT = raw_input('Which highlight color, "Fractal White" or '
                              '"Not White"? ')

COLORS = 'Your selected colors are: {}, {}, {}.'.format(BASE, ACCENT,
                                                        HIGHLIGHT)
print COLORS
