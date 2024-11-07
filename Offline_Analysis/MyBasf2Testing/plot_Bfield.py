import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as pl
import tables
import os
#from scipy.ndimage import gaussian_filter
from ROOT import  gROOT, TCanvas, TH2F, TObjArray, TGraph2D, gStyle, gPad, TVector2
import ROOT

gROOT.SetBatch(True)

dic=np.load('Varghese3D.npy') #contains objects 'xy_grid', 'z_grid' and 'B_field'



xy = dic[()]['xy_grid']
z = dic[()]['z_grid']
B_f = dic[()]['B_field']


#gStyle.SetPalette(55)  #kRainbow
gStyle.SetPalette(104) #kTemperatureMap

gStyle.SetNumberContours(999)
gStyle.SetOptStat(0)
#gPad.SetRightMargin(0.05)


zvals=np.array([-120,-110,-100,-90,-80,-70])

for i_z in range(len(zvals)):


    histx=TH2F( 'histx', 'X-component of B @ Z = %s cm'%zvals[i_z], 200, -10, 10, 200, -10, 10 )
    histy=TH2F( 'histy', 'Y-component of B @ Z = %s cm'%zvals[i_z], 200, -10, 10, 200, -10, 10 )
    histz=TH2F( 'histz', 'Z-component of B @ Z = %s cm'%zvals[i_z], 200, -10, 10, 200, -10, 10 )
    histr=TH2F( 'histr', 'Radial component of B @ Z = %s cm'%zvals[i_z], 200, -10, 10, 200, -10, 10 )


    for i_x in range(len(xy)):
        for i_y in range(len(xy)):
            
            histx.Fill(float(xy[i_x]), float(xy[i_y]),float(B_f[i_x][i_y][i_z][0]))
            histy.Fill(float(xy[i_x]), float(xy[i_y]),float(B_f[i_x][i_y][i_z][1]))
            histz.Fill(float(xy[i_x]), float(xy[i_y]),float(B_f[i_x][i_y][i_z][2]))
            #radial component
            B_vec = TVector2(B_f[i_x][i_y][i_z][0], B_f[i_x][i_y][i_z][1])
            n_vec = TVector2(xy[i_x], xy[i_y])
            n_vec = n_vec.Unit()
            B_r = B_vec * n_vec
            histr.Fill(float(xy[i_x]), float(xy[i_y]),float(B_r))


    histx.SetXTitle("X (cm)"); histx.SetYTitle("Y (cm)"); histx.GetZaxis().SetTitle("B_{x} (Tesla)")
    histy.SetXTitle("X (cm)"); histy.SetYTitle("Y (cm)"); histy.GetZaxis().SetTitle("B_{y} (Tesla)")
    histz.SetXTitle("X (cm)"); histz.SetYTitle("Y (cm)"); histz.GetZaxis().SetTitle("B_{z} (Tesla)")
    histr.SetXTitle("X (cm)"); histr.SetYTitle("Y (cm)"); histr.GetZaxis().SetTitle("B_{r} (Tesla)")



    #c1 = TCanvas()
    c1 = TCanvas('','',1400,1200)
    c1.Divide(2,2)
    c1.cd(1); histx.Draw("COLZ"); gPad.SetRightMargin(0.2)
    c1.cd(2); histy.Draw("COLZ"); gPad.SetRightMargin(0.2)
    c1.cd(3); histz.Draw("COLZ"); gPad.SetRightMargin(0.2)
    c1.cd(4); histr.Draw("COLZ"); gPad.SetRightMargin(0.2)
    
    c1.SaveAs('B_field_%scm.png'%zvals[i_z])
    c1.Close()
    del histx; del histy; del histz; del histr

















