from charge import Charge
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos

# X Limits on graph
NEGXLIM = -5
POSXLIM = 5

# Y Limits on graph
NEGYLIM = -5
POSYLIM = 5

# Distance between points
PD = 0.25

# Create grid of values
np_grid = np.mgrid[NEGXLIM:POSXLIM + PD:PD,
                   NEGYLIM:POSYLIM + PD:PD]

# Unpack x, y values
x_grid, y_grid = np_grid[0], np_grid[1]


print("Option 1: Dipole")
print("Option 2: Capacitor")
print("Option 3: Ring")
user_choice = int(input("> "))

###################################################################################################################################
# Dipole
if user_choice == 1:
    positive_charge = Charge(10**-9, -3, 0)
    negative_charge = Charge(-(10**-9), 3, 0)
    positive_charge_2 = Charge((10**-9), -2, 1)
    negative_charge_2 = Charge(-(10**-9), -2, 2)

    vector_list = []

    for idx1, x_row in enumerate(x_grid):
        for idx2, x in enumerate(x_row):
            y = y_grid[idx1][idx2]

            u1, v1 = positive_charge.calc_vec(x, y)
            u2, v2 = negative_charge.calc_vec(x, y)
            u3, v3 = positive_charge_2.calc_vec(x, y)
            u4, v4 = negative_charge_2.calc_vec(x, y)
            temp_vec = (x, y, (u1 + u2 + u3 + u4), (v1 + v2 + v3 + v4))
            vector_list.append(temp_vec)

    # np_vector_list = np.array(vector_list).transpose()

    for x, y, u, v in vector_list:
        plt.quiver(x, y, u, v, pivot="middle", width=0.001)
        print(x, y, u, v)

    plt.scatter(positive_charge.x_charge,
                positive_charge.y_charge, s=40, c="red")
    plt.scatter(negative_charge.x_charge,
                negative_charge.y_charge, s=40, c="blue")
    plt.show()
###################################################################################################################################
# Capacitor
elif user_choice == 2:
    n_charges = 100
    capacitor_len = 4
    x_pos_q = -3
    x_neg_q = 3
    # Create positive charge list

    charge_distance = PD/4
    start_point = -((n_charges)/2)*charge_distance
    end_point = (((n_charges)/2)*charge_distance) + charge_distance
    y_range = np.arange(start_point, end_point, charge_distance)
    pos_q_list = []
    neg_q_list = []
    for idx, y_n in enumerate(y_range):
        pos_q_list.append(Charge(10**-9, x_pos_q, y_n))
        neg_q_list.append(Charge(-(10**-9), x_neg_q, y_n))

    vector_list = []

    for idx1, x_row in enumerate(x_grid):
        for idx2, x in enumerate(x_row):
            y = y_grid[idx1][idx2]
            u_sum = 0
            v_sum = 0
            for idxq, pos_charge in enumerate(pos_q_list):
                neg_charge = neg_q_list[idxq]
                u1, v1 = pos_charge.calc_vec(x, y)
                u2, v2 = neg_charge.calc_vec(x, y)
                u3, v3 = positive_charge_2[idxq]
                u_sum = u_sum + u1 + u2
                v_sum = v_sum + v1 + v2
            vector_list.append((x, y, u_sum, v_sum))

    for x, y, u, v in vector_list:
        plt.quiver(x, y, u, v, pivot="middle", width=0.001)
        # print(x, y)

    for idx, charge in enumerate(pos_q_list):
        plt.scatter(charge.x_charge, charge.y_charge, color="red")
        plt.scatter(neg_q_list[idx].x_charge,
                    neg_q_list[idx].y_charge, color="blue")
    plt.show()

###################################################################################################################################
# Ring
elif user_choice == 3:
    r_ring = 1
    n_charges = 100

    period = (2*pi)/n_charges

    charge_list = []
    i = 1

    angles = np.arange(0, (2*pi), period)
    for angle in angles:
        x = r_ring * cos(angle)
        y = r_ring * sin(angle)
        charge_list.append(Charge(i*(10**-9), x, y))

    vector_list = []

    for idx1, x_row in enumerate(x_grid):
        for idx2, x in enumerate(x_row):
            y = y_grid[idx1][idx2]
            u_sum = 0
            v_sum = 0
            for charge in charge_list:
                u, v = charge.calc_vec(x, y)
                u_sum += u
                v_sum += v
            vector_list.append((x, y, u_sum, v_sum))

    for x, y, u, v in vector_list:
        plt.quiver(x, y, u, v, pivot="middle", width=0.001)

    for charge in charge_list:
        if charge.Q > 0:
            color = "red"
        elif charge.Q < 0:
            color = "blue"

        plt.scatter(charge.x_charge, charge.y_charge, color=color)
    plt.show()
