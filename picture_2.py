# coding: utf-8
from graph import *

def paint_background(width, height):
    """ Рисует фон - небо и землю на всю ширину и высоту листа """
    penSize(0)
    brushColor("#9eeaf5")
    rectangle(0, 0, width, height // 2)
    brushColor("#0e9325")
    rectangle(0, height // 2, width, height)

def paint_house(x, y):
    """ Рисует домик.
        x, y - координаты левой верхней стороны
    """
    pass

def paint_tree(x, y):
    """ Рисует дерево.
        x, y - координаты середины нижней части ствола.
    """
    pass

def paint_cloud(x, y):
    """ Рисует облако.
        x, y - координаты геометрической середины облака.
    """
    pass

def paint_sun(x, y):
    """ Рисует солнышко.
        x, y - координаты центра окружности солнца.
    """

    pass


def paint_all(width, height):
    """ Должна нарисовать всё. """
    paint_background(width, height)
    paint_house(68, 126)
    paint_tree(334, 188)
    paint_cloud(248, 53)
    paint_sun(396, 44)

windowSize(450, 300)
paint_all(450, 300)
run()
