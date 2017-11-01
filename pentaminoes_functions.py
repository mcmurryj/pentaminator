import numpy as np
from itertools import product

def rotate(phi, psi, ome) :
    """For a given set of angles, return a matrix to accomplish the specified rotation. """
    mat_x = np.matrix([[1,            0,            0],
                       [0,  np.cos(phi), -np.sin(phi)],
                       [0,  np.sin(phi),  np.cos(phi)]])

    mat_y = np.matrix([[np.cos(psi),  0,  np.sin(psi)],
                       [0,            1,            0],
                       [-np.sin(psi), 0,  np.cos(psi)]])

    mat_z = np.matrix([[np.cos(ome), -np.sin(ome),  0],
                       [np.sin(ome),  np.cos(ome),  0],
                       [          0,            0,  1]])
    #Convert to int as values from np.sin/np.cos are float and we don't want that.
    # Ninety degree rotations only.
    return((mat_x * mat_y * mat_z).astype(int))

def get_ok_poses(shape, grid):
    """for a given shape and a given grid,  get an
    exhaustive list of all the possible orientations of
    the shape in the grid.
    The shape input is a list of xyz coordinate arrays.
    The grid input is a numpy array, 0s are not allowed and 1s are allowed.
    Returns a list of numpy arrays with 1s corresponding to locations occupied by shape.
    Currently the poses are non-redundant and are pruned separately."""
    ok_poses = []
    #only works for a cubic grid, maybe?
    gridshape   = grid.shape
    squares     = product(range(gridshape[0]), range(gridshape[1]), range(gridshape[2]))
    # For every spot in the grid...
    for s in squares :
        # If the spot is supposed to have stuff in it...
        if grid[s] == 1 :
            print("s is")
            print(s)
            # For every angle....
            angles      = (np.arange(4))*np.pi/2
            angles      = product(angles, angles, angles)
            for a in angles:
                #try to place the shape in the grid
                try:
                    #Use matrix multiplication w/rotation matrix to rotate the shape.
                    rotoshape = shape * rotate(a[0], a[1], a[2])
                    #Add the displacement associated with each square of the shape to the starting position on the grid.
                    x    = np.array(rotoshape) + np.array([s,s,s,s,s])
                    #For each square the shape occupies...
                    for el in x :
                        # If it is not within the desired form...
                        if grid[tuple(el)] != 1 :
                            #Give up on the pose
                            break
                        # If the shape sticks out of the confines of the grid
                        if el.min() < 0 :
                            #Give up on the pose...Is this also covered by the IndexError exception below?
                            break
                    else :
                        ok_pose = np.copy(grid)
                        ok_pose.fill(0)
                        for el in x :
                            ok_pose[tuple(el)] = 1
                        ok_poses.append(ok_pose)
                #If you try and place a piece outside the boundary of the grid
                except IndexError:
                    #Just don't do anything, that wasn't going to work
                    pass
    return(ok_poses)

def get_nonredundant_poses(shape_list):
    """Convert a list of poses (arrays) into hashable form.
       Remove redundant elements.
       Return list of non-redundant poses in array form."""
    arraydict = {}
    for s in shape_list :
        k            = s.tostring()
        arraydict[k] = s
    nonredundant = []
    for x in set(arraydict.keys()) :
        nonredundant.append(arraydict[x])
    return(nonredundant)

def get_neighbors(s, superimposition) :
    """Take the coordinates of a square,
    and the superimposition of the grid and shapes placed upon it.
    Return a list of the coordinates of unnocupied neighboring squares."""
    neighbors = []
    gridshape = superimposition.shape
    #this caused problems
    if superimposition[s] != 1 :
        return (neighbors)
    #Should probably implement the following with a FOR loop for style, but this does the job.
    else:
        #If the next square to the right is within bounds...
        if   s[0] + 1 < gridshape[0] :
            #If the next square to the left is part of the target shape...
            if superimposition[s[0] + 1, s[1], s[2]] == 1 :
                #Add the square to the list of neighbors
                neighbors.append((s[0] + 1, s[1], s[2]))
        if s[0] - 1 >= 0 :
            if superimposition[s[0] - 1, s[1], s[2]] == 1 :
                neighbors.append((s[0] - 1, s[1], s[2]))
        if s[1] + 1 < gridshape[1] :
            if superimposition[s[0], s[1] + 1, s[2]] == 1 :
                neighbors.append((s[0], s[1] + 1, s[2]))
        if s[1] - 1 >= 0 :
            if superimposition[s[0], s[1] - 1, s[2]] == 1 :
                neighbors.append((s[0], s[1] - 1, s[2]))
        if s[2] + 1 < gridshape[2] :
            if superimposition[s[0], s[1], s[2] + 1] == 1 :
               neighbors.append((s[0], s[1], s[2] + 1))
        if s[2] - 1 >= 0 :
            if superimposition[s[0], s[1], s[2] - 1] == 1 :
                neighbors.append((s[0], s[1], s[2] - 1))
        return(neighbors)

def get_chunk(chunk, superimposition) :
    """Take a point on a grid.  Return a list of contiguous, unocupied neighbors.
    Relies on modification of a list being iterated over...
    So maybe not super-robust, but it seems to work.
    Also, will return a length-1 list if fed an empty coord."""
    #For every square in the chunk
    for c in chunk :
        #Get neighbors of the square.
        cand = get_neighbors(c, superimposition)
        for ca in cand :
            #Check to see if we already know about this square
            if ca not in chunk:
                #If it is new, put it at the end of the chunk-list.
                chunk.append(ca)
    #return the list of contiguous squares
    return(chunk)

def chunk_incompatible(superimposition) :
    """returns TRUE if the nascent grid cannot possibly work.
    FALSE means it maybe can work.
    Basis is the volume of contiguous chunks."""
    gridshape   = superimposition.shape
    squares     = product(range(gridshape[0]), range(gridshape[1]), range(gridshape[2]))
    for s in squares :
        if superimposition[s] == 1 :
            chunk_len = len(get_chunk([s], superimposition))
            return(chunk_len % 5 != 0)

def place_next(pieces,
               grid,
               index_list = [] ) :
    """Recursively try to place pieces.
    If there is overlap or if you trap a space with volume not divisible by 5, give up.
    When you have filled the grid, print the solution. """
    limit      = int(np.sum(grid) + len(pieces)*5 -1)
    poses = pieces[0]
    for p in poses :
        superimposition = grid + p
        new_list        = index_list + [p]
        if np.max(superimposition) > 2 :
            continue
        if chunk_incompatible(superimposition) :
            continue
        if np.sum(superimposition) > limit :
            print("victory\n")
            for i in new_list:
                print(i)
                print('\n\n')
            print("\n\n\n\n\n\n")
        else:
            #If you still have pieces left to try...""
            if len(pieces) > 1:
                #try to place the remaining pieces that you haven't placed yet.
                #The grid is the grid you started with, plus whichever piece you just added.
                #The list contains the positions of pieces that have been placed thus far.
                place_next(pieces[1:], superimposition, new_list)
