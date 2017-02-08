import numpy as np
from matplotlib import pyplot as plt

def fill_bottom_flat_triangle(face=None, screen=None, boundary=None, d=None):
    if type(face) == type(np.array([])):
        face = face.tolist()

    v = [None, None, None]
    # sort by y
    face = sorted(face, key=lambda i: i[1], reverse=True)
    v[0] = face[0]
    v[1], v[2] = tuple(sorted(face[1:], key=lambda i: i[0], reverse=False))

    dx, dy = d
     # prepocet realnej suradnice na diskretnu suradnicu
    dy1, dy2 = int((boundary[3] - v[0][1]) // dy), int((boundary[3] - v[1][1]) // dy)
    # maximalny rozsah pre riadkove naplnanie
    max_x, min_x = int((v[2][0] - boundary[0]) // dx) + 1, int((v[1][0] - boundary[0]) // dx) - 1

    if abs(dy2 - dy1) <= 1 and dy / 2.0 > v[0][1] - v[1][1]:
        return []

    invslope1 = ((v[1][0] - v[0][0]) / (v[1][1] - v[0][1])) * dy
    invslope2 = ((v[2][0] - v[0][0]) / (v[2][1] - v[0][1])) * dy

    curx1, curx2 = v[0][0], v[0][0]
    curdx1, curdx2 = int((curx1 - boundary[0]) // dx), int((curx2 - boundary[0]) // dx)

    # except of last line
    for y in range(dy1, dy2, 1):
        for x in range(curdx1, curdx2 + 1, 1):
            screen[y][x] = 1

        curx1 -= invslope1
        curx2 -= invslope2
        curdx1, curdx2 = int((curx1 - boundary[0]) // dx), int((curx2 - boundary[0]) // dx)
    # last line
    for x in range(curdx1, curdx2 + 1, 1):
        if x < min_x:
            continue
        elif x > max_x:
            break
        screen[dy2][x] = 1

def fill_top_flat_triangle(face=None, screen=None, boundary=None, d=None):
    if type(face) == type(np.array([])):
        face = face.tolist()

    v = [None, None, None]
    # sort by y
    face = sorted(face, key=lambda i: i[1], reverse=True)
    v[2] = face[2]
    v[0], v[1] = tuple(sorted(face[:-1], key=lambda i: i[0], reverse=False))
    dx, dy = d
    # prepocet realnej suradnice na diskretnu suradnicu
    dy1, dy2 = int((boundary[3] - v[2][1]) // dy), int((boundary[3] - v[0][1]) // dy)
    # maximalny rozsah pre riadkove naplnanie
    max_x, min_x = int((v[1][0] - boundary[0]) // dx) + 1, int((v[0][0] - boundary[0]) // dx) - 1

    # otestovanie, ci sa nema vykonat krko v "y" smere, napriek tomu, ze velkost pixela je daleko vacsia
    # ako vzdialenost dvoch bodov v "y" smere
    if abs(dy2 - dy1) <= 1 and dy / 2.0 > v[2][1] - v[0][1]:
        return []

    invslope1 = ((v[2][0] - v[0][0]) / (v[2][1] - v[0][1])) * dy
    invslope2 = ((v[2][0] - v[1][0]) / (v[2][1] - v[1][1])) * dy

    curx1, curx2 = v[2][0], v[2][0]
    curdx1, curdx2 = int((curx1 - boundary[0]) // dx), int((curx2 - boundary[0]) // dx)

    # tu sa vykonaju setky riadky okrem posledneho (teda toho flat)
    # all lines except of last one
    for y in range(dy1, dy2, -1):
        for x in range(curdx1, curdx2 + 1, 1):
            screen[y][x] = 1

        curx1 += invslope1
        curx2 += invslope2
        curdx1, curdx2 = int((curx1 - boundary[0]) // dx), int((curx2 - boundary[0]) // dx)
    # tu sa vykona ten flat riadok (mam to rozbite z dovodu vykonu, aby sa v kazdom loope nemuselo robit if)
    # last one
    for x in range(curdx1, curdx2 + 1, 1):
        if x < min_x:
            continue
        elif x > max_x:
            break
        screen[dy2][x] = 1


def fill_triangle(face=None, screen=None, boundary=None, d=None):
    if type(face) == type(np.array([])):
        face = face.tolist()
    # sort by y and then by x
    face.sort(key=lambda i: i[1], reverse=True)

    if face[0][1] == face[1][1]:
        fill_top_flat_triangle(face=face, screen=screen, boundary=boundary, d=d)
    elif face[1][1] == face[2][1]:
        fill_bottom_flat_triangle(face=face, screen=screen, boundary=boundary, d=d)
    else:
        # vertex 4 (has to be esetimated)
        #
        #           o v1
        #
        #
        #    v2 o       o v4
        #
        #
        #
        #                     o v3

        x = face[0][0] + ((face[1][1] - face[0][1]) / (face[2][1] - face[0][1])) * (face[2][0] - face[0][0])
        face_top_flat, face_bottom_flat = [face[1], face[2], [x, face[1][1]]], [face[0], face[1], [x, face[1][1]]]

        fill_bottom_flat_triangle(face=face_bottom_flat, screen=screen, boundary=boundary, d=d)
        fill_top_flat_triangle(face=face_top_flat, screen=screen, boundary=boundary, d=d)


t = [[10.3234234, 1.2324],
     [3.323432, 1.2324],
     [5.5324, 3.1324234]]

t = [[1.23423, 6.2325],
     [7.32445, 6.2325],
     [3.324, 3.345345]]

t = [[3.123124, 3.4656],
     [9.2353, 1.325534],
     [4.436, 7.24324]]

t = (np.array(t) * 100).tolist()

resx, resy = 1600, 900
minx, maxx = 0, 1600
miny, maxy = 0, 900

screen = np.zeros(shape=(resy, resx))
dev = (maxx - minx) / resx, (maxy - miny) / resy

fill_triangle(face=t, screen=screen, boundary=(minx, maxx, miny, maxy), d=dev)


# plt.scatter(list(zip(*t))[0], list(zip(*t))[1])
# xs = list(zip(*t))[0]
# ys = np.array(list(zip(*t))[1])
#
# plt.plot(xs, ys, c="k")
# plt.axis((0, 16, 0, 9))
plt.imshow(screen, cmap=plt.cm.gray_r, origin='upper', interpolation="nearest")
plt.show()

