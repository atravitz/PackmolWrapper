from packmol_wrapper import PackmolInput


# Specify dimensions
packmol_tol = 1.1
box_buffer = 0.

num_polymers = 100
num_kuhn = 10
num_lloops = 90
num_bridges = 10
num_rloops = 100

box_length = 44.281
box_width = 5
box_height = box_length

x_min = -box_width/2
x_max = box_width/2
y_min = -box_length/2+0.1
y_max = box_length/2-0.1
z_min = -box_height/2+0.1
z_max = box_height/2-0.1


inp = PackmolInput(packmol_tol, 'xyz', "{}loop_{}kuhn_{}ly_{}gap.xyz".format(num_polymers, num_kuhn, box_length, box_width), 2*box_buffer)

# Left Loops
left_loops = inp.addStructure('molecules/10kuhn.xyz', num_lloops)
inp.addStructureConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
left_loops.pickAtoms(1)
left_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.1)
left_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.4)
left_loops.pickAtoms(list(range(2, 11)))
left_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.4)
left_loops.pickAtoms(11)
left_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.1)
left_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.4)

# Bridges
bridges = inp.addStructure('molecules/10kuhn_bridge.xyz', num_bridges)
inp.addStructureConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
bridges.pickAtoms(1)
bridges.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.1)
bridges.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.4)
bridges.pickAtoms(list(range(2, 11)))
bridges.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.4)
bridges.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.4)
bridges.pickAtoms(11)
bridges.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.4)
bridges.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.1)

# Right Loops
right_loops = inp.addStructure('molecules/10kuhn.xyz', num_rloops)
inp.addStructureConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
right_loops.pickAtoms(1)
right_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.4)
right_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.1)
right_loops.pickAtoms(list(range(2, 11)))
right_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.4)
right_loops.pickAtoms(11)
right_loops.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.4)
right_loops.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.1)

inp.run()
