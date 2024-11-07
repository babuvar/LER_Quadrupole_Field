#z slices from z=50 to z=110 cm

import basf2
import ROOT
import numpy as np
from ROOT.Belle2 import FileSystem
from ROOT.Belle2 import CDCDatabaseImporter
from ROOT import Belle2
from basf2 import B2INFO



class TestBField(basf2.Module):
	def __init__(self):
		super().__init__()
	def event(self):
	# access to CDC wire hits and tracks:

		B_field=np.zeros((600,600,15,3))
		z_vals=np.zeros(15)
		xy_vals=np.zeros(600)

		z_grid = np.arange(50,200,10)
		xy_grid = np.arange(-30,30,0.1)
		for i_z in range(len(z_grid)):
			for i_x in range(len(xy_grid)):
				for i_y in range(len(xy_grid)):
					zz=z_grid[i_z]					
					xx=xy_grid[i_x]
					yy=xy_grid[i_y]

					pos = ROOT.TVector3(xx, yy, zz)
					b_z = Belle2.BFieldManager.getField(pos).Z()  / Belle2.Unit.T
					b_x = Belle2.BFieldManager.getField(pos).X()  / Belle2.Unit.T
					b_y = Belle2.BFieldManager.getField(pos).Y()  / Belle2.Unit.T
					
					B_field[i_x][i_y][i_z][0]=b_x
					B_field[i_x][i_y][i_z][1]=b_y
					B_field[i_x][i_y][i_z][2]=b_z

					#print ("B-field: ", xx, yy, zz, b_x, b_y, b_z)
		dic={}
		dic['z_grid']=z_grid
		dic['xy_grid']=xy_grid
		dic['B_field']=B_field

		np.save("B2_B_field_quad.npy", dic)


# Geometry
geometry = basf2.register_module('Geometry')
geometry.param('useDB', False)
geometry.param({  
   'excludedComponents': ['MagneticField'],  
   'additionalComponents': ['MagneticField3dQuadBeamline'],  
})

main = basf2.create_path()

# Event info setter - execute single event
eventinfosetter = basf2.register_module('EventInfoSetter')
main.add_module(eventinfosetter)
main.add_module("Gearbox")
main.add_module(geometry)
main.add_module(TestBField())
# process single event
basf2.process(main)





