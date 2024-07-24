limport numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib
import cmath
from matplotlib import gridspec
import matplotlib.colors


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


'''
------------------------------------------------ Function plot --------------------------------------------------------------------------------
'''
Jzz=3
def func_T1xy(x):
    y=[]
    Jpm=x
    for x in Jpm:
    
        if(x<=Jpm1*Jzz):
            y.append(0)
            
        elif(x<=Jpm2*Jzz):
            y.append(-1*Jzz/4-x/2)
        else:
            y.append(-2*x)
    return y

def func_T2(x):
    y=[]
    Jpm=x
    for x in Jpm:
        if(x<Jpm1*Jzz):
            y.append(0)
        elif(x<Jpm2*Jzz):
            y.append(1*Jzz/4+x/2)
        else:
            y.append(+2*x)
    return y

'''
------------------------------------------------ Function plot --------------------------------------------------------------------------------
'''

fig = plt.figure(figsize=(18,8))
spec = gridspec.GridSpec(ncols=3, nrows=2,left=0.08,bottom=0.08,right=0.98,top=0.99,wspace=0.6,hspace=0.25)

ax = fig.add_subplot(spec[0,0])
'''
------------------------------------------------ Main plot --------------------------------------------------------------------------------
'''
linewidth=2

Jpm=np.linspace(-2,1,200)*Jzz
y1=1/4+Jpm/2
y2=-1/4-Jpm/2
y3=-2*Jpm


Jpm1=(-1/2)
Jpm2=(1/6)

size_label_irreps=20
T1xy=np.array(func_T1xy(Jpm))
T2=np.array(func_T2(Jpm))

plt.plot(Jpm,T1xy,"k",linewidth=linewidth,zorder=1)
plt.plot(Jpm,T2,"k",linewidth=linewidth,zorder=1)
plt.plot(1/6*np.ones(50)*Jzz,np.linspace(-1/3,1/3,50)*Jzz,"k",linewidth=linewidth,zorder=1)

plt.fill_between(Jpm,-2*np.ones(len(Jpm)),T1xy,color="orange",alpha=0.6)
plt.fill_between(Jpm,T2,2*np.ones(len(Jpm)),color="red",alpha=0.7)

#plt.fill_between(Jpm,-2*np.ones(len(Jpm)),T1xy,color="orangered",alpha=0.6)
#plt.fill_between(Jpm,T2,2*np.ones(len(Jpm)),color="g",alpha=0.6)
plt.text(-1,1,r"$T_2}$",size=size_label_irreps)
plt.text(-1,-1.5,r"$T_1^{xy}$",size=size_label_irreps)

Jpm=np.linspace(-1/2,1/6)*Jzz
T1xy=func_T1xy(Jpm)
T2=func_T2(Jpm)
plt.fill_between(Jpm,T1xy,T2,color="gray",alpha=0.4)
plt.text(-0.4,-0.05,r"$T_1^{\mathrm{Ice}}$",size=size_label_irreps-1)

Jpm=np.linspace(1/6,1)*Jzz
T1xy=func_T1xy(Jpm)
T2=func_T2(Jpm)
plt.plot(Jpm,0*Jpm,"k",linewidth=linewidth)
plt.fill_between(Jpm,0*Jpm,T2,color="royalblue",alpha=0.7)
plt.fill_between(Jpm,T1xy,0*Jpm,color="dodgerblue",alpha=0.7)
plt.text(1,-1,r"$E(\psi_{_3})$",size=size_label_irreps)
plt.text(1,1,r"$E(\psi_{_2})$",size=size_label_irreps)

#
cut_plot=2
cut_plot_x=2
plt.ylim(-cut_plot,cut_plot)
plt.xlim(-cut_plot,cut_plot_x)
plt.xticks([-2,-1,0,1,2])
plt.yticks([-2,-1,0,1,2])
plt.gca().set_aspect(1/np.sqrt(2))
plt.xlabel(r"$J_\pm$",size=size_label_irreps)
plt.ylabel(r"$J_{\pm\pm}$",size=size_label_irreps)

linewidth_points=100

plt.scatter([1/6*Jzz],[-1/3*Jzz],c="w",s=linewidth_points,alpha=1,zorder=2)
plt.scatter([1/6*Jzz],[1/3*Jzz],c="w",s=linewidth_points,alpha=1,zorder=2,marker="*")
plt.scatter([-1/2*Jzz],[0],c="k",s=linewidth_points,alpha=1,zorder=2)

plt.tick_params(labelsize=size_label_irreps)
plt.gca().set_aspect(1/np.sqrt(3))

'''
------------------------------------------------ Inset plot --------------------------------------------------------------------------------
'''


ax = fig.add_subplot(spec[1,0])

'''
Parameters of the averaged runs
'''

sizex="10"#input("Enter size of x=")#input("Enter the size of the lattice=")
sizey=sizex
sizez=sizex

Theta="243"#input("Enter the value of theta with sign=")
N=50#int(input("Number of temperature points="))



label=["-0.001","-0.01","-0.02","-0.05","-0.1"]



max_sim_num=1000#int(input("Enter max number of sim number ="))+1
print("Max number of simularions = %d" %max_sim_num)
print("Including factor of \sqrt{3/2} in M_T1_planar \n")
num_average_simulations=0


resp_sizes=1
L_size_list=["12","10","8","6"][::-1]

markers_L=["s-","o-","^-","v-"]
col=["b","k","g","r"]


for i in range(len(L_size_list)):
    L_size=L_size_list[i]
    file_name="average_thermodynamic_data_L"+L_size+".txt"
    my_file = Path(file_name)

    if (my_file.is_file()):
     
        FILE=np.loadtxt(file_name)
        T=FILE[:,0]
        C_v=FILE[:,2]
        plt.semilogx(T,C_v,markers_L[i],color=col[i],alpha=0.5,fillstyle='none',label=r"$L=%i$" %(int(L_size)))
        
plt.xlim(min(T),max(T))
plt.xlabel("$ T $",size=size_label_irreps)
plt.ylabel(r"$ C/k_{\mathrm{B}} $",size=size_label_irreps)
plt.legend(loc=3,prop={'size': 15},ncol = 2)
T_ice_temp=np.linspace(min(T),0.03)
T_all_temp=np.linspace(0.03,max(T))
alpha_t=0.4
plt.fill_between(T_ice_temp,np.ones(len(T_ice_temp))*9/8*0.94,np.ones(len(T_ice_temp))*9/8,color="gray",alpha=alpha_t)
plt.fill_between(T_all_temp,np.ones(len(T_all_temp))*9/8*0.94,np.ones(len(T_all_temp))*9/8,color="slateblue",alpha=alpha_t)
plt.text(0.8*1E-1,9/8*0.96,r"$T_1^{\rm Ice}\ &\ T_1^{xy}\ &\  E   $",size=size_label_irreps-2)
plt.text(0.15*1E-1,9/8*0.96,r"$ T_1^{\rm Ice} $",size=size_label_irreps-2)
#ins.text(-1,-1.5,r"$T_1^{xy}$",size=size_label_irreps)
plt.grid()
plt.tick_params(labelsize=size_label_irreps)
yvals=[5/8,3/4,7/8,1,9/8]
ylabels=[r"$5/8$",r"$3/4$",r"$7/8$",r"$1$",r"9/8"]
plt.ylim(5/8,9/8)
plt.yticks(yvals,ylabels)


'''
------------------------------------------  Values for the structure factor plots ------------------------------------------
'''
Shrink_hhl=0.7
Shrink_hk0=0.9
size=15
pad_val=0.04
'''
------------------------------------------  Values for the structure factor plots ------------------------------------------
'''



def symmetrize_figure(matrix):
    return (matrix+matrix[:,::-1]+matrix[::-1,:]+matrix[::1,::-1]+matrix.T)/5

sizex="10"
sizey=sizex
sizez=sizex

temp_index_array=["20","40"]
T_structure=np.loadtxt("average_thermodynamic_data_L10.txt")[:,0]
print(T_structure[[20,40]])

Theta="243"#input("Enter the value of theta with sign=")
max_sim_num=50


cmap1 = matplotlib.colors.LinearSegmentedColormap.from_list("", ["navy","dodgerblue","orangered","gold","w"])#["blue","white","orange"]
cmap2 = matplotlib.colors.LinearSegmentedColormap.from_list("", ["midnightblue","royalblue","orange","red"])#["blue","white","orange"]




keyword=cmap2
resp_contour=0

resp_symm=0
levels=50
ticks_labels=[-2,0,2]
for i_temp in range(len(temp_index_array)):
    file_name=file_name="Structure_factor_"+sizex+"_"+sizey+"_"+sizez+"_"+temp_index_array[i_temp]+"_theta"+Theta+".bin"
    my_file = Path(file_name)
    
    if my_file.is_file():

        FILE=np.loadtxt(file_name)

        q1=FILE[:,0]
        q2=FILE[:,1]

        Spin_Structure_factor_hhl=FILE[:,2]
        Spin_Structure_factor_hk0=FILE[:,3]

        Structure_factor_hhl=FILE[:,4]
        Structure_factor_hk0=FILE[:,5]

        Q_size=int(sizex)*4

        Q1=np.reshape(q1,(Q_size,Q_size))
        Q2=np.reshape(q2,(Q_size,Q_size))
     
        q1=FILE[:,0]*2
        q2=FILE[:,1]*2
        extent=(min(q1), max(q1), min(q2), max(q2))

        Spin_Structure_factor_hhl= np.reshape(Spin_Structure_factor_hhl,(Q_size,Q_size))
        Spin_Structure_factor_hk0= np.reshape(Spin_Structure_factor_hk0,(Q_size,Q_size))

        '''
        Eliminating the point at 0
        '''
        index_hhl=np.argmax(Structure_factor_hhl)
        index_hk0=np.argmax(Structure_factor_hk0)
        Structure_factor_hk0[index_hk0]=(Structure_factor_hk0[index_hk0-1]+Structure_factor_hk0[index_hk0+1])/2
        Structure_factor_hhl[index_hhl]=(Structure_factor_hhl[index_hhl-1]+Structure_factor_hhl[index_hhl+1])/2

        Structure_factor_hk0[index_hk0]=np.max(Structure_factor_hk0)
        Structure_factor_hhl[index_hhl]=np.max(Structure_factor_hhl)

        Structure_factor_hhl= np.reshape(Structure_factor_hhl,(Q_size,Q_size))
        Structure_factor_hk0= np.reshape(Structure_factor_hk0,(Q_size,Q_size))

        Q1=Q1[1:,1:]
        Q2=Q2[1:,1:]
        Structure_factor_hhl= Structure_factor_hhl[1:,1:]
        Structure_factor_hk0= Structure_factor_hk0[1:,1:]

        if(i_temp==0):

            ax = fig.add_subplot(spec[0,1])
            if(resp_contour):
                im1=plt.contourf(2*Q1,2*Q2,Structure_factor_hhl,levels,cmap=keyword,shading='auto')
            else:
                im1=plt.pcolormesh(2*Q1,2*Q2,Structure_factor_hhl,cmap=keyword,shading='auto')

            plt.gca().set_aspect(1/np.sqrt(2))
            cbar=plt.colorbar(im1,orientation="vertical",pad=0.05, shrink=Shrink_hhl)
            cbar.ax.tick_params(labelsize=size_label_irreps)
            plt.xlabel("$ [hh0] $",size=size_label_irreps)
            plt.ylabel("$ [00\ell] $",size=size_label_irreps)
            plt.xticks(ticks_labels)
            plt.yticks(ticks_labels)
            plt.tick_params(labelsize=size_label_irreps)

            ax = fig.add_subplot(spec[1,1])
            if(resp_contour):
                im1=plt.contourf(2*Q1,2*Q2,Structure_factor_hk0,levels,cmap=keyword,shading='auto')
            else:
                im1=plt.pcolormesh(2*Q1,2*Q2,Structure_factor_hk0,cmap=keyword,shading='auto')

            plt.gca().set_aspect('equal')
            cbar=plt.colorbar(im1,orientation="vertical",pad=0.05, shrink=Shrink_hk0)
            cbar.ax.tick_params(labelsize=size_label_irreps)
            plt.xlabel("$ [h00] $",size=size_label_irreps)
            plt.ylabel("$ [0k0] $",size=size_label_irreps)
            plt.xticks(ticks_labels)
            plt.yticks(ticks_labels)
            plt.tick_params(labelsize=size_label_irreps)


keyword=cmap2
for i_temp in range(len(temp_index_array)):
    file_name=file_name="Structure_factor_"+sizex+"_"+sizey+"_"+sizez+"_"+temp_index_array[i_temp]+"_theta"+Theta+".bin"
    my_file = Path(file_name)

    if my_file.is_file():

        FILE=np.loadtxt(file_name)

        q1=FILE[:,0]
        q2=FILE[:,1]

        Spin_Structure_factor_hhl=FILE[:,2]
        Spin_Structure_factor_hk0=FILE[:,3]

        Structure_factor_hhl=FILE[:,4]
        Structure_factor_hk0=FILE[:,5]

        Q_size=int(sizex)*4

        Q1=np.reshape(q1,(Q_size,Q_size))
        Q2=np.reshape(q2,(Q_size,Q_size))
        q1=FILE[:,0]*2
        q2=FILE[:,1]*2
        extent=(min(q1), max(q1), min(q2), max(q2))

        Spin_Structure_factor_hhl= np.reshape(Spin_Structure_factor_hhl,(Q_size,Q_size))
        Spin_Structure_factor_hk0= np.reshape(Spin_Structure_factor_hk0,(Q_size,Q_size))

        '''
        Eliminating the point at 0
        '''
        index_hhl=np.argmax(Structure_factor_hhl)
        index_hk0=np.argmax(Structure_factor_hk0)
        Structure_factor_hk0[index_hk0]=(Structure_factor_hk0[index_hk0-1]+Structure_factor_hk0[index_hk0+1])/2
        Structure_factor_hhl[index_hhl]=(Structure_factor_hhl[index_hhl-1]+Structure_factor_hhl[index_hhl+1])/2
        Structure_factor_hk0[index_hk0]=np.max(Structure_factor_hk0)
        Structure_factor_hhl[index_hhl]=np.max(Structure_factor_hhl)

        Structure_factor_hhl= np.reshape(Structure_factor_hhl,(Q_size,Q_size))
        Structure_factor_hk0= np.reshape(Structure_factor_hk0,(Q_size,Q_size))
        
        Q1=Q1[1:,1:]
        Q2=Q2[1:,1:]
        Structure_factor_hhl= Structure_factor_hhl[1:,1:]
        Structure_factor_hk0= Structure_factor_hk0[1:,1:]


        if(i_temp==1):
            ax = fig.add_subplot(spec[0,2])
#            im1=plt.pcolormesh(2*Q1,2*Q2,Structure_factor_hk0,cmap=keyword,shading='auto')
            if(resp_contour):
                im1=plt.contourf(2*Q1,2*Q2,Structure_factor_hhl,levels,cmap=keyword,shading='auto')
            else:
                im1=plt.pcolormesh(2*Q1,2*Q2,Structure_factor_hhl,cmap=keyword,shading='auto')

            plt.gca().set_aspect(1/np.sqrt(2))
            cbar=plt.colorbar(im1,orientation="vertical",pad=0.05, shrink=Shrink_hhl)
            cbar.ax.tick_params(labelsize=size_label_irreps)
            plt.xlabel("$ [hh0] $",size=size_label_irreps)
            plt.ylabel("$ [00\ell] $",size=size_label_irreps)
            plt.xticks(ticks_labels)
            plt.yticks(ticks_labels)
            plt.tick_params(labelsize=size_label_irreps)
            ax = fig.add_subplot(spec[1,2])

            if(resp_contour):
                im1=plt.contourf(2*Q1,2*Q2,Structure_factor_hk0,levels,cmap=keyword,shading='auto')
            else:
                im1=plt.pcolormesh(2*Q1,2*Q2,Structure_factor_hk0,cmap=keyword,shading='auto')
            plt.gca().set_aspect('equal')
            cbar=plt.colorbar(im1,orientation="vertical",pad=0.05, shrink=Shrink_hk0)
            cbar.ax.tick_params(labelsize=size_label_irreps)
            plt.xlabel("$ [h00] $",size=size_label_irreps)
            plt.ylabel("$ [0k0] $",size=size_label_irreps)
            plt.xticks(ticks_labels)
            plt.yticks(ticks_labels)
            plt.tick_params(labelsize=size_label_irreps)

#plt.savefig("Fig_1_PNAS.pdf")
plt.show()

