"""This module contains variables for pentaminoes puzzles.
Attributes:
    Variables listed in the SHAPES section are numpy arrays representing the different pentaminoes.
    The letter code scheme is documented here:
    https://en.wikipedia.org/wiki/Pentomino

    Variables listed in the GRIDS section are numpy arrays representing different puzzles.
 """
############################IMPORT#############################
import numpy as np

##############SHAPES###########################################
SHAPE_I = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((3, 0, 0)),
           np.array((4, 0, 0))]

SHAPE_T = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((2, 1, 0)),
           np.array((2, -1, 0))]

SHAPE_L = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((3, 0, 0)),
           np.array((3, 1, 0))]

SHAPE_V = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((2, 1, 0)),
           np.array((2, 2, 0))]

SHAPE_Y = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((1, 1, 0)),
           np.array((2, 0, 0)),
           np.array((3, 0, 0))]

SHAPE_P = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((0, 1, 0)),
           np.array((1, 1, 0))]

SHAPE_N = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((2, 1, 0)),
           np.array((3, 1, 0))]

SHAPE_U = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((2, 0, 0)),
           np.array((0, 1, 0)),
           np.array((2, 1, 0))]

SHAPE_X = [np.array((0, 0, 0)),
           np.array((0, 1, 0)),
           np.array((0, 2, 0)),
           np.array((-1, 1, 0)),
           np.array((1, 1, 0))]

SHAPE_W = [np.array((0, 0, 0)),
           np.array((1, 0, 0)),
           np.array((1, 1, 0)),
           np.array((2, 1, 0)),
           np.array((2, 2, 0))]

SHAPE_F = [np.array((0, 0, 0)),
           np.array((0, 1, 0)),
           np.array((1, 1, 0)),
           np.array((2, 1, 0)),
           np.array((1, 2, 0))]

SHAPE_Z = [np.array((0, 0, 0)),
           np.array((0, 1, 0)),
           np.array((1, 1, 0)),
           np.array((1, 2, 0)),
           np.array((2, 2, 0))]

############SHAPE SETS#########################################
#problems 61-63
SET_1 = [SHAPE_T, SHAPE_Y, SHAPE_L,
         SHAPE_P, SHAPE_N, SHAPE_V, SHAPE_U]

SET_1 = [SHAPE_L, SHAPE_N, SHAPE_T, SHAPE_Y,
         SHAPE_P,  SHAPE_V, SHAPE_U]

#problems 64-67
SET_2 = [SHAPE_I, SHAPE_X, SHAPE_T, SHAPE_Z,
         SHAPE_W, SHAPE_L, SHAPE_F, SHAPE_Y,
         SHAPE_V, SHAPE_N, SHAPE_P, SHAPE_U]


############GRIDS##############################################

#grid size must be odd and at least 5
#at least the way I am thinking about doing poses
#For some reason coords are z, x, y w/r/t pictures in the game manual

#PYRAMID problem # 60
PYRAMID = np.zeros(3*5*5).reshape(3, 5, 5)
PYRAMID[0, :] = 1
PYRAMID[1, 1:4, 1:4] = 1
PYRAMID[2, 2, 2] = 1

#box with a hole in the top problem # 61
HOLE_CUBE = np.zeros(5**3).reshape(5, 5, 5)
HOLE_CUBE[0:4, 0:3, 0:3] = 1   #the cube
HOLE_CUBE[3, 1, 1] = 0   #the hole

#THRONE prob # 62
THRONE = np.zeros(9*3*2).reshape(9, 3, 2)
THRONE[0:7, 0, 0] = 1
THRONE[0:9, 1, 0] = 1
THRONE[0:7, 2, 0] = 1
THRONE[0:4, 0:3, 1] = 1

#prob 64:
ARMCHAIR = np.zeros(6*4*4).reshape(6, 4, 4)
ARMCHAIR[:, :, 0] = 1
ARMCHAIR[0:4, 0, :] = 1
ARMCHAIR[0:4, 3, :] = 1
ARMCHAIR[0:2, 1:3, 0:4] = 1
