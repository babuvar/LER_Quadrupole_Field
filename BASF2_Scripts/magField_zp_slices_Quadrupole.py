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
		'''
		B_field=np.zeros((400,400,15,2)) # only retaining B_r and B_z
		z_vals=np.zeros(15)
		xy_vals=np.zeros(400)
		z_grid = np.arange(50,200,10)
		xy_grid = np.arange(-10,10,0.05)
		'''

		B_field=np.zeros((140,140,7,2))
		z_vals=np.zeros(7)
		xy_vals=np.zeros(140)
		xy_grid = np.arange(-7,7,0.1)
		z_mid = [x for x in range(70, 115, 10)]; z_p = [119.9]; z_m = [60.1]
		z_grid=z_m+z_mid+z_p; z_grid=np.asarray(z_grid)

		#xy_grid = np.arange(-2,2,0.01)
		for i_z in range(len(z_grid)):
			for i_x in range(len(xy_grid)):
				for i_y in range(len(xy_grid)):
					zz= z_grid[i_z] 
					xx=xy_grid[i_x]
					yy=xy_grid[i_y]
					rr=np.sqrt( (xx*xx) + (yy*yy) )
					#B2INFO("---------------------------------------------")
					#B2INFO("Input point = %s %s %s"%(xx, yy, zz))
					#B2INFO("Input r = ", rr)
					#B2INFO("Input z = ", zz)
					#pos = ROOT.TVector3(np.double(xx), np.double(yy-0.1), np.double(zz))
					pos = ROOT.TVector3(np.double(xx), np.double(yy), np.double(zz))
					#Now it has to be rotated in
					pos.RotateY(-0.0415)
					
					Bfield = Belle2.BFieldManager.getField(pos)
					b_z = Bfield.Z()  / Belle2.Unit.T
					b_x = Bfield.X()  / Belle2.Unit.T
					b_y = Bfield.Y()  / Belle2.Unit.T
					
					#The LER beamline is 1 mm vertically down 
					B_fld =  ROOT.TVector3(b_x, b_y, b_z)


					orig = ROOT.TVector3(0.0, -0.1, zz)
					orig.RotateY(-0.0415)
					rad = pos - orig
					unirad = rad.Unit()
					zp = ROOT.TVector3(0, 0, zz)
					zp.RotateY(-0.0415) 
					unizp = zp.Unit()
					B_rad = B_fld.Dot(unirad)
					B_zp = B_fld.Dot(unizp)
					

					B_field[i_x][i_y][i_z][0] = B_rad #radial component (primed frame)
					B_field[i_x][i_y][i_z][1] = B_zp #z-component  (primed frame)

					#print ("B-field: ", xx, yy, zz, b_x, b_y, b_z)
		dic={}
		dic['z_grid']=z_grid
		dic['xy_grid']=xy_grid
		dic['B_field']=B_field


		#np.save("Sol+Quad_alongBeam_fine.npy", dic)
		#np.save("Sol_alongBeam_fine.npy", dic)
		np.save("Varg3D_slices.npy", dic)
		#np.save("Quad_slices.npy", dic)

# Geometry
geometry = basf2.register_module('Geometry')
geometry.param('useDB', False)
geometry.param({  
   'excludedComponents': ['MagneticField'],  
#   'additionalComponents': ['MagneticField3dQuadBeamline']
   'additionalComponents': ['QuadField3D']
#   'additionalComponents': ['QuadField']

})

main = basf2.create_path()

# Event info setter - execute single event
eventinfosetter = basf2.register_module('EventInfoSetter')
main.add_module(eventinfosetter)
main.add_module("Gearbox")
main.add_module(geometry)
#main.add_module("Geometry", useDB=True)
main.add_module(TestBField())
# process single event
basf2.process(main)





