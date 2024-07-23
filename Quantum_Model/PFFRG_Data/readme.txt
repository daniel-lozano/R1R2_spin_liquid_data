The folder contains static spin correlations $\bar{\chi}^{\mu\nu, \Lambda}_{ij}$ depending on site arguments $i$ and $j$, spin components $\mu, \nu \in \{ x,y,z \}$, and a cutoff $\Lambda$.

"Pyrochlore_N32_L1_Lams.txt" contains a list of cutoffs $\Lambda$ for which spin correlations are given out.

"Pyrochlore_N32_L111.txt" contains spin correlations for all given cutoffs, and for all lattice vectors below a distance of four nearest neighbor spacings that begin on a reference site of the lattice.
The row of a file entry determines $\Lambda$ and the column determines the lattice vector. The lattice vectors are specified in the "plot_script.py" by the list "LatticeVectors".

"plot_script.py" contains a Python script that plots the order parameter flows and spin structure factors for given PFFRG spin correlations of a non-Kramers pyrochlore model.
