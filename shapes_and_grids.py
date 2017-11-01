############################IMPORT#############################
import numpy as np

##############SHAPES###########################################
#line
shape_1 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((3,0,0)),
           np.array((4,0,0))]

#tee
shape_2 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((2,1,0)),
           np.array((2,-1,0))]

#ell
shape_3 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((3,0,0)),
           np.array((3,1,0))]

#vee
shape_4 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((2,1,0)),
           np.array((2,2,0))]

#offset tee
shape_5 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((1,1,0)),
           np.array((2,0,0)),
           np.array((3,0,0))]

#house
shape_6 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((0,1,0)),
           np.array((1,1,0))]

#squiggle
shape_7 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((2,1,0)),
           np.array((3,1,0))]

#cee
shape_8 = [np.array((0,0,0)),
           np.array((1,0,0)),
           np.array((2,0,0)),
           np.array((0,1,0)),
           np.array((2,1,0))]

#plus  THIS MAY BE A PROBLEM AS IT HAS A NEGATIVE COORD
shape_9 = [np.array((0,0,0)),
           np.array((0,1,0)),
           np.array((0,2,0)),
           np.array((-1,1,0)),
           np.array((1,1,0))]

#W
shape_10 = [np.array((0,0,0)),
            np.array((1,0,0)),
            np.array((1,1,0)),
            np.array((2,1,0)),
            np.array((2,2,0))]

#deformed L
shape_11 = [np.array((0,0,0)),
            np.array((0,1,0)),
            np.array((1,1,0)),
            np.array((2,1,0)),
            np.array((1,2,0))]

############GRIDS##############################################

#grid size must be odd and at least 5
#at least the way I am thinking about doing poses
#For some reason coords are z,x,y w/r/t pictures in the game manual

#pyramid problem # 60
pyramid            = np.zeros(5**3).reshape(5, 5, 5)
pyramid[0,:]       = 1
pyramid[1,1:4,1:4] = 1
pyramid[2,2,2]     = 1

#box with a hole in the top problem # 61
hole_cube                 = np.zeros(5**3).reshape(5, 5, 5)
hole_cube[0:4, 0:3, 0:3]  = 1   #the cube
hole_cube[3,1,1]          = 0   #the hole

#throne prob # 62
throne                    = np.zeros(9*3*2).reshape(9, 3, 2)
throne[0:7, 0, 0]         = 1
throne[0:9, 1, 0]         = 1
throne[0:7, 2, 0]         = 1
throne[0:4, 0:3, 1]       = 1
