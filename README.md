# RED-SEA
This is a red-sea cossim simulator

## Execution
You may reference to the following file in order to execute the MPICH on COSSIM (1node - up to 64cores) [MPICH-on-COSSIM-1node-64cores.md](MPICH-on-COSSIM-1node-64cores.md)

$GEM5/build/ARM/gem5.opt -d $GEM5/node0 $GEM5/configs/example/arm/starter_fs.py --kernel=vmlinux.arm64 --num-cores=2 --disk-image=ubuntu-18.04-arm64-docker.img
