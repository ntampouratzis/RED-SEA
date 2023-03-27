# How to execute MPICH on COSSIM framework?

# Setup the COSSIM environment

## 1. Declare how many gem5 nodes you want to simulate
```
gedit /home/red-sea/COSSIM/cgem5/run.sh
```

This is an example with 3 nodes:
```
$GEM5/build/ARM/gem5.fast --listener-mode=on -r -d $GEM5/node0 $GEM5/configs/example/arm/starter_fs.py --kernel=vmlinux.arm64 --num-cores=2 --disk-image=ubuntu-18.04-arm64-docker.img --SynchTime=100us --RxPacketTime=10us --TotalNodes=3 --nodeNum=0 --script=$GEM5/configs/boot/COSSIM/script0.rcS --etherdump=$GEM5/node0/ether_node0 --cossim &
$GEM5/build/ARM/gem5.fast --listener-mode=on -r -d $GEM5/node1 $GEM5/configs/example/arm/starter_fs.py --kernel=vmlinux.arm64 --num-cores=2 --disk-image=ubuntu-18.04-arm64-docker.img --SynchTime=100us --RxPacketTime=10us --TotalNodes=3 --nodeNum=1 --script=$GEM5/configs/boot/COSSIM/script1.rcS --etherdump=$GEM5/node1/ether_node1 --cossim &
$GEM5/build/ARM/gem5.fast --listener-mode=on -r -d $GEM5/node2 $GEM5/configs/example/arm/starter_fs.py --kernel=vmlinux.arm64 --num-cores=2 --disk-image=ubuntu-18.04-arm64-docker.img --SynchTime=100us --RxPacketTime=10us --TotalNodes=3 --nodeNum=2 --script=$GEM5/configs/boot/COSSIM/script2.rcS --etherdump=$GEM5/node2/ether_node2 --cossim &
```

If you may need to add more nodes please the add the following line (where XXX the number of node - i.e. if you would like to add a 4th node, XXX=3 and XXX+1=4. To be noticed that you need to change the TotalNodes to TotalNodes=4 in all of the above commands):
```
$GEM5/build/ARM/gem5.fast --listener-mode=on -r -d $GEM5/nodeXXX $GEM5/configs/example/arm/starter_fs.py --kernel=vmlinux.arm64 --num-cores=2 --disk-image=ubuntu-18.04-arm64-docker.img --SynchTime=100us --RxPacketTime=10us --TotalNodes=XXX+1 --nodeNum=XXX --script=$GEM5/configs/boot/COSSIM/scriptXXX.rcS --etherdump=$GEM5/nodeXXX/ether_nodeXXX --cossim &
```

## 2. Declare the gem5 boot scripts 
Create for each gem5 node a configuration script with the network parameters (lo, IP, netmask) as well as the command for rsh server start up.
This is an example for <b>node0</b> (the same configuartions must be declared for the other nodes):

```
ifconfig eth0 hw ether 00:90:00:00:00:00
ifconfig lo 127.0.0.1                             #Configure the localhost
ifconfig eth0 192.168.0.2                         #Configure the Ethernet
ifconfig eth0 netmask 255.255.255.0               #Configure the Netmask
ulimit -c unlimited

/etc/init.d/xinetd start #Start the rsh server

exec /bin/bash
```
The path for the scripts is (as declared in run.sh):
```
$GEM5/configs/boot/COSSIM
```
## 3. Declare how many OMNET++ nodes you want to simulate

Open OMNETPP

```
omnetpp
```

Go to HLANode --> src --> Txc.ned (in Project Explorer). 

This is an example with 3 nodes:
```
package HLANode;

simple Txc0
{
	parameters:
		double RXPacketTime = default(0.00001);
		int nodeNo = default(0);
		bool sendInitialMessage = default(false);

		@display("i=block/routing");
	gates:
		inout gate;
}
simple Txc1 extends Txc0
{
		parameters:
		RXPacketTime = default(0.00001);
		nodeNo = default(1);

		sendInitialMessage = default(false);
		@display("i=block/routing");
}
simple Txc2 extends Txc0
{
		parameters:
		RXPacketTime = default(0.00001);
		nodeNo = default(2);

		sendInitialMessage = default(false);
		@display("i=block/routing");
}
simple SyncNode
{
	parameters:
		int NumberOfHLANodes = default(3);
		double SynchTime = default(0.0001);

		bool sendInitialMessage = default(false);
		@display("i=block/routing");
	gates:
		input in;
		output out;
}
```
<b>You can add OMNET++ node adding the below code (do not forget to change the NumberOfHLANodes to default(4)) in the above SynchNode </b>:

```
simple Txc3 extends Txc0
{
		parameters:
		RXPacketTime = default(0.00001);
		nodeNo = default(3);

		sendInitialMessage = default(false);
		@display("i=block/routing");
}
```

To be noticed that the same number of gem5 and omnet++ nodes must be configured (We will simplify the procedure of 1 and 2 steps through GUI).

## 4. Connect the OMNET++ nodes

You need to connect the OMNET++ nodes through ARPTest.ned file (test --> simulations --> ARPTest.ned).


# Mount the Ubuntu 18.04 simulated image and configure the MPI environment

## 1. Mount the disk image
```
sudo mount -o loop,offset=65536 $HOME/COSSIM/kernels/disks/ubuntu-18.04-arm64-docker.img /mnt
cd /mnt
```
<b> To be noticed that the sudo code is: redsea1234 </b>

## 2. Copy the MPI application to Ubuntu 18.04 simulated image
```
sudo cp /home/red-sea/Desktop/mpi_hello_world.c .
```

## 3. Emulate the image through QEMU
```
sudo mount --bind /proc /mnt/proc
sudo mount --bind /dev /mnt/dev
sudo chroot .

echo "nameserver 8.8.8.8" > /etc/resolv.conf
```

## 4. Compile the MPI application to Ubuntu 18.04 simulated image
```
mpicc -o mpi_hello_world mpi_hello_world.c
```

## 5. Create the hosts file in Ubuntu 18.04 simulated image
You need to add the IP with the hostname for each gem5 node
```
vi /etc/hosts
```

This is an example for 3 nodes: \
127.0.0.1 localhost \
192.168.0.2 node0 \
192.168.0.3 node1 \
192.168.0.4 node2

## 6. Create a .rhosts file in Ubuntu 18.04 simulated image
You need to create a .rhosts in the root home directory and write the hostnames of the hosts in order to access password-free
```
vi /root/.rhosts
```

This is an example for 3 nodes: \
node0 root \
node1 root \
node2 root

## 7. Create a host_file in Ubuntu 18.04 simulated image
You need to create a host_file in order to tell the MPI where the application must be executed

```
vi host_file
```

This is an example for 3 nodes (1 process/per node): \
node0:1 \
node1:1 \
node2:1

## 8. Create Scripts in order to execute the MPI application without VEF traces
The following 3 scripts are used in order to execute the MPI application <b>without VEF traces</b> (in case you would like to execute the application with VEF traces, please go to Step 9).
### 1. Setup the correct hostname in all gem5 nodes (through node0)

```
vi 1.setup_script
```

This is an example for 3 nodes: \
hostname node0                  #declare the hostname for node0 \
rsh 192.168.0.3 hostname node1  #declare the hostname for node1 \
rsh 192.168.0.4 hostname node2  #declare the hostname for node2


### 2. Execute the MPI application (through node0)
```
vi 2.mpi_execution_script
```
This is an example for 3 nodes: \
m5 resetstats                   #reset the gem5 statistics before mpi execution \
mpirun -launcher rsh -n 3 -f host_file ./mpi_hello_world #execute the app \
m5 dumpstats                    #dump the gem5 statistics

### 3. Terminate the gem5s (through node0)
```
vi 3.finalization_script
```

This is an example for 3 nodes: \
rsh 192.168.0.3 m5 exit &       #terminate the gem5 node1 execution \
rsh 192.168.0.4 m5 exit &       #terminate the gem5 node2 execution

## 9. Create Scripts in order to execute the MPI application with VEF Traces
The following 4 scripts are used in order to execute the MPI application <b>with VEF traces</b> (in case you would like to execute the application with VEF traces, please skip the step 8).

### 1. Setup the correct hostname in all gem5 nodes (through node0)

```
vi 1.setup_script
```

This is an example for 3 nodes: \
hostname node0                  #declare the hostname for node0 \
rsh 192.168.0.3 hostname node1  #declare the hostname for node1 \
rsh 192.168.0.4 hostname node2  #declare the hostname for node2


### 2. Execute the MPI application with VEF support (through node0)
```
vi 2b.vef_mpi_execution_script 
```
This is an example for 3 nodes:

#declare the vef prospector path \
export PATH=$PATH:/opt/vef_prospector/bin/ \
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/vef_prospector/lib/

m5 resetstats                   #reset the gem5 statistics before mpi execution \
vmpirun -launcher rsh -n 3 -f host_file ./mpi_hello_world #execute the app \
m5 dumpstats                    #dump the gem5 statistics 


### 3. Gather the VEF traces from other nodes to node0
This is a script in order to gather the VEF traces from node1 and node2 to node0. It was necessary in order to be created the final trace file (.vef) through VEF mixer.
```
vi 2c.get_vef_traces
```
This is an example for 3 nodes:

#declare the vef prospector path \
export PATH=$PATH:/opt/vef_prospector/bin/ \
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/vef_prospector/lib/

#go to traces directory \
cd /mpi_hello_world-*

#get traces from node1 \
rsh 192.168.0.3 cat /mpi_hello_world-*/1.comm >> 1.comm \
rsh 192.168.0.3 cat /mpi_hello_world-*/1.veft >> 1.veft

#get traces from node2 \
rsh 192.168.0.4 cat /mpi_hello_world-*/2.comm >> 2.comm \
rsh 192.168.0.4 cat /mpi_hello_world-*/2.veft >> 2.veft

#Execute vef_mixer \
vef_mixer -i VEFT.main -o output_trace.vef

#read the traces \
cat output_trace.vef  

### 4. Terminate the gem5s (through node0)
```
vi 3.finalization_script
```

This is an example for 3 nodes: \
rsh 192.168.0.3 m5 exit &       #terminate the gem5 node1 execution \
rsh 192.168.0.4 m5 exit &       #terminate the gem5 node2 execution


## 10. Umount the disk image
exit \
cd \
sudo umount /mnt/proc \
sudo umount /mnt/dev \
sudo umount /mnt
