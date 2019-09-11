# coding: utf-8
from graph import *

windowSize(450, 300)
penColor(0, 0, 0)
penSize(0)
brushColor("#9eeaf5")
rectangle(0, 0, 450, 149)
brushColor("#0e9325")
rectangle(0, 150, 450, 299)
penSize(1)
brushColor("#936b0e")
rectangle(68, 126, 184, 202)
brushColor("#eb2f44")
polygon([(68, 126), (125, 70), (184, 126), (68, 126)])
brushColor("#0e9391")
rectangle(109, 151, 145, 180)
brushColor("black")
rectangle(328, 130, 340, 188)
brushColor("green")
for x, y in [(336, 81), (314, 99), (359, 98), (335, 111),
             (317, 125), (352, 125)]:
    circle(x, y, 18)
brushColor("white")
x, y = 221, 53
for i in range(4):
    circle(x, y, 18)
    x += 20

x, y = 241, 39
for i in range(2):
    circle(x, y, 18)
    x += 25
brushColor("#f9c2c2")
circle(396, 44, 23)

run()
