import packmol_wrapper as pmw


inp = pmw.PackmolInput(tolerance=1.0, filetype='xyz', output='output_test_main.xyz', box_buffer=1.0)

inp.addStructure('10kuhn.xyz', 1)
inp.addStructureConstraintInsideBox(-100, -100, -100, 100, 100, 100)
inp.run()
