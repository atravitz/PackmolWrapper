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

packmol.addStructure('10kuhn.xyz', num_lloops)
packmol.addConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
packmol.pickAtoms(1)
packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.2)
packmol.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.5)
for i in range(2,11):
	packmol.pickAtoms(i)
	packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.5)
packmol.pickAtoms(11)
packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.2)
packmol.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.5)

packmol.addStructure('10kuhn_bridge.xyz', num_bridges)
packmol.addConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
packmol.pickAtoms(1)
packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.2)
packmol.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_min+0.5)
for i in range(2,11):
	packmol.pickAtoms(i)
	packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_min+0.5)
packmol.pickAtoms(11)
packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.2)
packmol.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.5)

packmol.addStructure('10kuhn.xyz', num_rloops)
packmol.addConstraintInsideBox(x_min, y_min, z_min, x_max, y_max, z_max)
packmol.pickAtoms(1)
packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.2)
packmol.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.5)
for i in range(2,11):
	packmol.pickAtoms(i)
	packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.5)
packmol.pickAtoms(11)
packmol.addAtomConstraintOverPlane(1.0, 0.0, 0.0, x_max-0.2)
packmol.addAtomConstraintBelowPlane(1.0, 0.0, 0.0, x_max-0.5)

packmol.run()