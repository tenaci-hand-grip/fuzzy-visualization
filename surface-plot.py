#!/usr/bin/python3

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from scipy.interpolate import griddata
from scipy import interpolate
import scipy
import scipy.ndimage


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z_label = 'Thumb Grip'

ax.set_xlabel('Force (g)')
ax.set_ylabel('Flex (degrees)')
ax.set_zlabel(z_label)


X = np.array([0, 350, 700, 1050, 1400, 1750, 2100]) # force
Y = np.array([0, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100]) # flex
X, Y = np.meshgrid(X, Y)

# top-left is (0,0)
# bottom-right is (1,1)
Z = np.array([
    [0,      0,      0.3,    0.4,    0.4,    0.5,    0.5],
    [0,      np.nan, np.nan, np.nan, 0.5,    np.nan, 0.7],
    [0,      np.nan, np.nan, np.nan, 0.8,    np.nan, 0.7],
    [0.1,      np.nan, np.nan, np.nan, 0.9,    np.nan, 0.8],     # ---
    [0.2,    np.nan, np.nan, np.nan, 1.0,    np.nan, 1],    # flex
    [0.2,    np.nan, np.nan, np.nan, np.nan, np.nan, 1],       # +++
    [0.2,    np.nan, np.nan, np.nan, np.nan, np.nan, 0.8],
    [0,      np.nan, np.nan, np.nan, np.nan, np.nan, 0.7],
    [0,      0.3,    0.5,    0.6,    0.8,    0.8,    0.7]])

                     # --- force +++ #

array = np.ma.masked_invalid(Z)
x1 = X[~array.mask]
y1 = Y[~array.mask]
newarr = array[~array.mask]

Z = griddata((x1, y1), newarr.ravel(), (X, Y), method='cubic')

sigma = [1.0, 1.0]

Z = scipy.ndimage.filters.gaussian_filter(Z, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_zlim(0, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

# top view
ax.set_proj_type('ortho')
ax.set_zlabel('')
ax.view_init(89.9,269.9)
plt.savefig('output/surface-top.png', dpi=300)
plt.savefig('output/surface-top.pdf')
ax.set_zlabel(z_label)
ax.set_proj_type('persp')

# right-diagonal view
ax.view_init(30,315)
plt.savefig('output/surface-right.png', dpi=300)
plt.savefig('output/surface-right.pdf')

# left-diagonal view
ax.view_init(30,135)
plt.savefig('output/surface-left.png', dpi=300)
plt.savefig('output/surface-left.pdf')

# rear view
ax.view_init(30,45)
plt.savefig('output/surface-back.png', dpi=300)
plt.savefig('output/surface-back.pdf')

# front view
ax.view_init(30,225)
plt.savefig('output/surface-front.png', dpi=300)
plt.savefig('output/surface-front.pdf')

plt.show()