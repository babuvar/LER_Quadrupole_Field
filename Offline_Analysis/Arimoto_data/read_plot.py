import numpy as np
from ROOT  import  gROOT, TCanvas, TH2F, TObjArray, TGraph2D, gStyle, gPad, TVector2
import math as mt

#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_cyl_ler_l.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_rcanAll_cyl_ler_l.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-rcanAll_cyl_ler_l.table")


names=['qc1rp', 'qc1rp_rcanAll', 'rcanAll']



#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-%s_cyl_ler_s.table"%names[0])
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_rcanAll_cyl_ler_s.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-rcanAll_cyl_ler_s.table")


z_slices=[-0.6, -0.7, -0.8, -0.9, -1.0, -1.1, -1.2]


gStyle.SetPalette(104) #kTemperatureMap
gStyle.SetNumberContours(999)


for name in names:
    data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-%s_cyl_ler_s.table"%name)

    for zval in z_slices:

        gr_Br = TGraph2D(); gr_Br.SetTitle("Radial component of B @ Z =  %s (m) [file=%s] ; X (m); Y (m) ; B_{r} (Tesla) "%(zval, name) ); gr_Br.SetMarkerSize(0.5);
        count = -1;

        for i in range(data.shape[0]):
            if data[i][2] == zval:
                x = data[i][0] *  np.cos(np.deg2rad(data[i][1]))
                y = data[i][0] *  np.sin(np.deg2rad(data[i][1]))
                count += 1
                gr_Br.SetPoint(count, float(x), float(y), float(mt.cos(data[i][3])) )



        #plots
        c1 = TCanvas('c1','', 200, 10, 1150, 1100);
        c1.cd(); gr_Br.Draw('TRI2Z'); gr_Br.Draw('P0 SAME'); gPad.SetPhi(0);  gPad.SetTheta(90)
        gPad.SetRightMargin(0.15); gPad.SetLeftMargin(0.1); gPad.SetBottomMargin(0.1);
        c1.SaveAs('plots/Br_Map_%s%sm.png'%(name,zval))
        del c1; del gr_Br


raw_input()
