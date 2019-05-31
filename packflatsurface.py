from PackmolWrapper import PackmolInput

xy_len         = 30
packmol_tol    = 1.1
box_buffer     = 0.

num_lloops = 90
num_bridges = 10
num_rloops = 100

x_min = -5.5
x_max = 5.5
y_min = -14.9
y_max = 14.9
z_min = -14.9
z_max = 14.9



# pack a box with molecules sparsely, using half the estimated
# number density (estimate comes from resources file)
packmol = PackmolInput(packmol_tol, 'xyz', '100loop_10kuhn_30lx.xyz', 2*box_buffer)

left_loops = packmol.addStructure('10kuhn.xyz', num_lloops)
packmol.addStructureConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
left_loops.pickAtoms(1)
left_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.2)
left_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.5)
left_loops.pickAtoms(list(range(2,11)))
left_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.5)
left_loops.pickAtoms(11)
left_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.2)
left_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.5)

bridges = packmol.addStructure('10kuhn_bridge.xyz', num_bridges)
packmol.addStructureConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
bridges.pickAtoms(1)
bridges.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.2)
bridges.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.5)
bridges.pickAtoms(list(range(2,11)))
bridges.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.5)
bridges.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.5)
bridges.pickAtoms(11)
bridges.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.5)
bridges.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.2)

right_loops = packmol.addStructure('10kuhn.xyz', num_rloops)
packmol.addStructureConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
right_loops.pickAtoms(1)
right_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.5)
right_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.2)
right_loops.pickAtoms(list(range(2,11)))
right_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.5)
right_loops.pickAtoms(11)
right_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.5)
right_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.2)

packmol.run()