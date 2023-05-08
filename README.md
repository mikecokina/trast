[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Version](https://img.shields.io/badge/version-0.6.dev0-yellow.svg)](https://github.com/mikecokina/trast)
[![Python](https://img.shields.io/badge/python-3.6|3.7|3.8|3.9-orange.svg)](https://www.python.org/)
[![Python](https://img.shields.io/badge/os-Linux|Windows|MacOS-magenta.svg)](https://en.wikipedia.org/wiki/Operating_system)

# TRAST - Triangle - RASTerization
Python implementation of triangle rasterization in computer graphic. Rasterize trinagle/s defined by in 2D plane 
via 3 simple points on supplied screen size.

Usage:

```python
from trast import Rasterizer

t = [[3.0, 3.0],
     [9.2, 1.3],
     [4.4, 7.2]]

r = Rasterizer(screen=(1600, 900), pixel=255)
r.rasterize_triangle(face=t)
r.quick_plot()
```

Rasterized screen is accessible as following:

```
screen = r.raster
```
