import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'



L="10"
angle="243"
label_size=35

name_out1="Modes_values_"+ str(L)+ "_"+ str(L)+ "_"+ str(L)+"_theta"+str(angle)+"_IM.bin";
name_out2="Modes_values_"+ str(L)+ "_"+ str(L)+ "_"+ str(L)+"_theta"+str(angle)+"_SI.bin";

FILE1=np.loadtxt(name_out1)
FILE2=np.loadtxt(name_out2)


'''
Histogram of the modes found
'''
modes=[]
print(FILE2.shape)

num_configs=FILE2.shape[0]
num_modes=FILE2.shape[1]
label_size=20

Zero_energy_m3=[]
Zero_energy_m6=[]
Zero_energy_m9=[]
fig=plt.figure(figsize=(10,6))
plt.subplots_adjust(left=0.13, bottom=None, right=0.98, top=0.95, wspace=0.35, hspace=0.35)
for i in range(0,1):
    modes_i1=FILE1[i,:]
    modes_i2=FILE2[i,:]

    if(i%20==0 and 1):
        plt.subplot(221)
        plt.semilogy(abs(modes_i1),"k")
        plt.ylabel(r"$E$",size=label_size)
        plt.xlabel(r"$\mathrm{Eigenvalue\ index}$",size=label_size)
        plt.title(r"$\mathrm{Arbitrary}\ \mathrm{IM}\ \mathrm{state}$" ,size=label_size)
        plt.tick_params(labelsize=label_size)
        plt.grid()
        plt.subplot(222)
        plt.semilogy(abs(modes_i2),"k")
        plt.ylabel(r"$E$",size=label_size)
        plt.xlabel(r"$\mathrm{Eigenvalue\ index}$",size=label_size)
        plt.title(r"$\mathrm{Spin}$"+r"-$\mathrm{ice}\ \mathrm{state}$" ,size=label_size)
        plt.tick_params(labelsize=label_size)
        plt.grid()
        
        
'''
Data for the Fit obtained from the real space CLTE
'''

L=np.array([2,3,4,6,8,10,12])
Fraction=np.array([0.3593,0.3009,0.2793,0.2633,0.2576,0.2549,0.2534])
x=np.linspace(0,1/2,10)

'''
Fits to a quadratic and a cubic polynomia
'''


a3,a2,a1,a0=np.polyfit(1/L,Fraction,3)
print(a0,a1,a2,a3)
plt.subplot(212)
plt.plot(x,a0+a1*x+a2*x**2+a3*x**3,color="k",label=r"$a_0+a_1(1/L)+a_2(1/L)^2+a_3(1/L)^3$")
plt.grid()

'''
Data ploted as a function of 1/L
'''

plt.semilogx(1/L,Fraction,"ro",linewidth=15)

plt.xlabel(r"$1/L$",size=label_size)
plt.ylabel(r"$N_0(L)/8L^3$",size=label_size)
plt.axhline(0.25,color="b",linestyle="--")

plt.legend(prop={'size': 25})
plt.tick_params(labelsize=label_size)

L=np.array([2,3,4,6,8,10,12])

plt.xticks(1/L,["$1/%i$" %x for x in L])
plt.savefig("Figure_3.pdf")
plt.show()



Zero_energy_m3=[]
Zero_energy_m6=[]
Zero_energy_m9=[]
fig=plt.figure(figsize=(10,10))
plt.subplots_adjust(left=0.13, bottom=None, right=0.98, top=0.95, wspace=0.35, hspace=0.35)

#fig=plt.figure(figsize=(10,7))
#plt.subplots_adjust(left=0.13, bottom=None, right=0.98, top=0.95, wspace=0.35, hspace=0.35)


for i in range(0,1):
    modes_i1=FILE1[i,:]
    modes_i2=FILE2[i,:]

    if(i%20==0 and 1):
        plt.subplot(221)
        plt.semilogy(np.sort(abs(modes_i1)),"k")
        plt.ylabel(r"$E$",size=label_size)
        plt.xlabel(r"$\mathrm{Eigenvalue\ index}$",size=label_size)
        plt.title(r"$\mathrm{Arbitrary}\ \mathrm{IM}\ \mathrm{state}$" ,size=label_size)
        plt.tick_params(labelsize=label_size)
        plt.text(-1500,40, r"$ \mathrm{(a)} $", size=label_size)
        plt.text(-1500,5*1E-9, r"$ \mathrm{(c)} $", size=label_size)
        plt.text(10000,40, r"$ \mathrm{(b)} $", size=label_size)
        plt.grid()
        plt.subplot(222)
        plt.semilogy(np.sort(abs(modes_i2)),"k")
        plt.ylabel(r"$E$",size=label_size)
        plt.xlabel(r"$\mathrm{Eigenvalue\ index}$",size=label_size)
        plt.title(r"$\mathrm{Spin}$"+r"-$\mathrm{ice}\ \mathrm{state}$" ,size=label_size)
        plt.tick_params(labelsize=label_size)
        plt.grid()
        
        
'''
Data for the Fit obtained from the real space CLTE
'''

L=np.array([2,3,4,6,8,10,12])
Fraction=np.array([0.3593,0.3009,0.2793,0.2633,0.2576,0.2549,0.2534])
x=np.linspace(0,1/2,10)

'''
Fits to a quadratic and a cubic polynomia
'''


a3,a2,a1,a0=np.polyfit(1/L,Fraction,3)
print(a0,a1,a2,a3)
plt.subplot(212)
plt.plot(x,a0+a1*x+a2*x**2+a3*x**3,color="k",label=r"$a_0+a_1(1/L)+a_2(1/L)^2+a_3(1/L)^3$")
plt.grid()

'''
Data ploted as a function of 1/L
'''

plt.semilogx(1/L,Fraction,"ro",linewidth=15)

plt.xlabel(r"$1/L$",size=label_size)
plt.ylabel(r"$N_0(L)/8L^3$",size=label_size)
plt.axhline(0.25,color="b",linestyle="--")

plt.legend(prop={'size': 25})
plt.tick_params(labelsize=label_size)

L=np.array([2,3,4,6,8,10,12])

plt.xticks(1/L,["$1/%i$" %x for x in L])
plt.savefig("Figure_3_sorted_PNAS.pdf")
plt.show()
exit()
#
#from matplotlib import gridspec
#fig = plt.figure(figsize=(10,0))
#spec = gridspec.GridSpec(ncols=1, nrows=2,right=0.98, top=0.95, wspace=0.35, hspace=0.3)
#ax = fig.add_subplot(spec[0,0])

fig=plt.figure(figsize=(15,10))
plt.subplots_adjust(left=0.00, bottom=None, right=0.98, top=0.95, wspace=0.35, hspace=0.3)

for i in range(0,1):
    modes_i1=FILE1[i,:]
    modes_i2=FILE2[i,:]

    if(i%20==0 and 1):
        plt.subplot(221)
        plt.plot(np.sort(abs(modes_i1)),"k")
        plt.ylabel(r"$E$",size=label_size)
        plt.xlabel(r"$\mathrm{Eigenvalue\ index}$",size=label_size)
        plt.title(r"$\mathrm{Arbitrary}\ \mathrm{IM}\ \mathrm{state}$" ,size=label_size)
        plt.tick_params(labelsize=label_size)
        plt.grid()
        
        plt.subplot(222)
        plt.plot(np.sort(abs(modes_i2)),"k")
        plt.ylabel(r"$E$",size=label_size)
        plt.xlabel(r"$\mathrm{Eigenvalue\ index}$",size=label_size)
        plt.title(r"$\mathrm{Spin}$"+r"-$\mathrm{ice}\ \mathrm{state}$" ,size=label_size)
        plt.tick_params(labelsize=label_size)
        plt.grid()
       
        
        
'''
Data for the Fit obtained from the real space CLTE
'''

L=np.array([2,3,4,6,8,10,12])
Fraction=np.array([0.3593,0.3009,0.2793,0.2633,0.2576,0.2549,0.2534])
x=np.linspace(0,1/2,10)

'''
Fits to a quadratic and a cubic polynomia
'''


a3,a2,a1,a0=np.polyfit(1/L,Fraction,3)
print(a0,a1,a2,a3)
#ax = fig.add_subplot(spec[0,0])
#plt.subplot(212)
plt.plot(x,a0+a1*x+a2*x**2+a3*x**3,color="k",label=r"$a_0+a_1(1/L)+a_2(1/L)^2+a_3(1/L)^3$")
plt.grid()

'''
Data ploted as a function of 1/L
'''

plt.semilogx(1/L,Fraction,"ro",linewidth=15)

plt.xlabel(r"$1/L$",size=label_size)
plt.ylabel(r"$N_0(L)/8L^3$",size=label_size)
plt.axhline(0.25,color="b",linestyle="--")

plt.legend(prop={'size': 25})
plt.tick_params(labelsize=label_size)

L=np.array([2,3,4,6,8,10,12])

plt.xticks(1/L,["$1/%i$" %x for x in L])
plt.savefig("Figure_3_sorted_PNAS.pdf")
plt.show()


#plt.hist(abs(modes_i2),bins=1000)
#plt.xlabel(r"$E/J$")
#plt.show()
