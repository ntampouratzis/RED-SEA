# RED-SEA
This is the COSSIM [1] extension which is developed in the context of RED-SEA H2020 project. The extended simulation framework can simulate complete heterogeneous HPC Systems supporting ARM and RISC-V CPUs.

## The contribution of this work can be summarized in the following points:
 - An innovative flow to enable the designers to simulate the complete aspects of HPC Systems (i.e. CPU and Network Environment) through real MPI applications within one simulation framework creating HPC runtime environment inside simulation framework.
 - The integration of PCI Host to RISC-V GEM5 board and adaptation of GEM5 ethernet card to it in order to simulate multi-node RISC-V systems in COSSIM simulator (we merge the development code in the official GEM5 repository).
 - The integration of VEF traces Framework [2] to analyze communication traffic of MPI-based applications and generate traffic traces that can be used to feed other network simulator tools.


## Execution
We have created a Virual Machine which we have install everything there. You may donwload it from [here](http://kition.mhl.tuc.gr:8000/d/0cabeb13c1/) (It is tested using VMWare 16.1 tools - [download the VM tools for Windows from here](http://kition.mhl.tuc.gr:8000/f/1932b6edea)). The VM password is <b>redsea1234</b> .

You may see the related video for instructions [MPI-on-COSSIM-multinode](http://kition.mhl.tuc.gr:8000/f/faec6bbe61/).

## References
<a id="1">[1]</a> 
N. Tampouratzis, I. Papaefstathiou, A. Nikitakis, A. Brokalakis,
S. Andrianakis, A. Dollas, M. Marcon, and E. Plebani, “A novel,
highly integrated simulator for parallel and distributed systems,”
ACM Trans. Archit. Code Optim., vol. 17, no. 1, Mar. 2020.
Available: https://dl.acm.org/doi/10.1145/3378934

<a id="2">[2]</a> Andújar, F.J., Sánchez de la Rosa, M., Escudero-Sahuquillo, J. et al. Extending the VEF traces framework to model data center network workloads. J Supercomput 79, 814–831 (2023). https://doi.org/10.1007/s11227-022-04692-0
