import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib
import seaborn as sns


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'






T=np.loadtxt("temps_index.txt")[:,1]
E=np.loadtxt("temps_index.txt")[:,0]
print("index", "T")
for i in range(9):
    print(i*10,T[i] )
#opacity=0.5
N_bins=80
opacity=0.6


fig=plt.figure(figsize=(20,10))
plt.subplots_adjust(left=0.05, bottom=None, right=0.98, top=0.95, wspace=0.35, hspace=0.40)
ax = fig.add_subplot(111,projection='3d')
label_size=18

temp_index_list=["0","40"]
#    temp_index_list=["0","20","40"]
MT2_average=[]
MT1xy_average=[]
MT1Ice_average=[]
ME_average=[]
MA2_average=[]
cmap=plt.get_cmap("jet_r")
cmap_list=cmap(np.linspace(0,1,4))
colors_list=cmap(np.linspace(0.1,0.3,2))
#    colors_list=["red","goldenrod","green"]
for i in range(len(temp_index_list)):

    temp_index=temp_index_list[i]
    
    input_irreps="irreps_"+temp_index+"_theta243.bin"
   
    File=np.loadtxt(input_irreps)
    T_index=T[int(temp_index)//10]
   
    
   
    mt2=File[0,:]
    mt1xy=File[1,:]
    mt1ice=File[2,:]
    mE=File[3,:]
    mA2=File[4,:]
    print("len of the files =%d" %len(mA2) )

    
    plt.subplot(3,5,1)
    plt.hist(mt1ice,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index))
#    sns.distplot(mt1ice,hist=False,kde=True)
#    sns.displot(mt1ice,hist=False,kde=True)#, hist=True, kde=True,bins=N_bins,color= colors_list[i])#, hist_kws={'edgecolor':'black'})#,             kde_kws={'linewidth': 4})
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index=="40"):
#        plt.legend()
        plt.title(r"$T_1^{\mathrm{Ice}}$",size=label_size)
        plt.tick_params(labelsize=label_size)
    plt.xlim(0,1)
    
    
    plt.subplot(3,5,2)
    plt.hist(mt1xy,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index,))
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index=="40"):
#        plt.legend()
        plt.title(r"$T_1^{xy}$",size=label_size)
        plt.tick_params(labelsize=label_size)
    plt.xlim(0,1)
    plt.subplot(3,5,3)
    plt.hist(mE,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index))
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index=="40"):
#        plt.legend()
        plt.title(r"$E$",size=label_size)
        plt.tick_params(labelsize=label_size)
    plt.xlim(0,1)
    xlim_high=1
    plt.subplot(3,5,4)
    plt.hist(mt2,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index,))
    plt.xlim(0,xlim_high)
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index=="40"):
#        plt.legend(prop={'size': 15})
        plt.title(r"$T_2$",size=label_size)
        plt.tick_params(labelsize=label_size)
    plt.xlim(0,1)

    plt.subplot(3,5,5)
    plt.hist(abs(mA2),bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.3f$" %(T_index))
    plt.xlim(0,xlim_high)
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index=="40"):
        plt.legend(prop={'size': 15})
        plt.title(r"$A_2$",size=label_size)
        plt.tick_params(labelsize=label_size)
    plt.xlim(0,1)



    
      

temp_index_list=["50","60"]
colors_list=cmap(np.linspace(0.75,0.95,2))
opacity=0.7

for i in range(len(temp_index_list)):

    temp_index=temp_index_list[i]
    T_index=T[int(temp_index)//10]
     
    input_irreps="irreps_"+temp_index+"_theta243.bin"
   
    File=np.loadtxt(input_irreps)
    T_index=T[int(temp_index)//10]
   
    
   
    mt2=File[0,:]
    mt1xy=File[1,:]
    mt1ice=File[2,:]
    mE=File[3,:]
    mA2=File[4,:]
    print("len of the files =%d" %len(mA2) )
 
#    N_bins=50
    opacity=0.4
    plt.subplot(3,5,6)
    plt.hist(mt1ice,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index))
#    plt.yticks([0,50,100])
    plt.grid()
    plt.xlim(0,1)
    if(temp_index==temp_index_list[-1]):
#        plt.legend()
        plt.tick_params(labelsize=label_size)
#        plt.yticks([0,50,100,150])

        input_irreps="irreps_averages_theta243.bin"
        File=np.loadtxt(input_irreps)

        T_arrows=File[:,0]

        opacity_arrows=0.5
        label_size_arrows=20
        colors_list=cmap(np.linspace(0.1,0.3,2))
        plt.text(1.047,-12000,r"$\downarrow$",color=colors_list[0],alpha=opacity,size=label_size_arrows)
        plt.text(0.665,-12000,r"$\downarrow$",color=colors_list[1],alpha=opacity,size=label_size_arrows)

        colors_list=cmap(np.linspace(0.75,0.95,2))
        plt.text(0.54,-12000,r"$\downarrow$",color=colors_list[0],alpha=opacity,size=label_size_arrows)
        plt.text(0.344,-12000,r"$\downarrow$",color=colors_list[1],alpha=opacity,size=label_size_arrows)

    plt.subplot(3,5,7)
    plt.hist(mt1xy,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index,))
    plt.xlim(0,1)
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index==temp_index_list[-1]):
#        plt.legend()
        plt.tick_params(labelsize=label_size)
    plt.subplot(3,5,8)
    plt.hist(mE,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index))
    plt.xlim(0,1)
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index==temp_index_list[-1]):
#        plt.legend()
        plt.tick_params(labelsize=label_size)
   
    plt.subplot(3,5,9)
    plt.hist(mt2,bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.4f$" %(T_index,))
#        plt.xlim(0,1)
#    plt.yticks([0,50,100])
    plt.grid()
    if(temp_index==temp_index_list[-1]):
#        plt.legend()
        plt.tick_params(labelsize=label_size)
    plt.xlim(0,0.15)
    plt.subplot(3,5,10)
    plt.hist(abs(mA2),bins=N_bins,color=colors_list[i],alpha=opacity,label=r"$T=%.3f$" %(T_index))
#        plt.xlim(0,1)
#    plt.yticks([0,50,100])
    plt.grid()
    plt.xlim(0,0.15)
    if(temp_index==temp_index_list[-1]):
        plt.legend(prop={'size': 15})
        plt.tick_params(labelsize=label_size)

   
    

input_irreps="irreps_averages_theta243.bin"
File=np.loadtxt(input_irreps)

T=File[:,0]
MT1Ice_average=File[:,1]
MT1xy_average=File[:,2]
ME_average=File[:,3]
MT2_average=File[:,4]
MA2_average=File[:,5]


size_lines=2
linewidth=3

plt.subplot(3,3,7)
plt.semilogx(T,MT1Ice_average,"k.-",label=r"$T_1^{\mathrm{Ice}}$",linewidth=size_lines)
plt.xlabel(r"$T$",size=label_size)

plt.semilogx(T,MT1xy_average,"r.-",label=r"$T_1^{xy}$",linewidth=size_lines)
plt.semilogx(T,ME_average,".-",color="b",label=r"$E$",linewidth=size_lines)
plt.semilogx(T,MT2_average,"g.-",label=r"$T_2$",linewidth=size_lines)
plt.semilogx(T,MA2_average,".-",color="purple",label=r"$A_2$",linewidth=size_lines)
plt.axvline(0.03,linestyle="-.",color="gray",linewidth=2)
plt.legend(prop={'size': 15},mode = "expand", ncol = 5)
plt.ylim(0,1.4)
plt.xlim(min(T),max(T))
colors_list=cmap(np.linspace(0.1,0.3,2))

plt.axvline(T[5],color=colors_list[0],alpha=opacity,linewidth=linewidth)
plt.axvline(T[9],color=colors_list[1],alpha=opacity,linewidth=linewidth)
plt.text(T[5]+0.1,0.75,r"$\leftarrow \sim T_{\mathrm{gl}}$",color="k",size=label_size)
plt.text(0.0237,-0.1,r"$\uparrow$",color="k",size=label_size)
plt.text(0.0237,-0.25,r"$T^\ast$",color="k",size=label_size)


colors_list=cmap(np.linspace(0.75,0.95,2))
plt.axvline(T[10],color=colors_list[0],alpha=opacity,linewidth=linewidth)
plt.axvline(T[11],color=colors_list[1],alpha=opacity,linewidth=linewidth)
#plt.text(T[10]-1,1.5,r"$\downarrow$",color=colors_list[0],alpha=opacity,size=label_size)
#plt.text(T[11]-1,1.5,r"$\downarrow$",color=colors_list[1],alpha=opacity,size=label_size)


plt.grid()
plt.tick_params(labelsize=label_size)
plt.subplot(3,3,9)
#plt.semilogx(T,MT1xy_average,"k.-",label=r"$T_1^{xy}$")
#plt.semilogx(T,ME_average,".-",color="gray",label=r"$E$")
plt.semilogx(T,MT2_average,"g.-",label=r"$T_2$",linewidth=size_lines)
plt.semilogx(T,MA2_average,".-",color="purple",label=r"$A_2$",linewidth=size_lines)
plt.xlabel(r"$T$",size=label_size)
plt.legend(prop={'size': 15}, ncol = 2,loc=2)
plt.xlim(min(T),max(T))
plt.ylim(0,0.7)
plt.grid()
plt.tick_params(labelsize=label_size)
colors_list=cmap(np.linspace(0.1,0.3,2))
#linewidth=5
#plt.axvline(T[5],color=colors_list[0],alpha=opacity,linewidth=linewidth)
#plt.axvline(T[9],color=colors_list[1],alpha=opacity,linewidth=linewidth)
#colors_list=cmap(np.linspace(0.75,0.95,2))
#plt.axvline(T[10],color=colors_list[0],alpha=opacity,linewidth=linewidth)
#plt.axvline(T[11],color=colors_list[1],alpha=opacity,linewidth=linewidth)



plt.subplot(3,3,8)
plt.semilogx(T,MT1xy_average,"r.-",label=r"$T_1^{xy}$",linewidth=size_lines)
plt.semilogx(T,ME_average,".-",color="b",label=r"$E$",linewidth=size_lines)
plt.xlabel(r"$T$",size=label_size)
plt.legend(prop={'size': 15}, ncol = 2,loc=2)
plt.grid()
plt.tick_params(labelsize=label_size)
colors_list=cmap(np.linspace(0.1,0.3,2))
#linewidth=5
#plt.axvline(0.03,linestyle="-.",color="gray",linewidth=2)
#plt.axvline(T[5],color=colors_list[0],alpha=opacity,linewidth=linewidth)
#plt.axvline(T[9],color=colors_list[1],alpha=opacity,linewidth=linewidth)
#colors_list=cmap(np.linspace(0.75,0.95,2))
#plt.axvline(T[10],color=colors_list[0],alpha=opacity,linewidth=linewidth)
#plt.axvline(T[11],color=colors_list[1],alpha=opacity,linewidth=linewidth)

plt.xlim(min(T),max(T))
plt.ylim(0,0.7)
plt.savefig("Figure_2_option2.pdf")
plt.show()
    

    




