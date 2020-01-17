# coding: utf-8
from graph import *


def main():
    windowSize(450, 300)
    paint_all(450, 300)
    run()


def paint_all(width, height):
    """ Должна нарисовать всё. """
    paint_background(width, height)
    paint_house(48, 160, 115, 78)
    paint_house(262, 157, 80, 60)
    for i in range(4, -1, -1):
        paint_house(111 + i*20, 270 - i * 10, 50, 30)
    paint_tree(334, 188)
    paint_cloud(248, 53)
    paint_sun(396, 44)


def paint_background(width, height):
    """ Рисует фон - небо и землю на всю ширину и высоту листа """
    penSize(0)
    brushColor("#9eeaf5")
    rectangle(0, 0, width, height // 2)
    brushColor("#0e9325")
    rectangle(0, height // 2, width, height)

def paint_house(x, y, width, height):
    """ Рисует домик.
        x, y - координаты левой верхней стороны
        width, height - ширина и высота стен домика
    """
    paint_walls(x, y, width, height)
    paint_roof(x, y, width, height*0.75)

    window_x, window_y = x + width // 3, y + height // 3
    window_width = width // 3
    window_height = height // 3
    paint_window(window_x, window_y, window_width, window_height)


def paint_walls(x, y, width, height):
    """ Рисует стены домика.
        x, y - координаты левой-верхней точки стены
        width, height - ширина и высота стены
    """
    penSize(1)
    brushColor("#936b0e")
    rectangle(x, y, x + width, y + height)

    
def paint_roof(x, y, width, height):
    """ Рисует крышу домика.
        x, y - координаты левой-нижней точки крыши
        width, height - ширина и высота крыши
    """
    penSize(1)
    brushColor("#eb2f44")
    polygon([(x, y), (x + width // 2, y - height),
             (x + width, y), (x, y)])


def paint_window(x, y, width, height):
    """ Рисует окно.
        x, y - координаты левой-верхней точки окна
        width, height - ширина и высота окна
    """
    penSize(1)
    brushColor("#0e9391")
    rectangle(x, y, x + width, y + height)

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


main()
