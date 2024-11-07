import basf2
import ROOT
import numpy as np
from ROOT.Belle2 import FileSystem
from ROOT.Belle2 import CDCDatabaseImporter
from ROOT import Belle2


class TestBField(basf2.Module):
    def __init__(self):
        super().__init__()
    def event(self):
        # access to CDC wire hits and tracks:
        z = np.arange(-200,200,2)
        for zz in list(z):
            pos = ROOT.TVector3(0.,-zz*0.045,zz)
            b = Belle2.BFieldManager.getField(pos).Z()  / Belle2.Unit.T
            print ("z,field:",zz,b)

main = basf2.create_path()

# Event info setter - execute single event
eventinfosetter = basf2.register_module('EventInfoSetter')
main.add_module(eventinfosetter)
main.add_module("Gearbox")
main.add_module("Geometry", useDB=True)
main.add_module(TestBField())
# process single event
basf2.process(main)
