import numpy as np
from ROOT  import  gROOT, TCanvas, TH2F, TObjArray, TGraph2D, gStyle, gPad, TVector2, TMath
#import matplotlib as mpl
#mpl.use('Agg')
#from matplotlib import pyplot as pl

gROOT.SetBatch(True)
gStyle.SetPalette(104)
gStyle.SetNumberContours(999)
gStyle.SetOptStat(0)

z_slices=[-0.6, -0.7, -0.8, -0.9, -1.0, -1.1, -1.2]
#z_slices=[-0.8]

#for name in names:
data = np.loadtxt(fname = "Varghese3D.dat")


for i_z in range(7):
    zval = z_slices[i_z]

    #Histogram definitions
    low_phi = (TMath.Pi()*-2.5)/180; high_phi = (TMath.Pi()*357.5)/180;
    hist_Br = TH2F( 'histBr', '', 72, low_phi, high_phi, 31, 0, 0.0601 )
    hist_Bphi = TH2F( 'histBphi', '', 72, low_phi, high_phi, 31, 0, 0.0601 )
    hist_Bz = TH2F( 'histBz', '', 72, low_phi, high_phi, 31, 0, 0.0601 )
    hist_Bx = TH2F( 'histBx', '', 72, low_phi, high_phi, 31, 0, 0.0601 )
    hist_By = TH2F( 'histBy', '', 72, low_phi, high_phi, 31, 0, 0.0601 )
    #hist_Bx = TH2F( 'histBx', '', 72, low_phi, high_phi, 31, 0, 0.0601 )



    '''
    Br=np.zeros((31, 72)) # r, phi
    rad=np.zeros((31))
    phi=np.zeros((72))

    for i in range (31):
        rad[i]=float(i)*0.002+0.000001
   
    for i in range (72):
        phi[i]=float(i)*5
    '''

    for i in range(data.shape[0]):
        if data[i][2] == zval:
            bx = ( float(data[i][3]) * np.cos( float(data[i][1])*TMath.Pi()/180.0 ) )  -  ( float(data[i][4]) * np.sin( float(data[i][1])*TMath.Pi()/180.0 ) ) ; 
            by = ( float(data[i][3]) * np.sin( float(data[i][1])*TMath.Pi()/180.0 ) )  +  ( float(data[i][4]) * np.cos( float(data[i][1])*TMath.Pi()/180.0 ) ) ;

            hist_Br.Fill( float(data[i][1])*TMath.Pi()/180.0, float(data[i][0])+0.000001, float(data[i][3]) )
            hist_Bphi.Fill( float(data[i][1])*TMath.Pi()/180.0, float(data[i][0])+0.000001, float(data[i][4]) )
            hist_Bz.Fill( float(data[i][1])*TMath.Pi()/180.0, float(data[i][0])+0.000001, float(data[i][5]) )
            hist_Bx.Fill( float(data[i][1])*TMath.Pi()/180.0, float(data[i][0])+0.000001, bx)
            hist_By.Fill( float(data[i][1])*TMath.Pi()/180.0, float(data[i][0])+0.000001, by)

    #Plotting
    c1 = TCanvas('c1','',1600,1600); 
    c1.cd(); gPad.DrawFrame(-0.07, -0.07, 0.07, 0.07); hist_Br.SetTitle('B_r @ z = %s m'%zval); hist_Br.Draw("SAME COLZ POL");
    c1.SaveAs("Br_%sm.png"%(zval));

    c2 = TCanvas('c2','',1600,1600);
    c2.cd(); gPad.DrawFrame(-0.07, -0.07, 0.07, 0.07); hist_Bphi.SetTitle('B_phi @ z = %s m'%zval); hist_Bphi.Draw("SAME COLZ POL");
    c2.SaveAs("Bphi_%sm.png"%(zval));

    c3 = TCanvas('c3','',1600,1600)
    c3.cd(); gPad.DrawFrame(-0.07, -0.07, 0.07, 0.07); hist_Bz.SetTitle('B_z @ z = %s m'%zval); hist_Bz.Draw("SAME COLZ POL");
    c3.SaveAs("Bz_%sm.png"%(zval));

    c4 = TCanvas('c4','',1600,1600)
    c4.cd(); gPad.DrawFrame(-0.07, -0.07, 0.07, 0.07); hist_Bx.SetTitle('B_x @ z = %s m'%zval); hist_Bx.Draw("SAME COLZ POL");
    c4.SaveAs("Bx_%sm.png"%(zval));

    c5 = TCanvas('c5','',1600,1600)
    c5.cd(); gPad.DrawFrame(-0.07, -0.07, 0.07, 0.07); hist_By.SetTitle('B_y @ z = %s m'%zval); hist_By.Draw("SAME COLZ POL");
    c5.SaveAs("By_%sm.png"%(zval));

    c1.Close(); c2.Close(); c3.Close(); c4.Close(); c5.Close();
    del hist_Br; del hist_Bphi; del hist_Bz; del hist_Bx; del hist_By;
    print("plot at z = %s is done"%(zval))










