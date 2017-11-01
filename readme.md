## Pentaminator
Pentaminator is a script to solve pentomino puzzles, because I can't figure out how to solve them by hand.  A description of the puzzle can be found at:
https://en.wikipedia.org/wiki/Pentomino

### Usage:

### Terminology:
- PIECE:  A representation of a pantomino composed of 5 contiguous cubes.
- SHAPE:  The target shape.  One must make the shape by stacking PIECES together.
- GRID:  The SHAPE is encoded as 1s within a box-shaped numpy array referred to as the GRID.
- POSE:  An orientation of a PIECE within the GRID.  If the pose extends outside the boundaries of the SHAPE, it cannot be part of a workable solution.

### Notes:
This particular pentomino puzzle solver is probably not super-efficient, but it works reasonably fast on smaller (7-block) puzzles.  It relies heavily on numpy.  The basic process involves the generation of all possible orientations of each piece within the shape, followed by the recursive placement of pieces until the puzzle is solved.  

GENERATION OF ALL POSSIBLE POSES
1.  For every available piece, test all possible orientations at each point of the shape.  If a given orientation falls within the bounds of the shape, store it as a pose that could comprise part of a solution.
2.  Remove redundant poses.
3.  Remove poses that "pinch off" part of the shape into a volume not divisible by 5.  These poses cannot possibly be solutions.

PLACEMENT OF PIECES:
1.  Consider a list of pieces yet to be used, a target shape, and a list of poses already used.
2.  For all possible poses of the first piece in the list...
    superimpose the pose on the target shape.
    If the pose doesn't overlap with any previously placed poses....
    And the resulting superimposition doesn't pinch off any unusable volumes...
    Add the pose to the list of poses already used.
    Take the list of remaining pieces, the superimposition, and the list of poses already used and go back to 1.
3.  When you have successfully used all the pieces, print the solution.



### To-do:

As mentioned, the solver is probably not super-efficient. Possible improvements:

- Right now all possible solutions are printed.  I only really care about finding one solution, because I just want to know how to make the puzzle.  I should set things up to halt recursion once a solution is found.
- Alternately, it would be possible to eliminate trivial solutions that are just rotations of other solutions.  This could be accomplished by checking all the POSES for one and only one given PIECE to eliminate POSES of that PIECE that can be made equivalent through 90 degree or 180-degree rotations, assuming the SHAPE is symmetrical with respect to those rotations as well.
- I assume the order in which pieces are placed will influence the time to find the first solution.  Potentially placing pieces with fewer possible poses first will result in quicker convergence.
- The functions to generate all possible poses are quite inefficient, but they also don't have to deal with the combinatorial explosion that results from combining different poses, so this doesn't seem like a huge problem.
- Time-consuming functions could be implemented in Cython.
