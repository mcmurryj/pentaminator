import pentaminoes_functions as pen
import shapes_and_grids as stuff

pieces = [shape_4, shape_5, shape_6, shape_7, shape_8, shape_2, shape_3]

pose_list     = []

#For every piece in the list of pieces to be used....
for p in pieces:
    #get all possible orientations of the piece within the grid
    all_poses = pen.get_ok_poses(p, grid)
    #Filter these to get rid of redundant orientations
    n_poses   = pen.get_nonredundant_poses(all_poses)
    #Check poses for ones that cannot possibly be correct.
    #Store the poses that are not doomed to failure.
    c_poses   = []
    for z in n_poses:
        #Chunk incompatible takes the first enclosed space in the grid and counts the number of blocks in it.
        #If number_blocks %% 5 is not zero, this configuration cannot possibly work.
        if not pen.chunk_incompatible(z + grid) :
            c_poses.append(z)
    pose_list.append(c_poses)

#Recursively place pieces from the list of possible orientations
#Print the solutions.
pen.place_next(pose_list, grid)
