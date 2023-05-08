import numpy as np

from trast import Rasterizer


def main():
    # t = [[10.3234234, 1.2324],
    #      [3.323432, 1.2324],
    #      [5.5324, 3.1324234]]

    # t = [[1.23423, 6.2325],
    #      [7.32445, 6.2325],
    #      [3.324, 3.345345]]

    t = [[3.123124, 3.4656],
         [9.2353, 1.325534],
         [4.436, 7.24324]]

    t = (np.array(t) * 100).tolist()

    r = Rasterizer(screen=(1600, 900), pixel=255)
    r.rasterize_triangle(face=t)
    r.quick_plot()


if __name__ == '__main__':
    main()
