# RED-SEA
This is the COSSIM extension which is developed in the context of RED-SEA H2020 project.

## Execution
We have created a Virual Machine which we have install everything there. You may donwload it from [here](link) (It is tested using VMWare 16.1 tools - [download for here](http://kition.mhl.tuc.gr:8000/f/1932b6edea)).

You may reference to the following file in order to execute the MPICH on COSSIM (1node - up to 64cores) [MPICH-on-COSSIM-1node-64cores.md](MPICH-on-COSSIM-1node-64cores.md). 

In addition  Finally here you can see videos with execution examples Apollon gem5-Ptolemy , APOLLON 2nodes.

$GEM5/build/ARM/gem5.opt -d $GEM5/node0 $GEM5/configs/example/arm/starter_fs.py --kernel=vmlinux.arm64 --num-cores=2 --disk-image=ubuntu-18.04-arm64-docker.img
