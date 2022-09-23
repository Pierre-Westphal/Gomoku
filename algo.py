#!/usr/bin/env python3

import random

class algo:
    attack = [ "11110", "11101", "11011", "22220", "22202", "22022", "1110", "1101", "2220", "2202", "110", "101", "10" ]
    defenc = [ "11110", "11101", "11011", "22220", "22202", "22022", "2220", "2202", "1110", "1101", "220", "202", "110", "101", "10", "20" ]

    def __init__(self, first, size, matrice, x, y, info_dict):
        self.size = size
        self.matrice = matrice
        self.patterns = algo.attack if first else algo.defenc
        self.x = x
        self.y = y
        self.info_dict = info_dict
        self.res_x = 0
        self.res_y = 0

    def rndm(self):
        self.res_x = random.randint(4, self.size - 5)
        self.res_y = random.randint(4, self.size - 5)
        while self.matrice[self.res_y][self.res_x] > 0:
            self.res_x = random.randint(4, self.size - 5)
            self.res_y = random.randint(4, self.size - 5)

    def checkPattern(self, pattern, x, y):
        self.res_x, self.res_y = x_axis(self.matrice, pattern, x, y)
        if self.res_x and self.res_y: return
        self.res_x, self.res_y = y_axis(self.matrice, pattern, x, y)
        if self.res_x and self.res_y: return
        self.res_x, self.res_y = xy_axis(self.matrice, pattern, x, y)
        if self.res_x and self.res_y: return
        self.res_x, self.res_y = -1, -1
        return

    def calc(self):
        for pattern in self.patterns:
            for y in range(self.size):
                for x in range(self.size):
                    if self.matrice[y][x] > 0:
                        self.checkPattern(pattern, x, y)
                        if self.matrice[self.res_y][self.res_x] == 0 and self.res_x != -1 and self.res_y != -1:
                            return
        if self.res_x == -1 or self.res_y == -1 :
            self.rndm()
            return

    def get_result(self):
        return self.res_x, self.res_y

def x_axis(matrice, pattern, x, y):
    try:
        if ''.join(str(v) for v in matrice[y][x:x + len(pattern)]) == pattern:
            return [int(x + pattern.index("0")), y]
    except: return [None, None]
    try:
        if ''.join(str(v) for v in matrice[y][x - (len(pattern) - 1):x + 1]) == pattern[::-1]:
            return [int(x - pattern.index("0")), y]
    except: return [None, None]
    return [None, None]

def y_axis(matrice, pattern, x, y):
    a, b = '', ''
    try:
        for i in range(len(pattern)): a += str(matrice[y + i][x])
        if a == pattern: return [x, int(y + pattern.index("0"))]
    except: return [None, None]
    try:
        for i in range(len(pattern)): b += str(matrice[y - i][x])
        if b == pattern: return [x, int(y - pattern.index("0"))]
    except: return [None, None]
    return [None, None]

def xy_axis(matrice, pattern, x, y):
    a, b, c, d = '', '', '', ''
    try:
        for i in range(len(pattern)): a += str(matrice[y + i][x + i])
        if a == pattern: return [int(x + pattern.index("0")), int(y + pattern.index("0"))]
    except: return [None, None]
    try:
        for i in range(len(pattern)): b += str(matrice[y - i][x - i])
        if b == pattern: return [int(x - pattern.index("0")), int(y - pattern.index("0"))]
    except: return [None, None]
    try:
        for i in range(len(pattern)): c += str(matrice[y - i][x + i])
        if c == pattern: return [int(x + pattern.index("0")), int(y - pattern.index("0"))]
    except: return [None, None]
    try:
        for i in range(len(pattern)): d += str(matrice[y + i][x - i])
        if d == pattern: return [int(x - pattern.index("0")), int(y + pattern.index("0"))]
    except: return [None, None]
    return [None, None]

def lunch(first, size, matrice, x, y, info_dict, begin = False):
    i = algo(first, size, matrice, x, y, info_dict)
    if begin: i.rndm()
    else: i.calc()
    return i.get_result()