#!/bin/sh
"""
    Slab squeezing:
        There are at least two useful pieces of information for judging
        the progress of a slab squeezing. One is the density profile and
        another is the Lz of the box. The simplest scheme for controlling
        slab squeezing would be to only heed Lz and use no other information.
        Unfortunately, this is not sufficient, because non-uniform density
        profiles can develop which show relatively little change in Lz.

        Look for correlated density fluctuations, with bin size so that at least
        60 atoms are in each bin (on average). Checks for correlation just by
        looking at adjacent bin and seeing if correlation > 0.3.

        If not correlated, and if Lz is not changing by much, then we can
        stop squeezing.

        TODO
        Also look at xyz bins. If any cubic bin sized such that on average
        there should be 6 molecules inside happens to have zero molecules inside,
        that's a problem.

        TODO
        If there is a z slice without any atoms, cut it out, minus a tol sliver
"""
from packmol_wrapper import PackmolInput
from packmol_wrapper import PackmolStructure


"""
    This sets up a slab if dependencies are available.
    This function should be called /after/ verifying that the job is actually requested.
    Full squeezing trajectory is saved to full_squeeze.xtc
    TODO add/remove molecules to get Lz precisely right
"""

xy_len         = 30
packmol_tol    = 1.0
box_buffer     = packmol_tol/2.
# molecule_path  = project.root_directory()+'/resources/' + res.ff_molecule_pdb[ff][molecule]
number = 100

# molecule_pdb = molecule_path.strip('/').split('/')[-1]
box_size = [xy_len,xy_len,10]



# pack a box with molecules sparsely, using half the estimated
# number density (estimate comes from resources file)
input = PackmolInput(packmol_tol, 'xyz', 'test.xyz', 2*box_buffer)
structure1 = input.addStructure('molecules/10kuhn.xyz', number)
input.addStructureConstraintInsideBox(box_buffer, box_buffer, box_buffer,
                               10.*box_size[0]-box_buffer,
                               10.*box_size[1]-box_buffer,
                               10.*box_size[2]-box_buffer)
structure1.pickAtoms([3,4,5])
structure1.addAtomConstraintInsideBox(box_buffer, box_buffer, box_buffer,
                               10.*box_size[0]-box_buffer,
                               10.*box_size[1]-box_buffer,
                               10.*box_size[2]-box_buffer)


# structure2 = packmol.addStructure('molecules/10kuhn.xyz', number)
# packmol.addStructureConstraintInsideBox(box_buffer, box_buffer, box_buffer,
#                                10.*box_size[0]-box_buffer,
#                                10.*box_size[1]-box_buffer,
#                                10.*box_size[2]-box_buffer)

input.run()
