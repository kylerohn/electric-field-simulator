import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# X Limits on graph
NEGXLIM = -10
POSXLIM = 10

# Y Limits on graph
NEGYLIM = -10
POSYLIM = 10

# Positive Charge Position
POSQX = -4
POSQY = 2

# Negative Charge position
NEGQX = 4
NEGQY = -2

# Distance between points
PD = 0.5

# Charge values
POSQ = 1.602*(10**-19)
NEGQ = 1.602*(10**-19)

# K
k = 8.99 ** 9

# Initialize all x and y values
np_grid = np.mgrid[NEGXLIM:POSXLIM + PD:PD,
                   NEGYLIM:POSYLIM + PD:PD]

# Unpack all x and y values
x_grid, y_grid = np_grid[0], np_grid[1]

# Unpack Coordinates, additional values for vector
coordinate_list = []
for idx1, row_x in enumerate(x_grid):
    for idx2, x_val in enumerate(row_x):
        coordinate_list.append([x_val, y_grid[idx1][idx2], 1, 1])

for idx, coordinate in enumerate(coordinate_list):
    # Unpack x and y values
    x = coordinate[0]
    y = coordinate[1]

    if x == POSQX or y == POSQY:
        u = 0
        v = 0
        coordinate_list[idx][2] = u
        coordinate_list[idx][3] = v
        continue
    elif x == NEGQX or y == NEGQY:
        u = 0
        v = 0
        coordinate_list[idx][2] = u
        coordinate_list[idx][3] = v
        continue

    # Distances from positive charge
    x_d1 = x-POSQX
    y_d1 = y-POSQY
    xy_d1 = sqrt((x_d1 ** 2) + (y_d1 ** 2))

    # Distance from negative charges
    x_d2 = x-NEGQX
    y_d2 = y-NEGQY
    xy_d2 = sqrt((x_d2 ** 2) + (y_d2 ** 2))

    if xy_d1 == 0:
        xy_d1 = 0.001

    if xy_d2 == 0:
        xy_d2 = 0.001

    # Create coefficients of vectors
    c1 = (k * POSQ) / (xy_d1 ** 3)
    c2 = (k * NEGQ) / (xy_d2 ** 3)

    u = (c1 * x_d1) + (c2 * x_d2)
    v = (c1 * y_d1) + (c2 * y_d2)

    coordinate_list[idx][2] = u
    coordinate_list[idx][3] = v


for field_element in coordinate_list:
    plt.quiver(field_element[0], field_element[1],
               field_element[2], field_element[3], width=0.001, pivot="middle")


plt.scatter(POSQX, POSQY, s=30, c='red')
plt.scatter(NEGQX, NEGQY, s=30, c='red')
# plt.scatter(x, y, s=0.1, c='black')
plt.show()
