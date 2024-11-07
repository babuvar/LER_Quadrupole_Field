import numpy as np
#from ROOT  import  gROOT, TCanvas, TH2F, TObjArray, TGraph2D, gStyle, gPad, TVector2
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as pl


#----------------------------------------------------------------------------------------
#Belle II Quad field map
#----------------------------------------------------------------------------------------

#dic=np.load('B_field_quad_alongBeam_ArimotoCompare.npy')
dic=np.load('SolQuad_ArimotoCompare_fine.npy') #with 1mm vertical offset
rvals = dic[()]['r_grid']
zvals = dic[()]['z_grid']
phivals = dic[()]['phi_grid']
B_r = dic[()]['B_rad']



#dic_wo=np.load('B_field_alongBeam_ArimotoCompare.npy')#without quadrupole field
dic_wo=np.load('Sol_ArimotoCompare_fine.npy')
B_r_wo = dic_wo[()]['B_rad']

diff_max=np.max(B_r - B_r_wo)
diff_min=np.min(B_r - B_r_wo)

#----------------------------------------------------------------------------------------





#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_cyl_ler_l.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_rcanAll_cyl_ler_l.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-rcanAll_cyl_ler_l.table")


names=['qc1rp', 'qc1rp_rcanAll', 'rcanAll']



#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-%s_cyl_ler_s.table"%names[0])
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-qc1rp_rcanAll_cyl_ler_s.table")
#data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/B2_Magnetic/Arimoto_data/data/200201-rcanAll_cyl_ler_s.table")


z_slices=[-0.6, -0.7, -0.8, -0.9, -1.0, -1.1, -1.2]
#z_slices=[-0.7, -0.8, -0.9, -1.0, -1.1]


for name in names:
    data = np.loadtxt(fname = "/home/bonndaq_pc/tmp_varghese/Magnetic/Arimoto_data/data/200201-%s_cyl_ler_s.table"%name)


    for i_z in range(7):

        zval = z_slices[i_z]


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


        '''
        fig=pl.figure(figsize=(30,20))
        for i in range(12):
            pl.subplot(4,3,i+1); 
            pl.plot(100*rad, Br[:,i], marker='o', label='Arimoto-san field'); pl.title('z=%s m, phi = %s deg'%(zval, phi[i]), color='blue')
            pl.plot(rvals, B_r[-i,:,i_z], marker='o', color='red', label='Belle-2 Solenoid+Quad Field')
            pl.plot(rvals, B_r_wo[-i,:,i_z], marker='o', color='green', label='Belle-2 Solenoid Field')
            pl.ylabel('B_r (Tesla)'); pl.xlabel('radius (cm)');
            pl.legend(loc='lower right')
        fig.savefig("plots_compare/plot_%s_z_%sm.png"%(name,zval))
        pl.close(fig)
        '''

        fig=pl.figure(figsize=(30,20))
        for i in range(12):
            pl.subplot(4,3,i+1);
            pl.plot(100*rad, Br[:,i], marker='o', label='Arimoto-san field'); pl.title('z=%s m, phi = %s deg'%(zval, phi[i]), color='blue')
            pl.plot(rvals, B_r[-i,:,i_z] - B_r_wo[-i,:,i_z], marker='o', color='orange', label='Belle-2 Quad Field Alone')
            pl.ylabel('B_r (Tesla)'); pl.xlabel('radius (cm)'); 
            #pl.legend(loc='lower right'); pl.ylim((diff_min, diff_max))
            pl.legend(loc='lower right'); pl.ylim((2.2, -2.2))
        fig.savefig("plots_compare/diff_%s_z_%sm.png"%(name,zval))
        pl.close(fig)
        
        #print "max=", np.max(Br)
        #print "min=", np.min(Br)
        print "z = %s, name = %s is done"%(zval, name)











