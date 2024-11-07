#z slices from z=50 to z=110 cm

import basf2
import ROOT
import numpy as np
from ROOT.Belle2 import FileSystem
#from ROOT.Belle2 import CDCDatabaseImporter
from ROOT import Belle2


class TestBField(basf2.Module):
	def __init__(self):
		super().__init__()
	def event(self):
	# access to CDC wire hits and tracks:

		B_field=np.zeros((24,31,7))
		#B_field=np.zeros((72,31,7))
		#phi_vals=np.zeros(24)
		#r_vals=np.zeros(31)
		
		z_grid = np.arange(60,130, 10)
		phi_grid = np.arange(0,360,15)
		#phi_grid = np.arange(0,360,5)
		r_grid = np.arange(0.0,6.2,0.2)
		#print(phi_grid)
		#print(r_grid)

		
		for i_z in range(len(z_grid)): # iterate over z-slices
			for i_phi in range(len(phi_grid)): #iterate over phi
				for i_r in range(len(r_grid)): #iterate over radii
					zz=z_grid[i_z]					
					rr=r_grid[i_r]
					phi=phi_grid[i_phi]
					xx = rr * np.cos(np.deg2rad(phi))
					yy = rr * np.sin(np.deg2rad(phi))
					
					#Position vector of the point where the B-field will be evaluated, in Belle-2 coordiates
					pos = ROOT.TVector3(xx, yy-0.1, zz)
					#Now it has to be rotated to the Quadrupole frame
					pos.RotateY(-0.0415)
				
					bfield = Belle2.BFieldManager.getField(pos)	
					b_z = bfield.Z()  / Belle2.Unit.T
					b_x = bfield.X()  / Belle2.Unit.T
					b_y = bfield.Y()  / Belle2.Unit.T
					
					#B-field evaluated at the correct points on the rotated plane, but in terms of Belle-2 coordinates
					B_fld =  ROOT.TVector3(b_x, b_y, b_z)

					#Get the correct radial vector
					#Position vector of the 2-D origin of the rotated frame (centered around the Quad field) in belle-2 coordinates
					orig = ROOT.TVector3(0.0, -0.1, zz)
					orig.RotateY(-0.0415)
					#Radial vector in rotated coordinates 
					rad = pos - orig
					#Unit radial vector
					unirad= rad.Unit()
					#Correct radial component of B-field
					B_rad = B_fld.Dot(unirad)

					#Fill the numpy B-field array
					B_field[i_phi][i_r][i_z] = B_rad
					
					#Sanity-check	
					#unirad.RotateY(0.0415)
					#unirad.Print()
					#print("=====================================")

		dic={}
		dic['z_grid']=z_grid
		dic['phi_grid']=phi_grid
		dic['r_grid']=r_grid
		dic['B_rad']=B_field
		#np.save("Sol_ArimotoCompare_fine.npy", dic) 
		#np.save("SolQuad_ArimotoCompare_fine.npy", dic) 
		#np.save("Quad.npy", dic) 
		np.save("Varg3D.npy", dic)
			

# Geometry

geometry = basf2.register_module('Geometry')
geometry.param('useDB', False)
geometry.param({  
   'excludedComponents': ['MagneticField'],  
#   'additionalComponents': ['MagneticField3dQuadBeamline']
#   'additionalComponents': ['QuadField']
   'additionalComponents': ['QuadField3D']
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





