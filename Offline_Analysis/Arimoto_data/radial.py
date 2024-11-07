import numpy as np
#from ROOT  import  gROOT, TCanvas, TH2F, TObjArray, TGraph2D, gStyle, gPad, TVector2
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as pl

#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_cyl_ler_l.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_rcanAll_cyl_ler_l.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-rcanAll_cyl_ler_l.table")


names=['qc1rp', 'qc1rp_rcanAll', 'rcanAll']



data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-%s_cyl_ler_s.table"%names[0])
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_rcanAll_cyl_ler_s.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-rcanAll_cyl_ler_s.table")


z_slices=[-0.6, -0.7, -0.8, -0.9, -1.0, -1.1, -1.2]
#z_slices=[-0.7, -0.8, -0.9, -1.0, -1.1]


for name in names:
    data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-%s_cyl_ler_s.table"%name)


    for zval in z_slices:


        Br=np.zeros((31, 24)) # r, phi
        rad=np.zeros((31))
        phi=np.zeros((24))

        for i in range (31):
            rad[i]=float(i)*0.002
    
        for i in range (24):
            phi[i]=i*15


        for i in range(data.shape[0]):
            if data[i][2] == zval:
                Br[int(data[i][0]/0.002)][int(data[i][1]/15)]=data[i][3]



        fig=pl.figure(figsize=(30,20))
        for i in range(12):
            pl.subplot(4,3,i+1); pl.plot(rad, Br[:,i], marker='o'); pl.title('z=%s m, phi = %s deg'%(zval, phi[i]), color='blue')
            pl.ylabel('B_r (Tesla)'); pl.xlabel('radius (m)');
        fig.savefig("plots_rad/plot_%s_z_%sm.png"%(name,zval))
        pl.close(fig)



