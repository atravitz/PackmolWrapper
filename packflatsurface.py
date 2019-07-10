from PackmolWrapper import PackmolInput

#Specify dimensions
packmol_tol    = 1.1
box_buffer     = 0.

num_polymers = 100
num_kuhn = 10
num_lloops = 90
num_bridges = 10
num_rloops = 100

box_length = 44.2
box_width = 5
box_height = box_length

x_min = -box_width/2
x_max = box_width/2
y_min = -box_length/2+0.1
y_max = box_length/2-0.1
z_min = -box_height/2+0.1
z_max = box_height/2-0.1


packmol = PackmolInput(packmol_tol, 'xyz', "{}loop_{}kuhn_{}lx.xyz".format(num_polymers, num_kuhn, box_length), 2*box_buffer)

#Left Loops
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

#Bridges
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

#Right Loops
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