import numpy as np
from matplotlib import pyplot as plt

def fill_bottom_flat_triangle(face=None, screen=None, res=None, boundary=None):

    if type(face) == type(np.array([])):
        face = face.tolist()

    # sort by y and then by x
    face.sort(key=lambda i: (i[1], -i[0]), reverse=True)
    resX, resY = res[0], res[1]
    minX, maxX, minY, maxY = boundary

    dx, dy = (maxX - minX) / resX, (maxY - minY) / resY

    invslope1 = (face[1][0] - face[0][0]) / (face[1][1] - face[0][1])
    invslope2 = (face[2][0] - face[0][0]) / (face[2][1] - face[0][1])

    curx1, curx2 = face[0][0], face[0][0]

    # prepocet realnej suradnice na diskretnu suradnicu
    dy1, dy2 = int((maxY - face[0][1]) // dy), int((maxY - face[1][1]) // dy)

    curdx1, curdx2 = int((curx1 - minX) // dx), int((curx2 - minX) // dx)

    for y in range(dy1, dy2 + 1, 1):
        for x in range(curdx1, curdx2 + 1, 1):
            screen[y][x] = 1

        curx1 -= invslope1
        curx2 -= invslope2
        curdx1, curdx2 = int((curx1 - minX) // dx), int((curx2 - minX) // dx)

def fill_top_flat_triangle(face=None, screen=None, res=None, boundary=None):
    if type(face) == type(np.array([])):
        face = face.tolist()

    # sort by y and then by x
    face.sort(key=lambda i: (i[1], -i[0]), reverse=True)

    resX, resY = res[0], res[1]
    minX, maxX, minY, maxY = boundary

    dx, dy = (maxX - minX) / resX, (maxY - minY) / resY

    invslope1 = (face[2][0] - face[0][0]) / (face[2][1] - face[0][1])
    invslope2 = (face[2][0] - face[1][0]) / (face[2][1] - face[1][1])

    curx1, curx2 = face[2][0], face[2][0]

    # prepocet realnej suradnice na diskretnu suradnicu
    dy1, dy2 = int((maxY - face[2][1]) // dy), int((maxY - face[0][1]) // dy)

    curdx1, curdx2 = int((curx1 - minX) // dx), int((curx2 - minX) // dx)

    for y in range(dy1, dy2 - 1, -1):
        for x in range(curdx1, curdx2 + 1, 1):
            screen[y][x] = 1

        curx1 += invslope1
        curx2 += invslope2
        curdx1, curdx2 = int((curx1 - minX) // dx), int((curx2 - minX) // dx)


def fill_triangle(face=None, screen=None, res=None, boundary=None):
    if type(face) == type(np.array([])):
        face = face.tolist()
    # sort by y and then by x
    face.sort(key=lambda i: i[1], reverse=True)

    if face[0][1] == face[1][1]:
        fill_top_flat_triangle(face=face, screen=screen, res=res, boundary=boundary)
    elif face[1][1] == face[2][1]:
        fill_bottom_flat_triangle(face=face, screen=screen, res=res, boundary=boundary)
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

        fill_bottom_flat_triangle(face=face_bottom_flat, screen=screen, res=res, boundary=boundary)
        fill_top_flat_triangle(face=face_top_flat, screen=screen, res=res, boundary=boundary)


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

# fill_bottom_flat_triangle(face=t, screen=screen, res=(resx, resy), boundary=(minx, maxx, miny, maxy))
# fill_top_flat_triangle(face=t, screen=screen, res=(resx, resy), boundary=(minx, maxx, miny, maxy))
fill_triangle(face=t, screen=screen, res=(resx, resy), boundary=(minx, maxx, miny, maxy))


# plt.scatter(list(zip(*t))[0], list(zip(*t))[1])
# xs = list(zip(*t))[0]
# ys = np.array(list(zip(*t))[1])
#
# plt.plot(xs, ys, c="k")
# plt.axis((0, 16, 0, 9))
plt.imshow(screen, cmap=plt.cm.gray_r, origin='upper', interpolation="nearest")
plt.show()
