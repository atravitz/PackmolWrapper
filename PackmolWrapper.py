""" PackmolWrapper.py has a Python class helpful for generating Packmol input files
	Copyright (C) 2015      Kyle J. Huston

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>."""

""" Quick Guide for Packmol's Input located at
	http://www.ime.unicamp.br/~martinez/packmol/ """
from subprocess import Popen, PIPE

class PackmolError(Exception):
	pass

class PackmolInput():
	def __init__(self, tolerance, filetype, output, box_buffer):
		self.tolerance = tolerance
		self.filetype = filetype
		self.output = output
		self.box_buffer = box_buffer
		self.structures = []

	def genFileText(self):
		file_text = '# Generated by PackmolWrapper.py\n'
		file_text += 'tolerance %f\n'%(self.tolerance)
		file_text += 'filetype %s\n'%(self.filetype)
		file_text += 'output %s\n'%(self.output)
		#file_text += 'add_box_sides %f\n'%(self.box_buffer)
		file_text += '\n'
		for structure in self.structures:
			file_text += 'structure %s\n'%(structure.pdb)
			file_text += 'number %d\n  '%(structure.number)
			file_text += structure.constraint_text.replace('\n','\n  ')
			file_text = file_text[:-2]
			for atom_group in structure.atom_groups:
				file_text += '  atoms %s\n    ' %(atom_group.selected)
				file_text += atom_group.constraint_text.replace('\n','\n    ')
				file_text = file_text[:-2]			
				file_text += 'end atoms\n'
			file_text += 'end structure\n\n'
		return file_text

	def exportFile(self,path):
		with open(path,'w') as inputfile:
			inputfile.write(self.genFileText())

	def check_no_exception(self,stdout_path=None):
		"""
			Read standard error file at stdout_path to
			decide if Packmol ended in error. Raises an
			exception if Packmol ended in error.
		"""
		error_flag = False
		with open(stdout_path,'r') as stdout:
			for line in stdout.readlines():
				if not error_flag and 'ERROR:' in line:
					error_flag = True
					error_msg = '\n'
				if error_flag:
					error_msg += line
		if error_flag:
			raise PackmolError(error_msg)

	def run(self):
		self.exportFile('.packmol.inp')
		with open('.packmol.inp') as inpfile:
			with open('.packmol.stdout','w') as stdout:
				inp = inpfile.read()
				p = Popen(['packmol'], stdin=PIPE, stdout=stdout, shell=True, encoding='utf8')
				p.communicate(input=inp)

		self.check_no_exception('.packmol.stdout')

	def addStructure(self,pdb,number):
		structure_tmp = PackmolStructure(pdb,number)
		self.structures.append(structure_tmp)
		return structure_tmp

	def addStructureConstraintFixed(self, x, y, z, a, b, g):
		self.structures[-1].addStructureConstraintFixed(x,y,z,a,b,g)

	def addStructureConstraintInsideCube(self,x_min,y_min,z_min,d):
		self.structures[-1].addStructureConstraintInsideCube(x_min,y_min,z_min,d)

	def addStructureConstraintOutsideCube(self,x_min,y_min,z_min,d):
		self.structures[-1].addStructureConstraintOutsideCube(x_min,y_min,z_min,d)

	def addStructureConstraintInsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.structures[-1].addStructureConstraintInsideBox(x_min,y_min,z_min,x_max,y_max,z_max)

	def addStructureConstraintOutsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.structures[-1].addStructureConstraintOutsideBox(x_min,y_min,z_min,x_max,y_max,z_max)

	def addStructureConstraintInsideSphere(self,a,b,c,d):
		self.structures[-1].addStructureConstraintInsideSphere(a,b,c,d)

	def addStructureConstraintOutsideSphere(self,a,b,c,d):
		self.structures[-1].addStructureConstraintOutsideSphere(a,b,c,d)

	def addStructureConstraintOverPlane(self,a,b,c,d):
		self.structures[-1].addStructureConstraintOverPlane(a,b,c,d)

	def addStructureConstraintBelowPlane(self,a,b,c,d):
		self.structures[-1].addStructureConstraintBelowPlane(a,b,c,d)


class PackmolStructure():
	def __init__(self, pdb, number):
		self.pdb = pdb
		self.number = number
		self.atom_groups = []
		self.constraint_text = ''

	def pickAtoms(self,selected):
		self.atom_groups.append(PackmolAtom(selected))

	def addAtomConstraintFixed(self, x, y, z, a, b, g):
		self.atom_groups[-1].addAtomConstraintFixed(x,y,z,a,b,g)

	def addAtomConstraintInsideCube(self,x_min,y_min,z_min,d):
		self.atom_groups[-1].addAtomConstraintInsideCube(x_min,y_min,z_min,d)

	def addAtomConstraintOutsideCube(self,x_min,y_min,z_min,d):
		self.atom_groups[-1].addAtomConstraintOutsideCube(x_min,y_min,z_min,d)

	def addAtomConstraintInsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.atom_groups[-1].addAtomConstraintInsideBox(x_min,y_min,z_min,x_max,y_max,z_max)

	def addAtomConstraintOutsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.atom_groups[-1].addAtomConstraintOutsideBox(x_min,y_min,z_min,x_max,y_max,z_max)

	def addAtomConstraintInsideSphere(self,a,b,c,d):
		self.atom_groups[-1].addAtomConstraintInsideSphere(a,b,c,d)

	def addAtomConstraintOutsideSphere(self,a,b,c,d):
		self.atom_groups[-1].addAtomConstraintOutsideSphere(a,b,c,d)

	def addAtomConstraintOverPlane(self,a,b,c,d):
		self.atom_groups[-1].addAtomConstraintOverPlane(a,b,c,d)

	def addAtomConstraintBelowPlane(self,a,b,c,d):
		self.atom_groups[-1].addAtomConstraintBelowPlane(a,b,c,d)


	def addStructureConstraintFixed(self,x,y,z,a,b,g):
		self.constraint_text += 'fixed %f %f %f %f %f %f\n'%(x,y,z,a,b,g)

	def addStructureConstraintInsideCube(self,x_min,y_min,z_min,d):
		self.constraint_text += 'inside cube %f %f %f %f\n'%(x_min,y_min,z_min,d)

	def addStructureConstraintOutsideCube(self,x_min,y_min,z_min,d):
		self.constraint_text += 'outside cube %f %f %f %f\n'%(x_min,y_min,z_min,d)

	def addStructureConstraintInsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.constraint_text += 'inside box %f %f %f %f %f %f\n'%(x_min,y_min,z_min,x_max,y_max,z_max)

	def addStructureConstraintOutsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.constraint_text += 'outside box %f %f %f %f %f %f\n'%(x_min,y_min,z_min,x_max,y_max,z_max)

	def addStructureConstraintInsideSphere(self,a,b,c,d):
		self.constraint_text += 'inside sphere %f %f %f %f\n'%(a,b,c,d)

	def addStructureConstraintOutsideSphere(self,a,b,c,d):
		self.csonstraint_text += 'outside sphere %f %f %f %f\n'%(a,b,c,d)

	def addStructureConstraintOverPlane(self,a,b,c,d):
		self.constraint_text += 'over plane %f %f %f %f\n'%(a,b,c,d)

	def addStructureConstraintBelowPlane(self,a,b,c,d):
		self.constraint_text += 'below plane %f %f %f %f\n'%(a,b,c,d)

class PackmolAtom():
	def __init__(self, selected):
		self.selected = selected
		self.constraint_text = ''

	def addAtomConstraintFixed(self,x,y,z,a,b,g):
		self.constraint_text += 'fixed %f %f %f %f %f %f\n'%(x,y,z,a,b,g)

	def addAtomConstraintInsideCube(self,x_min,y_min,z_min,d):
		self.constraint_text += 'inside cube %f %f %f %f\n'%(x_min,y_min,z_min,d)

	def addAtomConstraintOutsideCube(self,x_min,y_min,z_min,d):
		self.constraint_text += 'outside cube %f %f %f %f\n'%(x_min,y_min,z_min,d)

	def addAtomConstraintInsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.constraint_text += 'inside box %f %f %f %f %f %f\n'%(x_min,y_min,z_min,x_max,y_max,z_max)

	def addAtomConstraintOutsideBox(self,x_min,y_min,z_min,x_max,y_max,z_max):
		self.constraint_text += 'outside box %f %f %f %f %f %f\n'%(x_min,y_min,z_min,x_max,y_max,z_max)

	def addAtomConstraintInsideSphere(self,a,b,c,d):
		self.constraint_text += 'inside sphere %f %f %f %f\n'%(a,b,c,d)

	def addAtomConstraintOutsideSphere(self,a,b,c,d):
		self.constraint_text += 'outside sphere %f %f %f %f\n'%(a,b,c,d)

	def addAtomConstraintOverPlane(self,a,b,c,d):
		self.constraint_text += 'over plane %f %f %f %f\n'%(a,b,c,d)

	def addAtomConstraintBelowPlane(self,a,b,c,d):
		self.constraint_text += 'below plane %f %f %f %f\n'%(a,b,c,d)
